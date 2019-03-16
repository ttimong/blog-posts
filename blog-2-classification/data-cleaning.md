

```python
import sqlite3
from sqlite3 import Error
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 100)
pd.options.display.max_rows = 4000
pd.set_option('display.max_colwidth', -1)
```


```python
sqlite_file = 'database.sqlite'    # name of the sqlite database file
# table names
# country
# league
# match
# player
# player_attributes
# team
# team_attributes
```


```python
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
```


```python
country = pd.read_sql_query("select * from country", conn)
league = pd.read_sql_query("select * from league", conn)
match = pd.read_sql_query("select * from match", conn)
player = pd.read_sql_query("select * from player", conn)
player_attributes = pd.read_sql_query("select * from player_attributes", conn)
team_attributes = pd.read_sql_query("select * from team_attributes", conn)
team = pd.read_sql_query("select * from team", conn)
player_position = pd.read_csv('./players_position.csv')
```


```python
season_dict = {
    2007: {1: '2006/2007', 2: '2006/2007', 3: '2006/2007', 4: '2006/2007', 5: '2007/2008', 6: '2007/2008', 7: '2007/2008', 8: '2007/2008', 9: '2007/2008', 10: '2007/2008', 11: '2007/2008', 12: '2007/2008'},
    2008: {1: '2007/2008', 2: '2007/2008', 3: '2007/2008', 4: '2007/2008', 5: '2008/2009', 6: '2008/2009', 7: '2008/2009', 8: '2008/2009', 9: '2008/2009', 10: '2008/2009', 11: '2008/2009', 12: '2008/2009'},
    2009: {1: '2008/2009', 2: '2008/2009', 3: '2008/2009', 4: '2008/2009', 5: '2009/2010', 6: '2009/2010', 7: '2009/2010', 8: '2009/2010', 9: '2009/2010', 10: '2009/2010', 11: '2009/2010', 12: '2009/2010'},
    2010: {1: '2009/2010', 2: '2009/2010', 3: '2009/2010', 4: '2009/2010', 5: '2010/2011', 6: '2010/2011', 7: '2010/2011', 8: '2010/2011', 9: '2010/2011', 10: '2010/2011', 11: '2010/2011', 12: '2010/2011'},
    2011: {1: '2010/2011', 2: '2010/2011', 3: '2010/2011', 4: '2010/2011', 5: '2011/2012', 6: '2011/2012', 7: '2011/2012', 8: '2011/2012', 9: '2011/2012', 10: '2011/2012', 11: '2011/2012', 12: '2011/2012'},
    2012: {1: '2011/2012', 2: '2011/2012', 3: '2011/2012', 4: '2011/2012', 5: '2012/2013', 6: '2012/2013', 7: '2012/2013', 8: '2012/2013', 9: '2012/2013', 10: '2012/2013', 11: '2012/2013', 12: '2012/2013'},
    2013: {1: '2012/2013', 2: '2012/2013', 3: '2012/2013', 4: '2012/2013', 5: '2013/2014', 6: '2013/2014', 7: '2013/2014', 8: '2013/2014', 9: '2013/2014', 10: '2013/2014', 11: '2013/2014', 12: '2013/2014'},
    2014: {1: '2013/2014', 2: '2013/2014', 3: '2013/2014', 4: '2013/2014', 5: '2014/2015', 6: '2014/2015', 7: '2014/2015', 8: '2014/2015', 9: '2014/2015', 10: '2014/2015', 11: '2014/2015', 12: '2014/2015'},
    2015: {1: '2014/2015', 2: '2014/2015', 3: '2014/2015', 4: '2014/2015', 5: '2015/2016', 6: '2015/2016', 7: '2015/2016', 8: '2015/2016', 9: '2015/2016', 10: '2015/2016', 11: '2015/2016', 12: '2015/2016'},
    2016: {1: '2015/2016', 2: '2015/2016', 3: '2015/2016', 4: '2015/2016', 5: '2016/2017', 6: '2016/2017', 7: '2016/2017', 8: '2016/2017', 9: '2016/2017', 10: '2016/2017', 11: '2016/2017', 12: '2016/2017'}
}
```


```python
team_attributes_2 = (
    team_attributes
    .merge(team[["team_api_id", "team_long_name", "team_short_name"]], on="team_api_id", how="left")
    .merge(match[["country_id", "home_team_api_id"]], left_on="team_api_id", right_on="home_team_api_id", how="left")
    .merge(league[["country_id", "name"]], on="country_id", how="left")
    .rename(columns={"name": "league_name"})
    .drop(["home_team_api_id", "country_id", "id", "team_fifa_api_id"], axis=1)
    .query("league_name == 'England Premier League'")
    .drop_duplicates()
    .reset_index(drop=True)
    .pipe(lambda x: x.assign(year=pd.to_datetime(x.date).dt.year))
    .pipe(lambda x: x.assign(month=pd.to_datetime(x.date).dt.month))
)
team_attributes_2['season'] = [season_dict[year][month] for (year, month) in zip(team_attributes_2.year, team_attributes_2.month)]

team_attributes_2.drop(['date', 'year', 'month'], axis=1, inplace=True)
```


```python
team_attributes_2.head(2)
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
      <th>team_api_id</th>
      <th>buildUpPlaySpeed</th>
      <th>buildUpPlaySpeedClass</th>
      <th>buildUpPlayDribbling</th>
      <th>buildUpPlayDribblingClass</th>
      <th>buildUpPlayPassing</th>
      <th>buildUpPlayPassingClass</th>
      <th>buildUpPlayPositioningClass</th>
      <th>chanceCreationPassing</th>
      <th>chanceCreationPassingClass</th>
      <th>chanceCreationCrossing</th>
      <th>chanceCreationCrossingClass</th>
      <th>chanceCreationShooting</th>
      <th>chanceCreationShootingClass</th>
      <th>chanceCreationPositioningClass</th>
      <th>defencePressure</th>
      <th>defencePressureClass</th>
      <th>defenceAggression</th>
      <th>defenceAggressionClass</th>
      <th>defenceTeamWidth</th>
      <th>defenceTeamWidthClass</th>
      <th>defenceDefenderLineClass</th>
      <th>team_long_name</th>
      <th>team_short_name</th>
      <th>league_name</th>
      <th>season</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9825</td>
      <td>66</td>
      <td>Balanced</td>
      <td>NaN</td>
      <td>Little</td>
      <td>30</td>
      <td>Short</td>
      <td>Free Form</td>
      <td>30</td>
      <td>Safe</td>
      <td>45</td>
      <td>Normal</td>
      <td>35</td>
      <td>Normal</td>
      <td>Free Form</td>
      <td>30</td>
      <td>Deep</td>
      <td>40</td>
      <td>Press</td>
      <td>50</td>
      <td>Normal</td>
      <td>Cover</td>
      <td>Arsenal</td>
      <td>ARS</td>
      <td>England Premier League</td>
      <td>2009/2010</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9825</td>
      <td>75</td>
      <td>Fast</td>
      <td>NaN</td>
      <td>Little</td>
      <td>40</td>
      <td>Mixed</td>
      <td>Free Form</td>
      <td>40</td>
      <td>Normal</td>
      <td>45</td>
      <td>Normal</td>
      <td>65</td>
      <td>Normal</td>
      <td>Free Form</td>
      <td>50</td>
      <td>Medium</td>
      <td>40</td>
      <td>Press</td>
      <td>45</td>
      <td>Normal</td>
      <td>Cover</td>
      <td>Arsenal</td>
      <td>ARS</td>
      <td>England Premier League</td>
      <td>2010/2011</td>
    </tr>
  </tbody>
</table>
</div>




```python
player_attributes = (
    player_attributes
    .pipe(lambda x: x.assign(year=pd.to_datetime(x.date).dt.year))
    .pipe(lambda x: x.assign(month=pd.to_datetime(x.date).dt.month))
)
player_attributes['season'] = [season_dict[year][month] for (year, month) in zip(player_attributes.year, player_attributes.month)]
```


```python
player_attributes_2 = (
    player_attributes
    .merge(player, on=['player_api_id', 'player_fifa_api_id'], how='left')
    .pipe(lambda x: x.assign(age=pd.to_datetime(x.date).dt.year - pd.to_datetime(x.birthday).dt.year))
    .drop(['player_name', 'birthday', 'id_x', 'id_y', 'player_fifa_api_id'], axis=1)
)
```


```python
selected_columns = [col for col in player_attributes_2.columns if col not in ('id', 'player_fifa_api_id', 'player_api_id', 'date', 'preferred_foot', 'attacking_work_rate', 'defensive_work_rate', 'year', 'month', 'season')]
```


```python
player_attributes_2 = (
    player_attributes_2
    .groupby(["player_api_id", "season"])
    .agg(dict(zip(selected_columns, ["mean"]*len(selected_columns))))
    .reset_index()
)
```


```python
player_attributes_2.head(2)
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
      <th>player_api_id</th>
      <th>season</th>
      <th>overall_rating</th>
      <th>potential</th>
      <th>crossing</th>
      <th>finishing</th>
      <th>heading_accuracy</th>
      <th>short_passing</th>
      <th>volleys</th>
      <th>dribbling</th>
      <th>curve</th>
      <th>free_kick_accuracy</th>
      <th>long_passing</th>
      <th>ball_control</th>
      <th>acceleration</th>
      <th>sprint_speed</th>
      <th>agility</th>
      <th>reactions</th>
      <th>balance</th>
      <th>shot_power</th>
      <th>jumping</th>
      <th>stamina</th>
      <th>strength</th>
      <th>long_shots</th>
      <th>aggression</th>
      <th>interceptions</th>
      <th>positioning</th>
      <th>vision</th>
      <th>penalties</th>
      <th>marking</th>
      <th>standing_tackle</th>
      <th>sliding_tackle</th>
      <th>gk_diving</th>
      <th>gk_handling</th>
      <th>gk_kicking</th>
      <th>gk_positioning</th>
      <th>gk_reflexes</th>
      <th>height</th>
      <th>weight</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2625</td>
      <td>2006/2007</td>
      <td>63.0</td>
      <td>64.0</td>
      <td>48.0</td>
      <td>48.0</td>
      <td>47.0</td>
      <td>64.0</td>
      <td>38.0</td>
      <td>57.0</td>
      <td>50.0</td>
      <td>46.0</td>
      <td>67.0</td>
      <td>57.0</td>
      <td>67.0</td>
      <td>64.0</td>
      <td>59.0</td>
      <td>52.0</td>
      <td>49.0</td>
      <td>61.0</td>
      <td>56.0</td>
      <td>78.0</td>
      <td>56.0</td>
      <td>59.0</td>
      <td>72.0</td>
      <td>52.0</td>
      <td>55.0</td>
      <td>56.0</td>
      <td>46.0</td>
      <td>64.0</td>
      <td>66.0</td>
      <td>63.0</td>
      <td>14.0</td>
      <td>11.0</td>
      <td>67.0</td>
      <td>9.0</td>
      <td>10.0</td>
      <td>175.26</td>
      <td>154.0</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2625</td>
      <td>2007/2008</td>
      <td>63.0</td>
      <td>64.0</td>
      <td>48.0</td>
      <td>48.0</td>
      <td>47.0</td>
      <td>64.0</td>
      <td>38.0</td>
      <td>57.0</td>
      <td>50.0</td>
      <td>51.0</td>
      <td>67.0</td>
      <td>57.0</td>
      <td>67.0</td>
      <td>64.0</td>
      <td>59.0</td>
      <td>52.0</td>
      <td>49.0</td>
      <td>61.0</td>
      <td>56.0</td>
      <td>78.0</td>
      <td>56.0</td>
      <td>59.0</td>
      <td>72.0</td>
      <td>52.0</td>
      <td>55.0</td>
      <td>56.0</td>
      <td>46.0</td>
      <td>64.0</td>
      <td>66.0</td>
      <td>63.0</td>
      <td>14.0</td>
      <td>24.0</td>
      <td>67.0</td>
      <td>24.0</td>
      <td>24.0</td>
      <td>175.26</td>
      <td>154.0</td>
      <td>26.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
match_selected_columns=[
    'season', 'match_api_id', 'home_team_api_id', 'away_team_api_id',
    'home_player_X1', 'home_player_X2', 'home_player_X3', 'home_player_X4', 'home_player_X5', 'home_player_X6', 'home_player_X7', 'home_player_X8', 
    'home_player_X9', 'home_player_X10', 'home_player_X11',
    'away_player_X1', 'away_player_X2', 'away_player_X3', 'away_player_X4', 'away_player_X5', 'away_player_X6', 'away_player_X7', 'away_player_X8', 
    'away_player_X9', 'away_player_X10', 'away_player_X11',
    'home_player_Y1', 'home_player_Y2', 'home_player_Y3', 'home_player_Y4', 'home_player_Y5', 'home_player_Y6', 'home_player_Y7', 'home_player_Y8', 
    'home_player_Y9', 'home_player_Y10', 'home_player_Y11',
    'away_player_Y1', 'away_player_Y2', 'away_player_Y3', 'away_player_Y4', 'away_player_Y5', 'away_player_Y6', 'away_player_Y7', 'away_player_Y8', 
    'away_player_Y9', 'away_player_Y10', 'away_player_Y11',
    'home_player_1','home_player_2', 'home_player_3', 'home_player_4', 'home_player_5', 'home_player_6', 'home_player_7', 'home_player_8', 
    'home_player_9', 'home_player_10', 'home_player_11',
    'away_player_1', 'away_player_2', 'away_player_3', 'away_player_4', 'away_player_5', 'away_player_6', 'away_player_7', 'away_player_8', 
    'away_player_9', 'away_player_10', 'away_player_11'
]
```


```python
epl_matches = (
    match
    .query("country_id==1729")
    [match_selected_columns]
    .fillna(0)
)
```


```python
epl_matches.head(2)
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
      <th>season</th>
      <th>match_api_id</th>
      <th>home_team_api_id</th>
      <th>away_team_api_id</th>
      <th>home_player_X1</th>
      <th>home_player_X2</th>
      <th>home_player_X3</th>
      <th>home_player_X4</th>
      <th>home_player_X5</th>
      <th>home_player_X6</th>
      <th>home_player_X7</th>
      <th>home_player_X8</th>
      <th>home_player_X9</th>
      <th>home_player_X10</th>
      <th>home_player_X11</th>
      <th>away_player_X1</th>
      <th>away_player_X2</th>
      <th>away_player_X3</th>
      <th>away_player_X4</th>
      <th>away_player_X5</th>
      <th>away_player_X6</th>
      <th>away_player_X7</th>
      <th>away_player_X8</th>
      <th>away_player_X9</th>
      <th>away_player_X10</th>
      <th>away_player_X11</th>
      <th>home_player_Y1</th>
      <th>home_player_Y2</th>
      <th>home_player_Y3</th>
      <th>home_player_Y4</th>
      <th>home_player_Y5</th>
      <th>home_player_Y6</th>
      <th>home_player_Y7</th>
      <th>home_player_Y8</th>
      <th>home_player_Y9</th>
      <th>home_player_Y10</th>
      <th>home_player_Y11</th>
      <th>away_player_Y1</th>
      <th>away_player_Y2</th>
      <th>away_player_Y3</th>
      <th>away_player_Y4</th>
      <th>away_player_Y5</th>
      <th>away_player_Y6</th>
      <th>away_player_Y7</th>
      <th>away_player_Y8</th>
      <th>away_player_Y9</th>
      <th>away_player_Y10</th>
      <th>away_player_Y11</th>
      <th>home_player_1</th>
      <th>home_player_2</th>
      <th>home_player_3</th>
      <th>home_player_4</th>
      <th>home_player_5</th>
      <th>home_player_6</th>
      <th>home_player_7</th>
      <th>home_player_8</th>
      <th>home_player_9</th>
      <th>home_player_10</th>
      <th>home_player_11</th>
      <th>away_player_1</th>
      <th>away_player_2</th>
      <th>away_player_3</th>
      <th>away_player_4</th>
      <th>away_player_5</th>
      <th>away_player_6</th>
      <th>away_player_7</th>
      <th>away_player_8</th>
      <th>away_player_9</th>
      <th>away_player_10</th>
      <th>away_player_11</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1728</th>
      <td>2008/2009</td>
      <td>489042</td>
      <td>10260</td>
      <td>10261</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>11.0</td>
      <td>30726.0</td>
      <td>30362.0</td>
      <td>30620.0</td>
      <td>30865.0</td>
      <td>32569.0</td>
      <td>24148.0</td>
      <td>34944.0</td>
      <td>30373.0</td>
      <td>24154.0</td>
      <td>24157.0</td>
      <td>30829.0</td>
      <td>24224.0</td>
      <td>25518.0</td>
      <td>24228.0</td>
      <td>30929.0</td>
      <td>29581.0</td>
      <td>38807.0</td>
      <td>40565.0</td>
      <td>30360.0</td>
      <td>33852.0</td>
      <td>34574.0</td>
      <td>37799.0</td>
    </tr>
    <tr>
      <th>1729</th>
      <td>2008/2009</td>
      <td>489043</td>
      <td>9825</td>
      <td>8659</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>11.0</td>
      <td>23686.0</td>
      <td>26111.0</td>
      <td>38835.0</td>
      <td>30986.0</td>
      <td>31291.0</td>
      <td>31013.0</td>
      <td>30935.0</td>
      <td>39297.0</td>
      <td>26181.0</td>
      <td>30960.0</td>
      <td>36410.0</td>
      <td>36373.0</td>
      <td>36832.0</td>
      <td>23115.0</td>
      <td>37280.0</td>
      <td>24728.0</td>
      <td>24664.0</td>
      <td>31088.0</td>
      <td>23257.0</td>
      <td>24171.0</td>
      <td>25922.0</td>
      <td>27267.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
home_player_cols= ['home_player_1','home_player_2', 'home_player_3', 'home_player_4', 'home_player_5', 'home_player_6', 
                    'home_player_7', 'home_player_8', 'home_player_9', 'home_player_10', 'home_player_11']
away_player_cols = ['away_player_1', 'away_player_2', 'away_player_3', 'away_player_4', 'away_player_5', 'away_player_6', 
                    'away_player_7', 'away_player_8', 'away_player_9', 'away_player_10', 'away_player_11']
```


```python
def get_team(df, min_max='min', home_away_id='home_team_api_id'):
    final_df = (
        df
        [['season', '{}'.format(col), '{}'.format(home_away_id)]]
        .drop_duplicates()
        .groupby(["season", "{}".format(col)])
        .agg({"{}".format(home_away_id): "min"})
        .reset_index()
        .rename(columns={"{}".format(col): "player_api_id", "{}".format(home_away_id): "team_api_id"})
    )
    return final_df
```


```python
first = True
for col in home_player_cols:
    if first is True:
        first_df = get_team(epl_matches, min_max='min', home_away_id='home_team_api_id')
        second_df = get_team(epl_matches, min_max='max', home_away_id='home_team_api_id')
        home_final = pd.concat([first_team, second_team], axis=0)
        first = False
    else:
        first_team = get_team(epl_matches, min_max='min', home_away_id='home_team_api_id')
        second_team = get_team(epl_matches, min_max='max', home_away_id='home_team_api_id')
        home_intermediate = pd.concat([first_team, second_team], axis=0)
        home_final = pd.concat([home_intermediate, home_final], axis=0)
        
home_final = (
    home_final
    .drop_duplicates()
    .query("player_api_id != 0")
    .reset_index(drop=True)
)
```


```python
first = True
for col in away_player_cols:
    if first is True:
        first_df = get_team(epl_matches, min_max='min', home_away_id='away_team_api_id')
        second_df = get_team(epl_matches, min_max='max', home_away_id='away_team_api_id')
        away_final = pd.concat([first_team, second_team], axis=0)
        first = False
    else:
        first_team = get_team(epl_matches, min_max='min', home_away_id='away_team_api_id')
        second_team = get_team(epl_matches, min_max='max', home_away_id='away_team_api_id')
        away_intermediate = pd.concat([first_team, second_team], axis=0)
        away_final = pd.concat([away_intermediate, away_final], axis=0)
        
away_final = (
    away_final
    .drop_duplicates()
    .query("player_api_id != 0")
    .reset_index(drop=True)
)
```


```python
player_team = pd.concat([home_final, away_final], axis=0)
```


```python
player_team = (
    player_team
    .drop_duplicates()
    .reset_index(drop=True)
)
```


```python
player_team.query("player_api_id == 38836 and season == '2008/2009'")
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
      <th>season</th>
      <th>player_api_id</th>
      <th>team_api_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2287</th>
      <td>2008/2009</td>
      <td>38836.0</td>
      <td>8472</td>
    </tr>
    <tr>
      <th>3519</th>
      <td>2008/2009</td>
      <td>38836.0</td>
      <td>8586</td>
    </tr>
  </tbody>
</table>
</div>




```python
player_attributes_3 = (
    player_attributes_2
    .merge(player_team, on=['season', 'player_api_id'], how='left')
    .merge(team_attributes_2[['team_api_id', 'season', 'league_name']], on=['team_api_id', 'season'], how='left')
    .query("league_name == 'England Premier League'")
    [['league_name', 'player_api_id', 'season', 'team_api_id', 'age', 'height', 'weight', 'overall_rating', 'potential', 
      'crossing', 'finishing', 'heading_accuracy', 'short_passing', 'volleys', 'dribbling', 'curve', 'free_kick_accuracy', 'long_passing', 'ball_control',
      'acceleration', 'sprint_speed', 'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina', 'strength', 'long_shots', 'aggression', 
      'interceptions', 'positioning', 'vision', 'penalties', 'marking', 'standing_tackle', 'sliding_tackle', 
      'gk_diving','gk_handling', 'gk_kicking', 'gk_positioning', 'gk_reflexes']]
)
```


```python
player_attributes_3.head(2)
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
      <th>league_name</th>
      <th>player_api_id</th>
      <th>season</th>
      <th>team_api_id</th>
      <th>age</th>
      <th>height</th>
      <th>weight</th>
      <th>overall_rating</th>
      <th>potential</th>
      <th>crossing</th>
      <th>finishing</th>
      <th>heading_accuracy</th>
      <th>short_passing</th>
      <th>volleys</th>
      <th>dribbling</th>
      <th>curve</th>
      <th>free_kick_accuracy</th>
      <th>long_passing</th>
      <th>ball_control</th>
      <th>acceleration</th>
      <th>sprint_speed</th>
      <th>agility</th>
      <th>reactions</th>
      <th>balance</th>
      <th>shot_power</th>
      <th>jumping</th>
      <th>stamina</th>
      <th>strength</th>
      <th>long_shots</th>
      <th>aggression</th>
      <th>interceptions</th>
      <th>positioning</th>
      <th>vision</th>
      <th>penalties</th>
      <th>marking</th>
      <th>standing_tackle</th>
      <th>sliding_tackle</th>
      <th>gk_diving</th>
      <th>gk_handling</th>
      <th>gk_kicking</th>
      <th>gk_positioning</th>
      <th>gk_reflexes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>53</th>
      <td>England Premier League</td>
      <td>2802</td>
      <td>2013/2014</td>
      <td>10003</td>
      <td>28.571429</td>
      <td>172.72</td>
      <td>159.0</td>
      <td>76.0</td>
      <td>76.857143</td>
      <td>76.285714</td>
      <td>71.0</td>
      <td>53.0</td>
      <td>68.857143</td>
      <td>65.0</td>
      <td>85.0</td>
      <td>83.0</td>
      <td>77.0</td>
      <td>69.0</td>
      <td>81.0</td>
      <td>80.142857</td>
      <td>77.571429</td>
      <td>84.0</td>
      <td>69.0</td>
      <td>80.714286</td>
      <td>76.0</td>
      <td>67.0</td>
      <td>59.0</td>
      <td>51.0</td>
      <td>77.0</td>
      <td>54.0</td>
      <td>49.0</td>
      <td>73.0</td>
      <td>73.142857</td>
      <td>72.0</td>
      <td>42.0</td>
      <td>47.0</td>
      <td>36.0</td>
      <td>13.0</td>
      <td>16.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>183</th>
      <td>England Premier League</td>
      <td>3520</td>
      <td>2009/2010</td>
      <td>9825</td>
      <td>28.500000</td>
      <td>172.72</td>
      <td>154.0</td>
      <td>85.0</td>
      <td>90.500000</td>
      <td>85.000000</td>
      <td>88.0</td>
      <td>50.0</td>
      <td>90.000000</td>
      <td>77.0</td>
      <td>93.0</td>
      <td>77.0</td>
      <td>76.0</td>
      <td>80.0</td>
      <td>91.0</td>
      <td>88.000000</td>
      <td>87.000000</td>
      <td>86.0</td>
      <td>85.0</td>
      <td>75.000000</td>
      <td>84.0</td>
      <td>58.0</td>
      <td>76.0</td>
      <td>67.0</td>
      <td>85.0</td>
      <td>49.0</td>
      <td>75.0</td>
      <td>86.0</td>
      <td>85.000000</td>
      <td>88.0</td>
      <td>22.0</td>
      <td>29.0</td>
      <td>28.0</td>
      <td>7.0</td>
      <td>24.0</td>
      <td>80.0</td>
      <td>24.0</td>
      <td>24.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
player_position.columns
```




    Index(['playerID', 'CAM', 'CB', 'CDM', 'CF', 'CM', 'GK', 'LB', 'LF', 'LM',
           'LW', 'LWB', 'RB', 'RF', 'RM', 'RW', 'RWB', 'ST', 'SW'],
          dtype='object')




```python
player_position.query("playerID == 2802")
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
      <th>playerID</th>
      <th>CAM</th>
      <th>CB</th>
      <th>CDM</th>
      <th>CF</th>
      <th>CM</th>
      <th>GK</th>
      <th>LB</th>
      <th>LF</th>
      <th>LM</th>
      <th>LW</th>
      <th>LWB</th>
      <th>RB</th>
      <th>RF</th>
      <th>RM</th>
      <th>RW</th>
      <th>RWB</th>
      <th>ST</th>
      <th>SW</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
player.head(2)
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
      <th>id</th>
      <th>player_api_id</th>
      <th>player_name</th>
      <th>player_fifa_api_id</th>
      <th>birthday</th>
      <th>height</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>505942</td>
      <td>Aaron Appindangoye</td>
      <td>218353</td>
      <td>1992-02-29 00:00:00</td>
      <td>182.88</td>
      <td>187</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>155782</td>
      <td>Aaron Cresswell</td>
      <td>189615</td>
      <td>1989-12-15 00:00:00</td>
      <td>170.18</td>
      <td>146</td>
    </tr>
  </tbody>
</table>
</div>




```python
country_league = (
    league
    .merge(country, left_on='country_id', right_on='id', how='left')
    .rename(columns={"name_x": "league_name", "name_y": "country"})
    [["country_id", "country", "league_name"]]
)
```


```python
columns=[
    'id', 'country_id', 'country', 'league_name', 'season', 'stage', 'date', 'match_api_id', 'home_team_api_id', 'home_team_long_name', 'home_team_short_name', 
    'away_team_api_id', 'away_team_long_name', 'away_team_short_name', 'home_team_goal', 'away_team_goal',
    'home_player_X1', 'home_player_X2', 'home_player_X3', 'home_player_X4', 'home_player_X5', 'home_player_X6', 'home_player_X7', 'home_player_X8', 'home_player_X9', 'home_player_X10', 'home_player_X11',
    'away_player_X1', 'away_player_X2', 'away_player_X3', 'away_player_X4', 'away_player_X5', 'away_player_X6', 'away_player_X7', 'away_player_X8', 'away_player_X9', 'away_player_X10', 'away_player_X11',
    'home_player_Y1', 'home_player_Y2', 'home_player_Y3', 'home_player_Y4', 'home_player_Y5', 'home_player_Y6', 'home_player_Y7', 'home_player_Y8', 'home_player_Y9', 'home_player_Y10', 'home_player_Y11',
    'away_player_Y1', 'away_player_Y2', 'away_player_Y3', 'away_player_Y4', 'away_player_Y5', 'away_player_Y6', 'away_player_Y7', 'away_player_Y8', 'away_player_Y9', 'away_player_Y10', 'away_player_Y11',
    'home_player_1','home_player_2', 'home_player_3', 'home_player_4', 'home_player_5', 'home_player_6', 'home_player_7', 'home_player_8', 'home_player_9', 'home_player_10', 'home_player_11',
    'away_player_1', 'away_player_2', 'away_player_3', 'away_player_4', 'away_player_5', 'away_player_6', 'away_player_7', 'away_player_8', 'away_player_9', 'away_player_10', 'away_player_11',
]#'goal', 'shoton', 'shotoff', 'foulcommit', 'card', 'cross', 'corner', 'possession']
```


```python
match_country_league = (
    match
    .merge(country_league, on='country_id', how='left')
    .merge(team[["team_api_id", "team_long_name", "team_short_name"]], left_on="home_team_api_id", right_on="team_api_id", how="left")
    .rename(columns={"team_long_name": "home_team_long_name", "team_short_name": "home_team_short_name"})
    .drop("team_api_id", axis=1)
    .merge(team[["team_api_id", "team_long_name", "team_short_name"]], left_on="away_team_api_id", right_on="team_api_id", how="left")
    .rename(columns={"team_long_name": "away_team_long_name", "team_short_name": "away_team_short_name"})
    .drop("team_api_id", axis=1)
    [columns]
    .query("league_name == 'England Premier League'")
)
```


```python
match[match.home_player_1.notnull()]
```


```python
match_country_league.head()
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
      <th>id</th>
      <th>country_id</th>
      <th>country</th>
      <th>league_name</th>
      <th>season</th>
      <th>stage</th>
      <th>date</th>
      <th>match_api_id</th>
      <th>home_team_api_id</th>
      <th>home_team_long_name</th>
      <th>home_team_short_name</th>
      <th>away_team_api_id</th>
      <th>away_team_long_name</th>
      <th>away_team_short_name</th>
      <th>home_team_goal</th>
      <th>away_team_goal</th>
      <th>home_player_X1</th>
      <th>home_player_X2</th>
      <th>home_player_X3</th>
      <th>home_player_X4</th>
      <th>home_player_X5</th>
      <th>home_player_X6</th>
      <th>home_player_X7</th>
      <th>home_player_X8</th>
      <th>home_player_X9</th>
      <th>home_player_X10</th>
      <th>home_player_X11</th>
      <th>away_player_X1</th>
      <th>away_player_X2</th>
      <th>away_player_X3</th>
      <th>away_player_X4</th>
      <th>away_player_X5</th>
      <th>away_player_X6</th>
      <th>away_player_X7</th>
      <th>away_player_X8</th>
      <th>away_player_X9</th>
      <th>away_player_X10</th>
      <th>away_player_X11</th>
      <th>home_player_Y1</th>
      <th>home_player_Y2</th>
      <th>home_player_Y3</th>
      <th>home_player_Y4</th>
      <th>home_player_Y5</th>
      <th>home_player_Y6</th>
      <th>home_player_Y7</th>
      <th>home_player_Y8</th>
      <th>home_player_Y9</th>
      <th>home_player_Y10</th>
      <th>home_player_Y11</th>
      <th>away_player_Y1</th>
      <th>away_player_Y2</th>
      <th>away_player_Y3</th>
      <th>away_player_Y4</th>
      <th>away_player_Y5</th>
      <th>away_player_Y6</th>
      <th>away_player_Y7</th>
      <th>away_player_Y8</th>
      <th>away_player_Y9</th>
      <th>away_player_Y10</th>
      <th>away_player_Y11</th>
      <th>home_player_1</th>
      <th>home_player_2</th>
      <th>home_player_3</th>
      <th>home_player_4</th>
      <th>home_player_5</th>
      <th>home_player_6</th>
      <th>home_player_7</th>
      <th>home_player_8</th>
      <th>home_player_9</th>
      <th>home_player_10</th>
      <th>home_player_11</th>
      <th>away_player_1</th>
      <th>away_player_2</th>
      <th>away_player_3</th>
      <th>away_player_4</th>
      <th>away_player_5</th>
      <th>away_player_6</th>
      <th>away_player_7</th>
      <th>away_player_8</th>
      <th>away_player_9</th>
      <th>away_player_10</th>
      <th>away_player_11</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1728</th>
      <td>1729</td>
      <td>1729</td>
      <td>England</td>
      <td>England Premier League</td>
      <td>2008/2009</td>
      <td>1</td>
      <td>2008-08-17 00:00:00</td>
      <td>489042</td>
      <td>10260</td>
      <td>Manchester United</td>
      <td>MUN</td>
      <td>10261</td>
      <td>Newcastle United</td>
      <td>NEW</td>
      <td>1</td>
      <td>1</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>11.0</td>
      <td>30726.0</td>
      <td>30362.0</td>
      <td>30620.0</td>
      <td>30865.0</td>
      <td>32569.0</td>
      <td>24148.0</td>
      <td>34944.0</td>
      <td>30373.0</td>
      <td>24154.0</td>
      <td>24157.0</td>
      <td>30829.0</td>
      <td>24224.0</td>
      <td>25518.0</td>
      <td>24228.0</td>
      <td>30929.0</td>
      <td>29581.0</td>
      <td>38807.0</td>
      <td>40565.0</td>
      <td>30360.0</td>
      <td>33852.0</td>
      <td>34574.0</td>
      <td>37799.0</td>
    </tr>
    <tr>
      <th>1729</th>
      <td>1730</td>
      <td>1729</td>
      <td>England</td>
      <td>England Premier League</td>
      <td>2008/2009</td>
      <td>1</td>
      <td>2008-08-16 00:00:00</td>
      <td>489043</td>
      <td>9825</td>
      <td>Arsenal</td>
      <td>ARS</td>
      <td>8659</td>
      <td>West Bromwich Albion</td>
      <td>WBA</td>
      <td>1</td>
      <td>0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>11.0</td>
      <td>23686.0</td>
      <td>26111.0</td>
      <td>38835.0</td>
      <td>30986.0</td>
      <td>31291.0</td>
      <td>31013.0</td>
      <td>30935.0</td>
      <td>39297.0</td>
      <td>26181.0</td>
      <td>30960.0</td>
      <td>36410.0</td>
      <td>36373.0</td>
      <td>36832.0</td>
      <td>23115.0</td>
      <td>37280.0</td>
      <td>24728.0</td>
      <td>24664.0</td>
      <td>31088.0</td>
      <td>23257.0</td>
      <td>24171.0</td>
      <td>25922.0</td>
      <td>27267.0</td>
    </tr>
    <tr>
      <th>1730</th>
      <td>1731</td>
      <td>1729</td>
      <td>England</td>
      <td>England Premier League</td>
      <td>2008/2009</td>
      <td>1</td>
      <td>2008-08-16 00:00:00</td>
      <td>489044</td>
      <td>8472</td>
      <td>Sunderland</td>
      <td>SUN</td>
      <td>8650</td>
      <td>Liverpool</td>
      <td>LIV</td>
      <td>0</td>
      <td>1</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>32562.0</td>
      <td>38836.0</td>
      <td>24446.0</td>
      <td>24408.0</td>
      <td>36786.0</td>
      <td>38802.0</td>
      <td>24655.0</td>
      <td>17866.0</td>
      <td>30352.0</td>
      <td>23927.0</td>
      <td>24410.0</td>
      <td>30660.0</td>
      <td>37442.0</td>
      <td>30617.0</td>
      <td>24134.0</td>
      <td>414792.0</td>
      <td>37139.0</td>
      <td>30618.0</td>
      <td>40701.0</td>
      <td>24800.0</td>
      <td>24635.0</td>
      <td>30853.0</td>
    </tr>
    <tr>
      <th>1731</th>
      <td>1732</td>
      <td>1729</td>
      <td>England</td>
      <td>England Premier League</td>
      <td>2008/2009</td>
      <td>1</td>
      <td>2008-08-16 00:00:00</td>
      <td>489045</td>
      <td>8654</td>
      <td>West Ham United</td>
      <td>WHU</td>
      <td>8528</td>
      <td>Wigan Athletic</td>
      <td>WIG</td>
      <td>2</td>
      <td>1</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>36374.0</td>
      <td>30966.0</td>
      <td>23818.0</td>
      <td>37277.0</td>
      <td>30687.0</td>
      <td>36394.0</td>
      <td>37169.0</td>
      <td>24223.0</td>
      <td>24773.0</td>
      <td>34543.0</td>
      <td>23139.0</td>
      <td>34421.0</td>
      <td>34987.0</td>
      <td>35472.0</td>
      <td>111865.0</td>
      <td>25005.0</td>
      <td>35327.0</td>
      <td>25150.0</td>
      <td>97988.0</td>
      <td>41877.0</td>
      <td>127857.0</td>
      <td>34466.0</td>
    </tr>
    <tr>
      <th>1732</th>
      <td>1733</td>
      <td>1729</td>
      <td>England</td>
      <td>England Premier League</td>
      <td>2008/2009</td>
      <td>1</td>
      <td>2008-08-17 00:00:00</td>
      <td>489046</td>
      <td>10252</td>
      <td>Aston Villa</td>
      <td>AVL</td>
      <td>8456</td>
      <td>Manchester City</td>
      <td>MCI</td>
      <td>4</td>
      <td>2</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>11.0</td>
      <td>30380.0</td>
      <td>30357.0</td>
      <td>24658.0</td>
      <td>43280.0</td>
      <td>23282.0</td>
      <td>38609.0</td>
      <td>24780.0</td>
      <td>23782.0</td>
      <td>23354.0</td>
      <td>23264.0</td>
      <td>26165.0</td>
      <td>31432.0</td>
      <td>46403.0</td>
      <td>24208.0</td>
      <td>23939.0</td>
      <td>33963.0</td>
      <td>47413.0</td>
      <td>40198.0</td>
      <td>42119.0</td>
      <td>NaN</td>
      <td>33633.0</td>
      <td>107216.0</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
