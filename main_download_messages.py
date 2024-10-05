from psqlpandas.postgresql import PostgresqlDatabaseConnector
from tantaroba.dates import today2str

from settings.config import (
    POSTGRES_DBNAME,
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_PWD,
    POSTGRES_USER,
)

if __name__ == "__main__":

    db_conn = PostgresqlDatabaseConnector(
        dbname=POSTGRES_DBNAME,
        host=POSTGRES_HOST,
        user=POSTGRES_USER,
        port=POSTGRES_PORT,
        password=POSTGRES_PWD,
    )
    messages = db_conn.read_df(
        "SELECT name, message FROM names_new WHERE message IS NOT NULL AND message != ''"
    )
    messages.to_excel(f"{today2str()}_maddiegiulio_messagi.xlsx", index=False)
