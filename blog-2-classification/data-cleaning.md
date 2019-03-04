

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
league
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
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>Belgium Jupiler League</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1729</td>
      <td>1729</td>
      <td>England Premier League</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4769</td>
      <td>4769</td>
      <td>France Ligue 1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7809</td>
      <td>7809</td>
      <td>Germany 1. Bundesliga</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10257</td>
      <td>10257</td>
      <td>Italy Serie A</td>
    </tr>
    <tr>
      <th>5</th>
      <td>13274</td>
      <td>13274</td>
      <td>Netherlands Eredivisie</td>
    </tr>
    <tr>
      <th>6</th>
      <td>15722</td>
      <td>15722</td>
      <td>Poland Ekstraklasa</td>
    </tr>
    <tr>
      <th>7</th>
      <td>17642</td>
      <td>17642</td>
      <td>Portugal Liga ZON Sagres</td>
    </tr>
    <tr>
      <th>8</th>
      <td>19694</td>
      <td>19694</td>
      <td>Scotland Premier League</td>
    </tr>
    <tr>
      <th>9</th>
      <td>21518</td>
      <td>21518</td>
      <td>Spain LIGA BBVA</td>
    </tr>
    <tr>
      <th>10</th>
      <td>24558</td>
      <td>24558</td>
      <td>Switzerland Super League</td>
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
first = True
for col in ['home_player_1','home_player_2', 'home_player_3', 'home_player_4', 'home_player_5', 'home_player_6', 'home_player_7', 'home_player_8', 'home_player_9', 'home_player_10', 'home_player_11']:
    if first is True:
        first_team = (
            epl_matches
            [['season', '{}'.format(col), 'home_team_api_id']]
            .drop_duplicates()
            .groupby(["season", "{}".format(col)])
            .agg({"home_team_api_id": "min"})
            .reset_index()
            .sort_values('home_team_api_id', ascending=False)
            .rename(columns={"{}".format(col): "player_id", "home_team_api_id": "team_api_id"})
        )

        second_team = (
            epl_matches
            [['season', '{}'.format(col), 'home_team_api_id']]
            .drop_duplicates()
            .groupby(["season", '{}'.format(col)])
            .agg({"home_team_api_id": "max"})
            .reset_index()
            .sort_values('home_team_api_id', ascending=False)
            .rename(columns={'{}'.format(col): "player_id", "home_team_api_id": "team_api_id"})
        )
        home_final = pd.concat([first_team, second_team], axis=0)
    else:
        first_team = (
            epl_matches
            [['season', '{}'.format(col), 'home_team_api_id']]
            .drop_duplicates()
            .groupby(["season", '{}'.format(col)])
            .agg({"home_team_api_id": "min"})
            .reset_index()
            .sort_values('home_team_api_id', ascending=False)
            .rename(columns={'{}'.format(col): "player_id", "home_team_api_id": "team_api_id"})
        )

        second_team = (
            epl_matches
            [['season', '{}'.format(col), 'home_team_api_id']]
            .drop_duplicates()
            .groupby(["season", '{}'.format(col)])
            .agg({"home_team_api_id": "max"})
            .reset_index()
            .sort_values('home_team_api_id', ascending=False)
            .rename(columns={'{}'.format(col): "player_id", "home_team_api_id": "team_api_id"})
        )
        home_intermediate = pd.concat([first_team, second_team], axis=0)
        home_final = pd.concat([home_intermediate, home_final], axis=0)

final.drop_duplicates(inplace=True)
```


```python
final.query("player_id == 46518 and season == '2009/2010'")
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
      <th>player_id</th>
      <th>home_team_api_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>70</th>
      <td>2009/2010</td>
      <td>46518.0</td>
      <td>8462</td>
    </tr>
    <tr>
      <th>70</th>
      <td>2009/2010</td>
      <td>46518.0</td>
      <td>10194</td>
    </tr>
  </tbody>
</table>
</div>




```python
match.query("season == '2009/2010' and home_player_1 == 46518")[['season', 'home_team_api_id', 'date']]
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
      <th>home_team_api_id</th>
      <th>date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2158</th>
      <td>2009/2010</td>
      <td>8462</td>
      <td>2009-11-28 00:00:00</td>
    </tr>
    <tr>
      <th>2168</th>
      <td>2009/2010</td>
      <td>8462</td>
      <td>2009-12-05 00:00:00</td>
    </tr>
    <tr>
      <th>2202</th>
      <td>2009/2010</td>
      <td>8462</td>
      <td>2009-12-19 00:00:00</td>
    </tr>
    <tr>
      <th>2231</th>
      <td>2009/2010</td>
      <td>8462</td>
      <td>2009-12-30 00:00:00</td>
    </tr>
    <tr>
      <th>2261</th>
      <td>2009/2010</td>
      <td>8462</td>
      <td>2010-01-26 00:00:00</td>
    </tr>
    <tr>
      <th>2411</th>
      <td>2009/2010</td>
      <td>10194</td>
      <td>2010-05-01 00:00:00</td>
    </tr>
    <tr>
      <th>2435</th>
      <td>2009/2010</td>
      <td>8462</td>
      <td>2009-08-30 00:00:00</td>
    </tr>
  </tbody>
</table>
</div>




```python
player.query("player_api_id == 46518")
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
      <th>1029</th>
      <td>1032</td>
      <td>46518</td>
      <td>Asmir Begovic</td>
      <td>172723</td>
      <td>1987-06-20 00:00:00</td>
      <td>200.66</td>
      <td>183</td>
    </tr>
  </tbody>
</table>
</div>




```python
team.query("team_api_id in (8462, 10194)")
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
      <th>team_api_id</th>
      <th>team_fifa_api_id</th>
      <th>team_long_name</th>
      <th>team_short_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>40</th>
      <td>3472</td>
      <td>10194</td>
      <td>1806.0</td>
      <td>Stoke City</td>
      <td>STK</td>
    </tr>
    <tr>
      <th>44</th>
      <td>3476</td>
      <td>8462</td>
      <td>1790.0</td>
      <td>Portsmouth</td>
      <td>POR</td>
    </tr>
  </tbody>
</table>
</div>




```python
epl_matches.query("home_player_1==23021 and season == '2009/2010'")
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
      <th>2125</th>
      <td>2009/2010</td>
      <td>658706</td>
      <td>8667</td>
      <td>8462</td>
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
      <td>23021.0</td>
      <td>40132.0</td>
      <td>24509.0</td>
      <td>26066.0</td>
      <td>23022.0</td>
      <td>32577.0</td>
      <td>34437.0</td>
      <td>23333.0</td>
      <td>23225.0</td>
      <td>39073.0</td>
      <td>37798.0</td>
      <td>36286.0</td>
      <td>24137.0</td>
      <td>47418.0</td>
      <td>26108.0</td>
      <td>23939.0</td>
      <td>25421.0</td>
      <td>40004.0</td>
      <td>23889.0</td>
      <td>27335.0</td>
      <td>38704.0</td>
      <td>30901.0</td>
    </tr>
    <tr>
      <th>2183</th>
      <td>2009/2010</td>
      <td>658824</td>
      <td>8667</td>
      <td>8655</td>
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
      <td>9.0</td>
      <td>11.0</td>
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
      <td>23021.0</td>
      <td>40132.0</td>
      <td>26066.0</td>
      <td>24509.0</td>
      <td>23022.0</td>
      <td>23438.0</td>
      <td>30595.0</td>
      <td>34437.0</td>
      <td>23225.0</td>
      <td>39073.0</td>
      <td>23034.0</td>
      <td>30622.0</td>
      <td>38836.0</td>
      <td>19020.0</td>
      <td>23921.0</td>
      <td>30739.0</td>
      <td>30842.0</td>
      <td>109621.0</td>
      <td>30849.0</td>
      <td>113465.0</td>
      <td>34947.0</td>
      <td>49825.0</td>
    </tr>
    <tr>
      <th>2213</th>
      <td>2009/2010</td>
      <td>658921</td>
      <td>8667</td>
      <td>10260</td>
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
      <td>23021.0</td>
      <td>32577.0</td>
      <td>24509.0</td>
      <td>26066.0</td>
      <td>23022.0</td>
      <td>23438.0</td>
      <td>30595.0</td>
      <td>23333.0</td>
      <td>23225.0</td>
      <td>70297.0</td>
      <td>23034.0</td>
      <td>35906.0</td>
      <td>38994.0</td>
      <td>30865.0</td>
      <td>30362.0</td>
      <td>32569.0</td>
      <td>35327.0</td>
      <td>34944.0</td>
      <td>24148.0</td>
      <td>24154.0</td>
      <td>27430.0</td>
      <td>30829.0</td>
    </tr>
    <tr>
      <th>2223</th>
      <td>2009/2010</td>
      <td>658588</td>
      <td>8667</td>
      <td>8586</td>
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
      <td>23021.0</td>
      <td>93458.0</td>
      <td>34275.0</td>
      <td>24509.0</td>
      <td>23022.0</td>
      <td>32577.0</td>
      <td>30595.0</td>
      <td>23333.0</td>
      <td>23225.0</td>
      <td>23563.0</td>
      <td>26143.0</td>
      <td>30455.0</td>
      <td>32870.0</td>
      <td>46403.0</td>
      <td>26209.0</td>
      <td>40006.0</td>
      <td>30895.0</td>
      <td>97988.0</td>
      <td>24656.0</td>
      <td>31097.0</td>
      <td>24635.0</td>
      <td>30348.0</td>
    </tr>
    <tr>
      <th>2242</th>
      <td>2009/2010</td>
      <td>658940</td>
      <td>8667</td>
      <td>8455</td>
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
      <td>23021.0</td>
      <td>40132.0</td>
      <td>24509.0</td>
      <td>93458.0</td>
      <td>23022.0</td>
      <td>23034.0</td>
      <td>30595.0</td>
      <td>182962.0</td>
      <td>23225.0</td>
      <td>70297.0</td>
      <td>37798.0</td>
      <td>30859.0</td>
      <td>31306.0</td>
      <td>30911.0</td>
      <td>30627.0</td>
      <td>40825.0</td>
      <td>30699.0</td>
      <td>30686.0</td>
      <td>30631.0</td>
      <td>30679.0</td>
      <td>30822.0</td>
      <td>37804.0</td>
    </tr>
    <tr>
      <th>2273</th>
      <td>2009/2010</td>
      <td>658971</td>
      <td>8667</td>
      <td>8602</td>
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
      <td>23021.0</td>
      <td>40132.0</td>
      <td>93458.0</td>
      <td>24509.0</td>
      <td>23022.0</td>
      <td>32577.0</td>
      <td>30595.0</td>
      <td>182962.0</td>
      <td>23225.0</td>
      <td>37798.0</td>
      <td>70297.0</td>
      <td>30669.0</td>
      <td>40022.0</td>
      <td>32581.0</td>
      <td>23334.0</td>
      <td>33138.0</td>
      <td>23099.0</td>
      <td>35466.0</td>
      <td>29673.0</td>
      <td>25415.0</td>
      <td>23538.0</td>
      <td>23291.0</td>
    </tr>
    <tr>
      <th>2285</th>
      <td>2009/2010</td>
      <td>659065</td>
      <td>8667</td>
      <td>8456</td>
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
      <td>23021.0</td>
      <td>40132.0</td>
      <td>24509.0</td>
      <td>93458.0</td>
      <td>23022.0</td>
      <td>23034.0</td>
      <td>30595.0</td>
      <td>182962.0</td>
      <td>23225.0</td>
      <td>70297.0</td>
      <td>37798.0</td>
      <td>24224.0</td>
      <td>30509.0</td>
      <td>30831.0</td>
      <td>191616.0</td>
      <td>30635.0</td>
      <td>24213.0</td>
      <td>30598.0</td>
      <td>23782.0</td>
      <td>33781.0</td>
      <td>38817.0</td>
      <td>30960.0</td>
    </tr>
    <tr>
      <th>2335</th>
      <td>2009/2010</td>
      <td>658600</td>
      <td>8667</td>
      <td>8559</td>
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
      <td>7.0</td>
      <td>11.0</td>
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
      <td>23021.0</td>
      <td>26066.0</td>
      <td>34275.0</td>
      <td>24509.0</td>
      <td>23022.0</td>
      <td>97489.0</td>
      <td>23333.0</td>
      <td>39073.0</td>
      <td>38816.0</td>
      <td>23225.0</td>
      <td>23563.0</td>
      <td>23932.0</td>
      <td>34430.0</td>
      <td>23783.0</td>
      <td>40128.0</td>
      <td>24728.0</td>
      <td>23934.0</td>
      <td>155384.0</td>
      <td>35532.0</td>
      <td>24653.0</td>
      <td>24372.0</td>
      <td>34261.0</td>
    </tr>
    <tr>
      <th>2343</th>
      <td>2009/2010</td>
      <td>659113</td>
      <td>8667</td>
      <td>9825</td>
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
      <td>23021.0</td>
      <td>32577.0</td>
      <td>26066.0</td>
      <td>93458.0</td>
      <td>23022.0</td>
      <td>23034.0</td>
      <td>30595.0</td>
      <td>24843.0</td>
      <td>34437.0</td>
      <td>37798.0</td>
      <td>70297.0</td>
      <td>23686.0</td>
      <td>26111.0</td>
      <td>34418.0</td>
      <td>26005.0</td>
      <td>31291.0</td>
      <td>30935.0</td>
      <td>39297.0</td>
      <td>27277.0</td>
      <td>26181.0</td>
      <td>36410.0</td>
      <td>3520.0</td>
    </tr>
    <tr>
      <th>2364</th>
      <td>2009/2010</td>
      <td>659135</td>
      <td>8667</td>
      <td>9879</td>
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
      <td>23021.0</td>
      <td>40132.0</td>
      <td>93458.0</td>
      <td>23284.0</td>
      <td>38816.0</td>
      <td>23438.0</td>
      <td>30595.0</td>
      <td>24843.0</td>
      <td>34437.0</td>
      <td>23034.0</td>
      <td>70297.0</td>
      <td>30633.0</td>
      <td>23282.0</td>
      <td>26777.0</td>
      <td>43247.0</td>
      <td>24781.0</td>
      <td>25015.0</td>
      <td>165823.0</td>
      <td>112035.0</td>
      <td>24020.0</td>
      <td>24737.0</td>
      <td>30956.0</td>
    </tr>
    <tr>
      <th>2384</th>
      <td>2009/2010</td>
      <td>659155</td>
      <td>8667</td>
      <td>8191</td>
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
      <td>23021.0</td>
      <td>40132.0</td>
      <td>23284.0</td>
      <td>93458.0</td>
      <td>23022.0</td>
      <td>32577.0</td>
      <td>30595.0</td>
      <td>24843.0</td>
      <td>38816.0</td>
      <td>23034.0</td>
      <td>70297.0</td>
      <td>24788.0</td>
      <td>34230.0</td>
      <td>43252.0</td>
      <td>34214.0</td>
      <td>23823.0</td>
      <td>23370.0</td>
      <td>23185.0</td>
      <td>46008.0</td>
      <td>11496.0</td>
      <td>23190.0</td>
      <td>32627.0</td>
    </tr>
    <tr>
      <th>2455</th>
      <td>2009/2010</td>
      <td>658630</td>
      <td>8667</td>
      <td>8658</td>
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
      <td>23021.0</td>
      <td>40132.0</td>
      <td>26066.0</td>
      <td>23284.0</td>
      <td>23022.0</td>
      <td>39073.0</td>
      <td>23333.0</td>
      <td>34437.0</td>
      <td>23225.0</td>
      <td>37798.0</td>
      <td>70297.0</td>
      <td>31432.0</td>
      <td>24226.0</td>
      <td>34193.0</td>
      <td>23837.0</td>
      <td>24190.0</td>
      <td>77704.0</td>
      <td>24978.0</td>
      <td>24655.0</td>
      <td>33049.0</td>
      <td>36802.0</td>
      <td>31073.0</td>
    </tr>
    <tr>
      <th>2475</th>
      <td>2009/2010</td>
      <td>658686</td>
      <td>8667</td>
      <td>8528</td>
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
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>7.0</td>
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
      <td>7.0</td>
      <td>11.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>6.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>11.0</td>
      <td>23021.0</td>
      <td>40132.0</td>
      <td>23284.0</td>
      <td>38816.0</td>
      <td>23022.0</td>
      <td>26066.0</td>
      <td>23025.0</td>
      <td>34437.0</td>
      <td>39073.0</td>
      <td>23225.0</td>
      <td>37798.0</td>
      <td>34421.0</td>
      <td>34987.0</td>
      <td>35472.0</td>
      <td>24230.0</td>
      <td>111865.0</td>
      <td>40015.0</td>
      <td>129817.0</td>
      <td>29581.0</td>
      <td>25005.0</td>
      <td>71550.0</td>
      <td>30953.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
season_dict = {}
for s in epl_matches.season.sort_values().unique():
    season_dict[s] = {}
    df = (
        epl_matches
        .query("season == '{}'".format(s))
        [['home_player_1','home_player_2', 'home_player_3', 'home_player_4', 'home_player_5', 'home_player_6', 
          'home_player_7', 'home_player_8', 'home_player_9', 'home_player_10', 'home_player_11']]
    )
    
    for col in 
    for team_id in df.home_team_api_id.sort_values().unique():
        
        
        
        player_id_list = []
        home_df = (
            df
            .query("home_team_api_id == {}".format(team_id))
            [['home_player_1','home_player_2', 'home_player_3', 'home_player_4', 'home_player_5', 'home_player_6', 
              'home_player_7', 'home_player_8', 'home_player_9', 'home_player_10', 'home_player_11']]
        )
        for col in home_df.columns:
            for player_id in home_df[col]:
                player_id_list.append(int(player_id))
    
        away_df = (
            df
            .query("away_team_api_id == {}".format(team_id))
            [['away_player_1', 'away_player_2', 'away_player_3', 'away_player_4', 'away_player_5', 'away_player_6', 
              'away_player_7', 'away_player_8', 'away_player_9', 'away_player_10', 'away_player_11']]
        )
        for col in away_df.columns:
            for player_id in away_df[col]:
                player_id_list.append(int(player_id))
        player_id_list = list(set(player_id_list))
        season_dict[s][team_id] = player_id_list
```


```python
season_dict = {}
for s in epl_matches.season.sort_values().unique():
    season_dict[s] = {}
    df = epl_matches.query("season == '{}'".format(s))
    for team_id in df.home_team_api_id.sort_values().unique():
        player_id_list = []
        home_df = (
            df
            .query("home_team_api_id == {}".format(team_id))
            [['home_player_1','home_player_2', 'home_player_3', 'home_player_4', 'home_player_5', 'home_player_6', 
              'home_player_7', 'home_player_8', 'home_player_9', 'home_player_10', 'home_player_11']]
        )
        for col in home_df.columns:
            for player_id in home_df[col]:
                player_id_list.append(int(player_id))
    
        away_df = (
            df
            .query("away_team_api_id == {}".format(team_id))
            [['away_player_1', 'away_player_2', 'away_player_3', 'away_player_4', 'away_player_5', 'away_player_6', 
              'away_player_7', 'away_player_8', 'away_player_9', 'away_player_10', 'away_player_11']]
        )
        for col in away_df.columns:
            for player_id in away_df[col]:
                player_id_list.append(int(player_id))
        player_id_list = list(set(player_id_list))
        season_dict[s][team_id] = player_id_list
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

```


```python

```


```python

```


```python

```


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
