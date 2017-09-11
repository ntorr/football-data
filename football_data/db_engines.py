from sqlalchemy.engine import create_engine
from football_data.constants import POSTGRES_DB, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_USER, POSTGRES_PWD

import logging


def connect_postgres(db=None):
    db = POSTGRES_DB if db is None else db
    logging.debug('connecting to postgres database with connection parameters %s@%s:%s/%s' % (
        POSTGRES_USER, POSTGRES_HOST, POSTGRES_PORT, db))
    return create_engine(
        'postgresql+psycopg2://%s:%s@%s:%s/%s' % (POSTGRES_USER, POSTGRES_PWD, POSTGRES_HOST, POSTGRES_PORT, db))


def connect_sqlite(db_path):
    logging.debug('connecting to sqlite database file %s' % db_path)
    return create_engine('sqlite+pysqlite:///%s' % db_path)
