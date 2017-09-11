import os
import logging

# path constants
CONST_FILE_PATH = os.path.abspath(__file__)
PROJECT_ROOT = os.path.split(os.path.split(CONST_FILE_PATH)[0])[0]
USER_HOME = os.path.expanduser('~')


# for dealing with secrets
def get_secret_var(constant_name, file_name=None):
    """
    function that can be used to retrieve secret constants (e.g. passwords, api keys etc.) from environment variables
    or optionally from a file which should be created in the users home directory
    if parsing from a file, simply enter the secret as a single line in a hidden text file e.g.
    file name = ".secret-message", content = "MySecretPassword"
    :param constant_name: name of environment variable
    :param file_name: filename if reading secret from a file
    :return:
    """
    # try from environment
    val = str()
    try:
        val = os.environ[constant_name]
    except KeyError:
        if file_name is not None:
            if file_name[0] != '.':
                # if file is not hidden warn user
                logging.warning('file name %s contains a secret, make it a hidden file' % file_name)

            # try to read from file in user home
            try:
                val = open(os.path.join(USER_HOME, file_name), 'r').readline()
            except FileNotFoundError:
                pass

    if constant_name == str():
        logging.warning('Could not set constant %s, default value set to %s' % (constant_name, str(val)))
    return val


# soccer-date api key
SOCCER_API_HOST = "http://www.football-data.org"
SOCCER_CLI_API_TOKEN = get_secret_var('SOCCER_CLI_API_TOKEN', '.soccer-api-key')

# postgres connection details
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = 5432
POSTGRES_USER = 'fapp'
POSTGRES_DB = 'football'
POSTGRES_PWD = get_secret_var('POSTGRES_PWD', '.postgres-pwd')

# Kaggle European Football Database details
KAGGLE_SQLITE_DB_PATH = os.path.join(PROJECT_ROOT, 'data', 'kaggle-european-football-db.sqlite')
KAGGLE_POSTGRES_SCHEMA = 'kaggle_european_soccer'

