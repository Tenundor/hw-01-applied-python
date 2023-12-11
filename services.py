import csv
import logging

import sqlalchemy as sa

from pydantic import ValidationError
from sqlalchemy.dialects import postgresql


engine = sa.create_engine(
    "postgresql+psycopg2://applied_python:applied_python@localhost/applied_python_hw_01"
)


def read_and_validate(csv_file_path, pydantic_model):
    valid_data = []
    with open(csv_file_path) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            try:
                valid_row = pydantic_model.model_validate(row)
                valid_data.append(valid_row)
            except ValidationError as exc:
                logging.warning(
                    f"Validation error in row {row},\n{exc}"
                )
    return valid_data


def idempotent_insert_data(table, insertion_data):
    converted_data = [obj.model_dump() for obj in insertion_data]
    with engine.connect() as connection:
        stmt = postgresql.insert(table)\
            .values(converted_data)\
            .on_conflict_do_nothing()
        connection.execute(stmt)
        connection.commit()
