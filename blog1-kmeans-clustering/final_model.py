
# coding: utf-8



import pandas as pd
import numpy as np
import datetime 
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')

pd.set_option('display.max_columns', 100)


# # Introduction



# 2006 - 2017 raw data is taken from Stocker package which uses Quandl API
raw_data = pd.read_csv('./2012_2017_data.csv', index_col=0)




raw_data.head(3)




# 2018 raw data is taken from yahoo-finance package
df_2018 = pd.read_csv('./2018_data.csv', index_col=0)




df_2018.head(3)




# narrowing data set to 2012 - 2017
# creating new column `year`
df_2012_2017 = (
    raw_data
    .pipe(lambda x: x.assign(year=pd.to_datetime(x.date).dt.year))
    .query("year >= 2012")
    [['ticker', 'date', 'year', 'open', 'close']]
)




# getting the first day and last day of each year that is available in the data set
first_date_list = [df_2012_2017.query("year == '{}'".format(2012+i)).date.min() for i in range(6)]
last_date_list = [df_2012_2017.query("year == '{}'".format(2012+i)).date.max() for i in range(6)]
first_date_df =pd.DataFrame({"date": first_date_list}) 
last_date_df = pd.DataFrame({"date": last_date_list})




# filtering for the first day data in `df_2012_2017`
first_date_2012_2017_df = (
    df_2012_2017
    .merge(first_date_df, on='date', how='inner')
    .pipe(lambda x: x.assign(year=x.date.str[:4]))
    .rename(columns={"open": "open_first_day"})
    .reset_index(drop=True)
    [['ticker', 'year', 'open_first_day']]
    .pivot_table(values='open_first_day', columns='year', index='ticker', aggfunc='sum')
    .rename_axis(None, axis=1)
    .reset_index()
)

# filtering last day data in `df_2012_2017` 
last_date_2012_2017_df = (
    df_2012_2017
    .merge(last_date_df, on='date', how='inner')
    .pipe(lambda x: x.assign(year=x.date.str[:4]))
    .rename(columns={"close": "close_last_day"})
    .reset_index(drop=True)
    [['ticker', 'year', 'close_last_day']]
    .pivot_table(values='close_last_day', columns='year', index='ticker', aggfunc='sum')
    .rename_axis(None, axis=1)
    .reset_index()
)




# transforming 2018 data to be similar to the `first_date_2012_2017` and `last_date_2012_2017` dataframe
first_date_2018_df = (
    df_2018
    .query("date == '2018-01-03'")
    [['ticker', 'date', 'Open']]
    .pipe(lambda x: x.assign(year=pd.to_datetime(x.date).dt.year))
    .rename(columns={"Open": "open_first_day"})
    .reset_index(drop=True)
    [['ticker', 'year', 'open_first_day']]
    .pivot_table(values='open_first_day', columns='year', index='ticker', aggfunc='sum')
    .rename_axis(None, axis=1)
    .reset_index()
)

last_date_2018_df = (
    df_2018
    .query("date == '2018-12-29'")
    [['ticker', 'date', 'Close']]
    .pipe(lambda x: x.assign(year=pd.to_datetime(x.date).dt.year))
    .rename(columns={"Close": "close_last_day"})
    .reset_index(drop=True)
    [['ticker', 'year', 'close_last_day']]
    .pivot_table(values='close_last_day', columns='year', index='ticker', aggfunc='sum')
    .rename_axis(None, axis=1)
    .reset_index()
)




# merging 2012-2017 data with 2018 data
agg_first_date_df = (
    first_date_2012_2017_df
    .merge(first_date_2018_df, on='ticker', how='inner')
    .rename(columns=({2018: "2018"}))
    .melt(id_vars='ticker', value_vars=['2012', '2013', '2014', '2015', '2016', '2017', '2018'])
    .rename(columns={"variable": "year", "value": "open_first_day"})
)

agg_last_date_df = (
    last_date_2012_2017_df
    .merge(last_date_2018_df, on='ticker', how='inner')
    .rename(columns=({2018: "2018"}))
    .melt(id_vars='ticker', value_vars=['2012', '2013', '2014', '2015', '2016', '2017', '2018'])
    .rename(columns={"variable": "year", "value": "close_last_day"})
)




# calculating yearly return and then averaging them to get average yearly returns for each stock
agg_gains_df = (
    agg_first_date_df
    .merge(agg_last_date_df, on=['ticker', 'year'], how='inner')
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
    .merge(agg_last_date_df, on=['ticker', 'year'], how='inner')
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




agg_df3.head(3)




agg_df3.info()




from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler
from sklearn.cluster import KMeans
from sklearn import metrics




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




plot_cluster(agg_df3, max_loop=25)


# From the first graph, `Within Cluster SSE After K-Means Clustering`, we can see that as the number of clusters increase pass 7, the sum of square of errors within clusters plateaus off. From the second graph, `Silhouette Score After K-Means Clustering`, we can see that there are various parts of the graph where a kink can be seen. Since there is not much a difference in SSE after 7 clusters and that the drop in sihouette score is quite significant between 13 clusters and 14 clusters, I would use 13 clusters in my K-Means model below.



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




first_trial = apply_cluster(agg_df3, clusters=13)




cluster_perf_df = (
    first_trial
    .groupby('cluster')
    .agg({"avg_yearly_returns":"mean", "variance":"mean", "ticker":"count"})
    .sort_values('avg_yearly_returns')
    .reset_index()
)

cluster_perf_df


# From the dataframe above, we can see that the distribution of the stocks amongst the clusters is very skewed. Most of the stocks are aggregated in cluster `0`. For the other clusters, we can see that the `avg_yearly_returns` and `variance` are huge. A savvy investor would definitely not go for these other clusters as the variance is way too high, ranging from ~102% to 65100%. As such, he/she would most probably invest in a stock in cluster 0. As cluster 0 still contains too many stocks to choose from, I will attempt to conduct another K-Means clustering on cluster `0`.



agg_df3_sub = agg_df3.query("cluster == 0").reset_index(drop=True)




plot_cluster(agg_df3_sub, max_loop=25)


# From the second graph, `Silhouette Score After K-Means Clustering`, we can see that there was a steep drop in silhouette score between 5 clusters and 6 clusters. As such, I would use 5 clusters in my K-Means model below.



second_trial= apply_cluster(agg_df3_sub, clusters=5)




sub_cluster_perf_df = (
    second_trial
    .groupby('cluster')
    .agg({"avg_yearly_returns":"mean", "variance":"mean", "ticker":"count"})
    .sort_values('avg_yearly_returns')
    .reset_index()
)

sub_cluster_perf_df


# To better ascertain the performance of each cluster, I decided to add in Sharpe Ratio as a metric to better evaluate their performance. Using the first day of the year, 5-years daily U.S. yield rates, from https://home.treasury.gov/ as the risk-free rate, I have computed the Sharpe Ratio as such:
# 
# $Sharpe\ Ratio = (R_s - R_f) /{SD_s}$



# calculating the average risk free rate over the time period of 2012 - 2018 
us_yield_curve_5years_dict = {"year": [2012, 2013, 2014, 2015, 2016, 2017, 2018],
                         "risk_free_rate": [0.89, 0.76, 1.72, 1.61, 1.73, 1.94, 2.25]}
us_yield_curve_5years_df = pd.DataFrame.from_dict(us_yield_curve_5years_dict)

avg_risk_free_rate = (
    us_yield_curve_5years_df
    .mean()
    [['risk_free_rate']]
    [0]
)




def get_sharpe_ratio_df(df):
    """
    Computing Sharpe Ratio
    """
    df_w_sharpe_ratio = (
        df
        .pipe(lambda x: x.assign(avg_risk_free_rate=avg_risk_free_rate/100))
        .pipe(lambda x: x.assign(std_dev=np.sqrt(x.variance)))
        .pipe(lambda x: x.assign(sharpe_ratio=(x.avg_yearly_returns-x.avg_risk_free_rate)/x.std_dev))
    )

    return df_w_sharpe_ratio




second_trial_w_sharpe_ratio = get_sharpe_ratio_df(second_trial)




def get_transform_df(df_w_sharpe_ratio):
    """
    Transforming dataframe so that I can plot a boxplot of `Returns`, `Variance` and `Sharpe Ratio` for each cluster
    """
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




sub_cluster_transform, sub_cluster_sharpe_ratio = get_transform_df(second_trial_w_sharpe_ratio)




def cluster_perf(transform_df, sharpe_ratio_df):
    """
    Plotting boxplot of cluster performance
    """
    _  = plt.figure(figsize=(15,7))

    ax1 = plt.subplot(121)
    _ = sns.boxplot(x='cluster', y='rate', hue='type', data=transform_df)
    _ = plt.title("Distribution of Returns and Variance for each Cluster")

    ax2 = plt.subplot(122)
    _ =sns.boxplot(x='cluster', y='sharpe_ratio', data=sharpe_ratio_df, color='royalblue')
    _ = plt.title("Distribution of Sharpe Ratio for each Cluster")




cluster_perf(sub_cluster_transform, sub_cluster_sharpe_ratio)


# From the charts above, we can see that cluster `1` has the best sharpe ratio distribution amongst the rest and that their average returns (22.2%) and variance (12%) is still acceptable for my risk appetite. For someone who have a smaller risk appetite, he/she should be looking at cluster `0`, where the sharpe ratio is still fairly decent, along with moderate average returns (8.1%) and variance(5.6%)
# 
# As there are still more than 200 stocks in cluster `1` and there are some outliers (outperforming stocks) in that cluster, I would like to take segement it even further so that I can have a smaller group of stocks to research on.



best_sub_cluster = second_trial.query("cluster == 1")




plot_cluster(best_sub_cluster, max_loop=15)

I decided to conduct my K-Means clustering with 7 clusters


third_trial = apply_cluster(best_sub_cluster, clusters=7)




best_sub_cluster_perf = (    
    third_trial
    .groupby('cluster')
    .agg({"avg_yearly_returns":"mean", "variance":"mean", "ticker":"count"})
    .sort_values('avg_yearly_returns')
    .reset_index()
)
best_sub_cluster_perf




third_trial_w_sharpe_ratio = get_sharpe_ratio_df(third_trial)




best_sub_cluster_transform, best_sub_cluster_sharpe_ratio = get_transform_df(third_trial_w_sharpe_ratio)




cluster_perf(best_sub_cluster_transform, best_sub_cluster_sharpe_ratio)


# We can see that cluster `0` produces the best sharpe ratio and a very impressive average returns of 26% and variance of 5%. This group of 36 stocks definitely deserve my attention to conduct a proper equity research.

# # Conclusion
