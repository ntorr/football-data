import unittest
import pandas as pd
from football_data.constants import KAGGLE_DB_PATH
from football_data.db_engines import connect_postgres, connect_sqlite


class TestDataConnections(unittest.TestCase):
    def test_postgres_connection(self):
        """
        tests connection setup to postgres by creating a table test.test from a simple pandas data frame,
        reads it back and verifies the input and output data are the same
        :return: boolean, passed
        """
        con = connect_postgres()
        df_in = pd.DataFrame([1], columns=['test'], index=[0])
        df_in.to_sql('test', con, schema='test', if_exists='replace', index=False)
        df_out = pd.read_sql_table('test', con, schema='test', )

        return self.assertEqual(str(df_out), str(df_in))

    def test_sqlite_connection(self):
        """
        tests ability to read from static sqlite file
        :return: boolean, passed
        """
        sql = 'select * from Player limit 10;'
        con = connect_sqlite(KAGGLE_DB_PATH)
        df = pd.read_sql(sql, con)

        return self.assertTrue(len(df) == 10)
