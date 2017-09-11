#### Data Available From football-data.org

The football data service provides several data sets through the API
endpoint http://www.football-data.org. Data can be collected through
this API from three perspectives
* Fixtures & Results
* Team Data
* League Standings

Once collected, data will be stored locally in postgres. The default
postgres database is **football**.

##### Football Data Dictionary

Most data will be constructed by making successive calls to the API.
The schema for most data is **football**.

**football_data.epl_league_standings**

match_day | team_id | position | season_id
--- | --- | --- | ---

**football_data.epl_teams**

team_id | full_team_name
--- | ---


**football_data.epl_fixture_results**

View of all fixtures and results from the EPL.

fixture_date | match_day | season_id | home_team_id | away_team_id | home_score | away_score | total_goals
----|----|---|----|----|---- | ---- | ----
Timestamp of match  | Match day number | Season ID e.g 1516 for 2015-16 season| Unique ID of home team | Unique ID of away team | Score home | Score away | Total goals scored

