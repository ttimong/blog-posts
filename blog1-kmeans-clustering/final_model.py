
# coding: utf-8



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime 
from dateutil.relativedelta import relativedelta

get_ipython().run_line_magic('matplotlib', 'inline')

pd.set_option('display.max_columns', 100)


# # Introduction
# I wanted to invest my money in the stock market, but there were too many stocks to choose from. I would like to segment the thousands of stocks that are available and filter out the group of better performing stocks. I shall attempt to use K-means clustering to solve this problem.
# 
# ### What is K-means clustering?
# K-means clustering is a type of unsupervised learning model. Unsupervised models are used to learn from a data set that is not labeled or classified. It identifies commonalities in the data set and react based on the presence or absence of such commonalities in each data point.
# 
# The objective of this model is to form clusters in the data set, with the number of clusters represented by the variable K. Data points are assigned to one of the K groups based on feature similarity.
# 
# ### How does K-means clustering works?
# 1. K number of cluster centroids are initialized randomly
# 2. Data points that are near to the cluster centroids are assigned to that cluster
# 3. The centroids will then move to the average point in the cluster and the data points will be re-assigned again
# 4. Step 1 and 2 will be repeated until there is no change in the clusters.

# # Data Transformation
# I have decided to use annual returns and variance as my variables as they informed users of the stock performance and its volatility. To narrow down my scope, I would be using stocks listed on NASDAQ and NYSE.



# 2006 - 2017 raw data is taken from Stocker python package which pulls from Quandl API
raw_data = pd.read_csv('./agg_df2_2012_onwards.csv', index_col=0)




raw_data.head()




# 2018 raw data is taken from yahoo-finance package
df_2018 = pd.read_csv('./2018_data.csv', index_col=0)




df_2018.head(3)




# narrowing dataset to 2012 - 2017
# creating new column `year`
df_2012_2017 = (
    raw_data
    .pipe(lambda x: x.assign(year=pd.to_datetime(x.date).dt.year))
    .query("year >= 2012")
    [['ticker', 'date', 'year', 'open', 'close']]
)


# `df_2012_2017` dataset provides the data for each stock performance on a daily basis, during the stated time period. I would like to obtain the annual performance of each stock to calculate the average annual return and variance.
# 
# ### For those who are unfamiliar, average yearly return can be calculated in 3 steps:
# 1. Calculate annual return of each year by subtracting the closing price of a stock on the last trading day in the year with the opening price of the same stock on the first trading day in the same year.
# 2. Divide the value in step 1 by the opening price of the stock on the first trading day in the same year. You would obtain the annual return for that year. Repeat step 1 and 2 for X number of years you have.
# 3. Sum up all the annual returns in the stated time period and divide the value by X number of years.
# 
# ### To calculate variance:
# 1. subtract each year's annual return with the average annual return and square that value. 
# 2. Sum all the values in step 1 and divide it by X years.
# 
# As such, I would need to transform my data set to based on the above parameters to obtain my desired variables. 



# getting the first day and last day of each year that is available in the dataset
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
    .rename(columns={"gains_pctg": "yearly_variance"})
)

agg_df3 = (
    agg_gains_df
    .merge(agg_var_df, on='ticker', how='inner')
)




agg_df3.head()




agg_df3.info()


# 1300 stocks will be used for this study.

# # Modelling
# 
# ### Evaluation
# Typically, two metrics are used to evaluate a K-means model. 
# 1. Sum of square errors (SSE) within clusters
# 2. Silhouette score.
# 
# SSE within clusters is derived by summing up the squared distance between each data point and its closest centroid. The goal is to reduce the error value. The intuition behind this is that we would want the distance of each data point to be as close as possible to the centroid. If the error is small, it would mean that the data points in the same cluster are relatively similar. As the number of centroids (clusters) increase, the error value will decrease. As such we would need to rely on the next metric to ensure that we are not introducing too many centroids (clusters) in the model.
# 
# Silhouette score is a measure of how similar the data point is to its own cluster compared to other clusters. The value ranges from -1 (worst score) to 1 (best score). A negative value would mean that data points are wrongly clustered while values near 0 would mean that there are overlapping clusters.



from sklearn.preprocessing import RobustScaler
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


# From the first graph, `Within Cluster SSE After K-Means Clustering`, we can see that as the number of clusters increase pass 7, the sum of square of errors within clusters plateaus off. From the second graph, `Silhouette Score After K-Means Clustering`, we can see that there are various parts of the graph where a kink can be seen. Since there is not much a difference in SSE after 7 clusters and that the drop in sihouette score is quite significant between 14 clusters and 15 clusters, I would use 14 clusters in my K-Means model below.



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




first_trial = apply_cluster(agg_df3, clusters=14)




cluster_perf_df = (
    first_trial
    .groupby('cluster')
    .agg({"avg_yearly_returns":"mean", "yearly_variance":"mean", "ticker":"count"})
    .sort_values('avg_yearly_returns')
    .reset_index()
)

cluster_perf_df


# From the dataframe above, we can see that the distribution of the stocks amongst the clusters is very skewed. Most of the stocks are aggregated in cluster `0`. For the other clusters, we can see that the `avg_yearly_returns` and `variance` are huge. A savvy investor would definitely not invest in these other clusters as the swing is too big, ranging from ~102% to 65100%. As such, he/she would most probably invest in a stock in cluster 0. As cluster 0 still contains too many stocks to choose from, I will attempt to conduct another K-Means clustering on cluster `0`.



# creating a dataframe that only consists of cluster `0`
agg_df3_sub = agg_df3.query("cluster == 0").reset_index(drop=True)




plot_cluster(agg_df3_sub, max_loop=25)


# From the second graph, `Silhouette Score After K-Means Clustering`, we can see that there was a steep drop in silhouette score between 5 clusters and 6 clusters. As such, I would use 5 clusters in my K-Means model below.



second_trial= apply_cluster(agg_df3_sub, clusters=5)




sub_cluster_perf_df = (
    second_trial
    .groupby('cluster')
    .agg({"avg_yearly_returns":"mean", "yearly_variance":"mean", "ticker":"count"})
    .sort_values('avg_yearly_returns')
    .reset_index()
)

sub_cluster_perf_df


# From the dataframe above, we can see that cluster `0` and cluster `2` would be the 2 better clusters to invest, amongst the rest. Cluster `0` yields a decent return of 8.1% with a 5.3% variance, while cluster `2` yields a much higher return of 20.7%, with a correspondingly higher variance of 11.6%. I decided to add in Sharpe Ratio as a metric to better evaluate the cluster performance.
# 
# ### What is Sharpe Ratio?
# Sharpe Ratio is used to help investors understand the return of an investment compared to its risk. The ratio is the average return earned in excess of the risk-free rate per unit of volatility or total risk. It is derived using annual returns, variance and risk-free rate. A Sharpe Ratio of more than 1 is considered good while a Sharpe Ratio of more than 2 is considered very good.
# 
# ### How to compute Sharpe Ratio?
# Sharpe Ratio can be computed as such:
# 
# **$Sharpe\ Ratio = (R_s - R_f) /{SD_s}$**
# 
# I will be using the first day of the year, 5-years daily U.S. yield rates, from https://home.treasury.gov/ as the risk-free rate.



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
        .pipe(lambda x: x.assign(std_dev=np.sqrt(x.yearly_variance)))
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
        [['yearly_variance', 'cluster']]
        .pipe(lambda x: x.assign(type='yearly_variance'))
        .rename(columns={"yearly_variance": "rate"})
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


# From the charts above, we can see that cluster `2` has the best Sharpe Ratio distribution amongst the rest and that its average returns (20.7%) and variance (11.6%) is still acceptable for my risk appetite. For someone who have a smaller risk appetite, he/she should be looking at cluster `0`, where the sharpe ratio is still fairly decent, along with moderate average returns (8.1%) and variance(5.3%)
# 
# Coupled with the fact that there are still more than 200 stocks in cluster `2` and there are some outliers (outperforming stocks) in that cluster, I would like to take segement it even further so that I can have a smaller group of stocks to research on.



(
    second_trial_w_sharpe_ratio
    .groupby("cluster")
    .agg({"avg_yearly_returns": "mean", "yearly_variance": "mean", "sharpe_ratio": "mean", "ticker": "count"})
    .reset_index()
)




# filtering out for cluster 1
best_sub_cluster = second_trial.query("cluster == 2")




plot_cluster(best_sub_cluster, max_loop=15)


# Based the above 2 graphs, I will use 6 clusters in my K-Means model below.



third_trial = apply_cluster(best_sub_cluster, clusters=6)




best_sub_cluster_perf = (    
    third_trial
    .groupby('cluster')
    .agg({"avg_yearly_returns":"mean", "yearly_variance":"mean", "ticker":"count"})
    .sort_values('avg_yearly_returns')
    .reset_index()
)
best_sub_cluster_perf




third_trial_w_sharpe_ratio = get_sharpe_ratio_df(third_trial)




best_sub_cluster_transform, best_sub_cluster_sharpe_ratio = get_transform_df(third_trial_w_sharpe_ratio)




cluster_perf(best_sub_cluster_transform, best_sub_cluster_sharpe_ratio)


# We can see that cluster `3` has the best sharpe ratio distribution and a very impressive average returns of 24.0% and variance of 5.0% (over the last 7 years). This golden cluster of 57 stocks definitely captured my attention and I should focused my research on them and create a portfolio based on them.



(
    third_trial_w_sharpe_ratio
    .groupby('cluster')
    .agg({"avg_yearly_returns": "mean", "yearly_variance": "mean", "sharpe_ratio": "mean", "ticker": "count"})
    .reset_index()
)




third_trial.query("cluster == 3").ticker.unique()


# # Conclusion
# In the first iteration of K-Means clustering, 14 clusters were formed. 13 of those clusters had extremely high returns and variance, stocks where no savvy investors would have purchased. As such, I have decided to conduct a second iteration on the remaining cluster, cluster `0`, that contains a majority of the stocks (1193 out of 1300 stocks). 
# 
# In the second iteration of K-Means clustering of the sub-cluster, 5 clusters were formed. As the performance of the clusters were fairly close, I have introduced a new metric, Sharpe Ratio, to better evaluate the performance of each cluster. From the Sharpe Ratio boxplot, it can be seen that cluster `2` was the better performing cluster as its Sharpe Ratio distribution was on the higher end. Since cluster `2` compromised of 257 stocks (still a fairly large number of stocks to study) and that there are some outliers in the Sharpe Ratio, I would like to take a more in-depth look into it, to see whether can I further narrow down to form a golden cluster.
# 
# In my third iteration of K-Means clustering of the sub-sub-cluster, 6 clusters were formed. From this last iteration, we can see a clear winner. Cluster `3` has the best Sharp Ratio distribution and that it has an impressive average returns of 24.0% and a variance of 5.0%, over the last 7 years. I should focus my research on this cluster (57 stocks) and choose the best stocks to invest in, based on fundamental analysis.

# # Limitations and Assumptions
# 1. The time period where there was a financial crisis (2007 and 2008) were not taken into account.
# 2. The volatility of each stocks within a year was not taken into account as well. The golden cluster's annual return could have a low variance of 5% in the 7 years period, but there could be huge movement in the stocks within a year.
