from dotenv import dotenv_values
dotenv_values()
from sqlalchemy import create_engine


def get_database_conn():
    # Get database credentials from environment variable
    config = dict(dotenv_values('.env'))
    db_user_name = config.get('DB_USER_NAME')
    db_password = config.get('DB_PASSWORD')
    db_name = config.get('DB_NAME')
    port = config.get('PORT')
    host = config.get('HOST')
    # Create and return a postgresql database connection object
    return create_engine(f'postgresql+psycopg2://{db_user_name}:{db_password}@{host}:{port}/{db_name}')
con = get_database_conn