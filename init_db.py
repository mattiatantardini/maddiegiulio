import logging
import datetime

import pandas as pd
from tantaroba.log import configure_logging
from tantaroba.yaml import read_yaml
from psqlpandas.tables import initialize_table
from psqlpandas.postgresql import PostgresqlDatabaseConnector

from settings.config import (
    POSTGRES_DBNAME,
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_PWD,
    POSTGRES_USER,
)


if __name__ == "__main__":
    configure_logging()
    logging.info("Initializing database for maddi e giulio")

    db_connector = PostgresqlDatabaseConnector(
        dbname=POSTGRES_DBNAME,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USER,
        password=POSTGRES_PWD,
    )
    tables_info = read_yaml("data/tables_definition.yml")["tables"]
    names_info = tables_info[0]
    initial_data = pd.DataFrame(
        data={
            "uid": [0, 1],
            "name": ["maddi", "giulio"],
            "message": ["test", "test2"],
            "date_saved": [datetime.datetime.now(), datetime.datetime.now()],
        }
    )

    initialize_table(
        table_info=names_info, db_connector=db_connector, data=initial_data
    )
