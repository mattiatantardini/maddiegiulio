import os

POSTGRES_PWD = os.getenv("POSTGRES_PWD", "pwd")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_DBNAME = os.getenv("POSTGRES_DBNAME", "db")
