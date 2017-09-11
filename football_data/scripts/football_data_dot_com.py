import os
import pandas as pd
import pandas.errors
import pandas.io.sql
from football_data.constants import PROJECT_ROOT
from football_data.db_engines import connect_postgres


league_index = {'epl': 0,
                'efc': 1,
                'el1': 2,
                'el2': 3,
                'conf': 4}


def download_english_league_stats_and_odds(season_code='1718', league='epl'):
    league, season_code = str(league), str(season_code)
    data_path = os.path.join(PROJECT_ROOT, 'data', 'stats_and_odds_%s_%s.csv' % (season_code, league))
    url = 'http://www.football-data.co.uk/mmz4281/%s/E%s.csv' % (season_code, league_index[league])
    print(url)
    data = pd.DataFrame()
    try:
        data = pd.read_csv(url, error_bad_lines=False)
    except pandas.errors.ParserError:
        pass
    print(data.head())
    data.to_csv(data_path, index=False)


def next_season(season_code):
    first = season_code[2:]
    second = str(int(first) + 1).zfill(2) if int(first) < 99 else '00'
    return first + second


if __name__ == '__main__':
    # postgres connection
    con = connect_postgres('football')
    offline = True
    season = '9495'
    current_season = '1718'
    if not offline:
        while season != current_season:
            print(season)
            download_english_league_stats_and_odds(season)
            season = next_season(season)

    season = '9596'
    full_data = None
    while season != current_season:
        file_name = 'stats_and_odds_%s_%s' % (season, 'PL')
        path = os.path.join(PROJECT_ROOT, 'data', 'epl_' + file_name + '.csv')
        print(season)
        season = next_season(season)
        df = pd.read_csv(path)
        print(df)
        table_name = file_name.lower().replace('PL', 'epl')
        pandas.io.sql.execute('drop table if exists football_data_api.%s' % table_name, con)
        table_name = table_name.replace('pl', 'epl')
        full_data = df if full_data is None else full_data.append(df, ignore_index=True)
        df.to_sql(table_name, con, schema='football_data_api', if_exists='replace')

    print(full_data)
    full_data.to_sql('epl_stats_and_odds', con, schema='football_data_api', if_exists='replace', index=False)
