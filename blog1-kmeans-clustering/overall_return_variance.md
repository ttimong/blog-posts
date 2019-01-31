

```python
import pandas as pd
import numpy as np
import datetime 
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline 

pd.set_option('display.max_columns', 100)
```


```python
# raw data is taken from Stocker package which uses Quandl API
agg_df = pd.read_csv('./agg_data2.csv', index_col=0)
```

    C:\Users\timothy.ong\AppData\Local\Continuum\anaconda3\lib\site-packages\numpy\lib\arraysetops.py:522: FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison
      mask |= (ar1 == a)
    


```python
# narrowing data set to 2012 - 2017
# creating new column `year`
agg_df2 = (
    agg_df
    .pipe(lambda x: x.assign(year=pd.to_datetime(x.date).dt.year))
    .query("year >= 2012")
    [['ticker', 'date', 'year', 'open', 'close']]
)
```


```python
# getting the first day and last day of each year that is available in the data set
first_date_list = [agg_df2.query("year == '{}'".format(2012+i)).date.min() for i in range(6)]
last_date_list = [agg_df2.query("year == '{}'".format(2012+i)).date.max() for i in range(6)]
first_date_df =pd.DataFrame({"date": first_date_list}) 
last_date_df = pd.DataFrame({"date": last_date_list})
```


```python
# filtering first day data
agg_first_date_df = (
    agg_df2
    .merge(first_date_df, on='date', how='inner')
    .pipe(lambda x: x.assign(year=x.date.str[:4]))
    .rename(columns={"open": "open_first_day", "close": "close_first_day"})
    .reset_index(drop=True)
    [['ticker', 'year', 'open_first_day', 'close_first_day']]
)

# filtering last day data
agg_last_date_df = (
    agg_df2
    .merge(last_date_df, on='date', how='inner')
    .pipe(lambda x: x.assign(year=x.date.str[:4]))
    .rename(columns={"open": "open_last_day", "close": "close_last_day"})
    .reset_index(drop=True)
    [['ticker', 'year', 'open_last_day', 'close_last_day']]
)

# calculating yearly return and then averaging them to get average yearly returns for each stock
agg_gains_df = (
    agg_first_date_df
    .merge(agg_last_date_df, on=['ticker', 'year'], how='left')
    .pipe(lambda x: x.assign(gains_dollar=x.close_last_day-x.open_first_day))
    .pipe(lambda x: x.assign(gains_pctg=x.gains_dollar/x.open_first_day))
    .groupby("ticker")
    .agg({"gains_pctg": "mean"})
    .reset_index()
    .rename(columns={"gains_pctg": "avg_yearly_returns"})
)

# calculating overall variance using each year's return
agg_var_df = (
    agg_first_date_df
    .merge(agg_last_date_df, on=['ticker', 'year'], how='left')
    .pipe(lambda x: x.assign(gains_dollar=x.close_last_day-x.open_first_day))
    .pipe(lambda x: x.assign(gains_pctg=x.gains_dollar/x.open_first_day))
    [['ticker', 'gains_pctg']]
    .groupby("ticker")
    .agg(np.var)
    .reset_index()
    .rename(columns={"gains_pctg": "variance"})
)

agg_df3 = (
    agg_gains_df
    .merge(agg_var_df, on='ticker', how='inner')
)
```


```python
agg_df3.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ticker</th>
      <th>avg_yearly_returns</th>
      <th>variance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>0.133075</td>
      <td>0.068609</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AAN</td>
      <td>0.084080</td>
      <td>0.057674</td>
    </tr>
    <tr>
      <th>2</th>
      <td>AAON</td>
      <td>0.126208</td>
      <td>0.089675</td>
    </tr>
  </tbody>
</table>
</div>




```python
agg_df3.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 1651 entries, 0 to 1650
    Data columns (total 3 columns):
    ticker                1651 non-null object
    avg_yearly_returns    1651 non-null float64
    variance              1651 non-null float64
    dtypes: float64(2), object(1)
    memory usage: 51.6+ KB
    


```python
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler
from sklearn.cluster import KMeans
from sklearn import metrics
```


```python
def plot_cluster(df, max_loop=50):
    """
    Looking at the performance of various number of clusters using K-Means.
    Performance is evaluated by within cluster SSE and silhouette score.
    """
    try:
        df.drop('cluster', axis=1, inplace=True)
    except:
        next
    X = df.iloc[:,1:]
    
    # robust scaling is used so that the centering and scaling statistics are therefore not influenced by a few number of very large marginal outliers as they are based on percentiles
    rb = RobustScaler()
    X_rb = rb.fit_transform(X)
    
    sse_within_cluster = {}
    silhouette_score = {}
    
    for k in range(2, max_loop):
        kmeans = KMeans(n_clusters=k,  random_state=10, n_init=10, n_jobs=-1)
        kmeans.fit(X_rb)
        sse_within_cluster[k] = kmeans.inertia_
        silhouette_score[k] = metrics.silhouette_score(X_rb, kmeans.labels_, random_state=10)

    _ = plt.figure(figsize=(10,6))
    ax1 = plt.subplot(211)
    _ = plt.plot(list(sse_within_cluster.keys()), list(sse_within_cluster.values()))
    _ = plt.xlabel("Number of Clusters")
    _ = plt.ylabel("SSE Within Cluster")
    _ = plt.title("Within Cluster SSE After K-Means Clustering")
    _ = plt.xticks([i for i in range(2, max_loop)], rotation=75)
    
    ax2 = plt.subplot(212)
    _ = plt.plot(list(silhouette_score.keys()), list(silhouette_score.values()))
    _ = plt.xlabel("Number of Clusters")
    _ = plt.ylabel("Silhouette Score")
    _ = plt.title("Silhouette Score After K-Means Clustering")
    _ = plt.xticks([i for i in range(2, max_loop)], rotation=75)
    
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.5, wspace=0.35)
```


```python
plot_cluster(agg_df3, max_loop=25)
```


![png](overall_return_variance_files/overall_return_variance_9_0.png)


1. From the first graph, `Within Cluster SSE After K-Means Clustering`, we can see that as the number of clusters increase pass 4, the sum of square of errors within clusters plateaus off. 

2. As for the second graph, `Silhouette Score After K-Means Clustering`, we can see that there are various parts of the graph where a kink can be seen. 


```python
def apply_cluster(df, clusters=2):
    """
    Applying K-Means with the optimal number of clusters identified
    """
    try:
        df.drop('cluster', axis=1, inplace=True)
    except:
        next
    X = df.iloc[:,1:]
    rb = RobustScaler()
    X_rb = rb.fit_transform(X)
    kmeans = KMeans(n_clusters=clusters, random_state=10, n_init=10, n_jobs=-1)  
    kmeans.fit(X_rb) 
    score = metrics.silhouette_score(X_rb, kmeans.labels_, random_state=10)
    df['cluster'] = kmeans.labels_
    sse_within_cluster = kmeans.inertia_
    
    print("clustering performance")
    print("-----------------------------------")
    print("silhouette score: " + str(score.round(2)))
    print("sse withing cluster: " + str(sse_within_cluster.round()))
    
    return df
```


```python
first_trial = apply_cluster(agg_df3, clusters=17)
```

    clustering performance
    -----------------------------------
    silhouette score: 0.79
    sse withing cluster: 4925.0
    


```python
cluster_perf_df = (
    first_trial
    .groupby('cluster')
    .agg({"avg_yearly_returns":"mean", "variance":"mean", "ticker":"count"})
    .sort_values('avg_yearly_returns')
    .reset_index()
)

cluster_perf_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cluster</th>
      <th>avg_yearly_returns</th>
      <th>variance</th>
      <th>ticker</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0.128180</td>
      <td>0.105072</td>
      <td>1506</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15</td>
      <td>0.399462</td>
      <td>1.055879</td>
      <td>80</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10</td>
      <td>0.665059</td>
      <td>3.106788</td>
      <td>28</td>
    </tr>
    <tr>
      <th>3</th>
      <td>14</td>
      <td>1.003335</td>
      <td>5.965267</td>
      <td>15</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6</td>
      <td>1.212379</td>
      <td>9.210504</td>
      <td>6</td>
    </tr>
    <tr>
      <th>5</th>
      <td>8</td>
      <td>1.638056</td>
      <td>17.217217</td>
      <td>3</td>
    </tr>
    <tr>
      <th>6</th>
      <td>16</td>
      <td>1.811096</td>
      <td>22.714211</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7</th>
      <td>13</td>
      <td>2.150359</td>
      <td>29.579875</td>
      <td>3</td>
    </tr>
    <tr>
      <th>8</th>
      <td>11</td>
      <td>2.248405</td>
      <td>40.914102</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9</th>
      <td>12</td>
      <td>2.853394</td>
      <td>51.105084</td>
      <td>1</td>
    </tr>
    <tr>
      <th>10</th>
      <td>3</td>
      <td>3.090436</td>
      <td>35.033572</td>
      <td>1</td>
    </tr>
    <tr>
      <th>11</th>
      <td>9</td>
      <td>3.846878</td>
      <td>66.493500</td>
      <td>1</td>
    </tr>
    <tr>
      <th>12</th>
      <td>4</td>
      <td>4.134567</td>
      <td>84.399514</td>
      <td>1</td>
    </tr>
    <tr>
      <th>13</th>
      <td>5</td>
      <td>4.593472</td>
      <td>130.385703</td>
      <td>1</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2</td>
      <td>5.828209</td>
      <td>180.088451</td>
      <td>1</td>
    </tr>
    <tr>
      <th>15</th>
      <td>7</td>
      <td>6.185437</td>
      <td>217.825908</td>
      <td>1</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1</td>
      <td>10.729512</td>
      <td>759.066239</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



From 


```python
agg_df3_sub = agg_df3.query("cluster == 0").reset_index(drop=True)
```


```python
plot_cluster(agg_df3_sub, max_loop=25)
```


![png](overall_return_variance_files/overall_return_variance_16_0.png)



```python
second_trial= apply_cluster(agg_df3_sub, clusters=6)
```

    clustering performance
    -----------------------------------
    silhouette score: 0.38
    sse withing cluster: 630.0
    


```python
sub_cluster_perf_df = (
    second_trial
    .groupby('cluster')
    .agg({"avg_yearly_returns":"mean", "variance":"mean", "ticker":"count"})
    .sort_values('avg_yearly_returns')
    .reset_index()
)

sub_cluster_perf_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cluster</th>
      <th>avg_yearly_returns</th>
      <th>variance</th>
      <th>ticker</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>-0.070141</td>
      <td>0.095642</td>
      <td>184</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>0.074051</td>
      <td>0.364641</td>
      <td>87</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>0.101346</td>
      <td>0.043300</td>
      <td>638</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>0.123799</td>
      <td>0.168898</td>
      <td>190</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>0.246546</td>
      <td>0.076607</td>
      <td>331</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1</td>
      <td>0.391000</td>
      <td>0.313726</td>
      <td>76</td>
    </tr>
  </tbody>
</table>
</div>




```python
second_trial.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ticker</th>
      <th>avg_yearly_returns</th>
      <th>variance</th>
      <th>cluster</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>0.133075</td>
      <td>0.068609</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AAN</td>
      <td>0.084080</td>
      <td>0.057674</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>AAON</td>
      <td>0.126208</td>
      <td>0.089675</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
def get_sharpe_ratio_df(df):
    df_w_sharpe_ratio = (
        df
        .pipe(lambda x: x.assign(avg_risk_free_rate=avg_risk_free_rate/100))
        .pipe(lambda x: x.assign(std_dev=np.sqrt(x.variance)))
        .pipe(lambda x: x.assign(sharpe_ratio=(x.avg_yearly_returns-x.avg_risk_free_rate)/x.std_dev))
    )

    return df_w_sharpe_ratio
```


```python
second_trial_w_sharpe_ratio = get_sharpe_ratio_df(second_trial)
```


```python
def get_transform_df(df_w_sharpe_ratio):
    df_yearly_returns = (
        df_w_sharpe_ratio
        [['avg_yearly_returns', 'cluster']]
        .pipe(lambda x: x.assign(type='avg_yearly_returns'))
        .rename(columns={"avg_yearly_returns": "rate"})
    )

    df_variance = (
        df_w_sharpe_ratio
        [['variance', 'cluster']]
        .pipe(lambda x: x.assign(type='variance'))
        .rename(columns={"variance": "rate"})
    )

    df_sharpe_ratio = (
        df_w_sharpe_ratio
        [['sharpe_ratio', 'cluster']]
    )

    df_transform = pd.concat([df_yearly_returns, df_variance], axis=0)

    return df_transform, df_sharpe_ratio
```


```python
sub_cluster_transform, sub_cluster_sharpe_ratio = get_transform_df(second_trial_w_sharpe_ratio)
```


```python
def cluster_perf(transform_df, sharpe_ratio_df):
    _  = plt.figure(figsize=(15,7))

    ax1 = plt.subplot(121)
    _ = sns.boxplot(x='cluster', y='rate', hue='type', data=transform_df)
    _ = plt.title("Distribution of Returns and Variance for each Cluster")

    ax2 = plt.subplot(122)
    _ =sns.boxplot(x='cluster', y='sharpe_ratio', data=sharpe_ratio_df, color='royalblue')
    _ = plt.title("Distribution of Sharpe Ratio for each Cluster")
```


```python
cluster_perf(sub_cluster_transform, sub_cluster_sharpe_ratio)
```


![png](overall_return_variance_files/overall_return_variance_25_0.png)



```python
best_sub_cluster = second_trial.query("cluster == 2")
```


```python
plot_cluster(best_sub_cluster, max_loop=15)
```

    C:\Users\timothy.ong\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\frame.py:3697: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      errors=errors)
    


![png](overall_return_variance_files/overall_return_variance_27_1.png)



```python
third_trial = apply_cluster(best_sub_cluster, clusters=4)
```

    C:\Users\timothy.ong\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\frame.py:3697: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      errors=errors)
    

    clustering performance
    -----------------------------------
    silhouette score: 0.39
    sse withing cluster: 74.0
    

    C:\Users\timothy.ong\AppData\Local\Continuum\anaconda3\lib\site-packages\ipykernel_launcher.py:15: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      from ipykernel import kernelapp as app
    


```python
best_sub_cluster_perf = (    
    third_trial
    .groupby('cluster')
    .agg({"avg_yearly_returns":"mean", "variance":"mean", "ticker":"count"})
    .sort_values('avg_yearly_returns')
    .reset_index()
)
best_sub_cluster_perf
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cluster</th>
      <th>avg_yearly_returns</th>
      <th>variance</th>
      <th>ticker</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>0.199555</td>
      <td>0.085915</td>
      <td>102</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0.227018</td>
      <td>0.034496</td>
      <td>111</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>0.303590</td>
      <td>0.137955</td>
      <td>71</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>0.308470</td>
      <td>0.063184</td>
      <td>47</td>
    </tr>
  </tbody>
</table>
</div>




```python
third_trial_w_sharpe_ratio = get_sharpe_ratio_df(third_trial)
```


```python
best_sub_cluster_transform, best_sub_cluster_sharpe_ratio = get_transform_df(third_trial_w_sharpe_ratio)
```


```python
cluster_perf(best_sub_cluster_transform, best_sub_cluster_sharpe_ratio)
```


![png](overall_return_variance_files/overall_return_variance_32_0.png)



```python
us_yield_curve_5years_dict = {"year": [2012, 2013, 2014, 2015, 2016, 2017],
                         "risk_free_rate": [0.89, 0.76, 1.72, 1.61, 1.73, 1.94]}
us_yield_curve_5years_df = pd.DataFrame.from_dict(us_yield_curve_5years_dict)
```


```python
avg_risk_free_rate = (
    us_yield_curve_5years_df
    .mean()
    [['risk_free_rate']]
    [0]
)
```
