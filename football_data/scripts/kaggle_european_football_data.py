import pandas as pd

from football_data.constants import KAGGLE_POSTGRES_SCHEMA, KAGGLE_SQLITE_DB_PATH
from football_data.db_engines import connect_sqlite, connect_postgres

import logging


def update():
    sqlite = connect_sqlite(KAGGLE_SQLITE_DB_PATH)
    tables = pd.read_sql('select * from sqlite_sequence;', sqlite)

    postgres = connect_postgres('football')
    schema = KAGGLE_POSTGRES_SCHEMA

    logging.debug('importing into postgres the following tables: %s' % tables)

    table_mapping = dict()
    for t in tables['name'].tolist():
        table_mapping[t] = t.lower()
    logging.debug('mapping table names according to %s' % table_mapping)

    for source_table in table_mapping.keys():
        destination_table = table_mapping[source_table]
        copy_to_postgres(sqlite, source_table, postgres, destination_table, schema)


def copy_to_postgres(source_con, source_table, destination_con, destination_table, destination_schema=None):
    logging.debug('reading from %s' % source_table)
    df = pd.read_sql('select * from %s;' % source_table, source_con)
    logging.debug('writing %s to %s with schema = %s' % (str(df.head()), destination_table, destination_schema))
    df.to_sql(destination_table, destination_con, index=False, schema=destination_schema)
    return df


if __name__ == '__main__':
    update()
