
# coding: utf-8


import sqlite3
from sqlite3 import Error
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 100)
pd.options.display.max_rows = 4000
pd.set_option('display.max_colwidth', -1)



sqlite_file = 'database.sqlite'    # name of the sqlite database file
# table names
# country
# league
# match
# player
# player_attributes
# team
# team_attributes



conn = sqlite3.connect(sqlite_file)
c = conn.cursor()



country = pd.read_sql_query("select * from country", conn)
league = pd.read_sql_query("select * from league", conn)
match = pd.read_sql_query("select * from match", conn)
player = pd.read_sql_query("select * from player", conn)
player_attributes = pd.read_sql_query("select * from player_attributes", conn)
team_attributes = pd.read_sql_query("select * from team_attributes", conn)
team = pd.read_sql_query("select * from team", conn)
player_position = pd.read_csv('./players_position.csv')



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



team_attributes_2.head(2)



player_attributes = (
    player_attributes
    .pipe(lambda x: x.assign(year=pd.to_datetime(x.date).dt.year))
    .pipe(lambda x: x.assign(month=pd.to_datetime(x.date).dt.month))
)
player_attributes['season'] = [season_dict[year][month] for (year, month) in zip(player_attributes.year, player_attributes.month)]



player_attributes_2 = (
    player_attributes
    .merge(player, on=['player_api_id', 'player_fifa_api_id'], how='left')
    .pipe(lambda x: x.assign(age=pd.to_datetime(x.date).dt.year - pd.to_datetime(x.birthday).dt.year))
    .drop(['player_name', 'birthday', 'id_x', 'id_y', 'player_fifa_api_id'], axis=1)
)



selected_columns = [col for col in player_attributes_2.columns if col not in ('id', 'player_fifa_api_id', 'player_api_id', 'date', 'preferred_foot', 'attacking_work_rate', 'defensive_work_rate', 'year', 'month', 'season')]



player_attributes_2 = (
    player_attributes_2
    .groupby(["player_api_id", "season"])
    .agg(dict(zip(selected_columns, ["mean"]*len(selected_columns))))
    .reset_index()
)



player_attributes_2.head(2)



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



epl_matches = (
    match
    .query("country_id==1729")
    [match_selected_columns]
    .fillna(0)
)



epl_matches.head(2)



home_player_cols= ['home_player_1','home_player_2', 'home_player_3', 'home_player_4', 'home_player_5', 'home_player_6', 
                    'home_player_7', 'home_player_8', 'home_player_9', 'home_player_10', 'home_player_11']
away_player_cols = ['away_player_1', 'away_player_2', 'away_player_3', 'away_player_4', 'away_player_5', 'away_player_6', 
                    'away_player_7', 'away_player_8', 'away_player_9', 'away_player_10', 'away_player_11']



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



player_team = pd.concat([home_final, away_final], axis=0)



player_team = (
    player_team
    .drop_duplicates()
    .reset_index(drop=True)
)



player_team.query("player_api_id == 38836 and season == '2008/2009'")



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



player_attributes_3.head(2)



player_position.columns



player_position.query("playerID == 2802")



player.head(2)



country_league = (
    league
    .merge(country, left_on='country_id', right_on='id', how='left')
    .rename(columns={"name_x": "league_name", "name_y": "country"})
    [["country_id", "country", "league_name"]]
)



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



match[match.home_player_1.notnull()]



match_country_league.head()





