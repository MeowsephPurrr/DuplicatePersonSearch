import os
from http.client import HTTPException
from typing import Iterator

import psycopg2

class DB:
    BATCH_SIZE: int = 1000

    connection: psycopg2.extensions.connection = None

    def __init__(self):
        self._create_db_connection()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.connection.close()

    def _create_db_connection(self) -> psycopg2.connect:
        connection = None
        try:
            DB_HOST = os.environ.get("POSTGRES_HOST", "db")
            DB_NAME = os.environ.get("POSTGRES_DB", "mydb")
            DB_USER = os.environ.get("POSTGRES_USER", "user")
            DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "password")

            connection = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )

            self.connection = connection
        except Exception:
            if connection:
                connection.close()
            raise HTTPException(status_code=503, detail="Service Unavailable: Cannot connect to database.")

    def _build_query(self, table: str, fields: list[str]) -> str:
        return f"""
            SELECT {', '.join(fields)} FROM {table}
        """

    def get_records_in_batches(self, table: str, fields: list[str]) -> Iterator[dict[str, any]]:
        cursor = self.connection.cursor()

        query = self._build_query(table, fields)
        cursor.execute(query)
        while True:
            batch = cursor.fetchmany(2)

            if not batch:
                break

            yield from batch