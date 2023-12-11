import csv
import logging

import sqlalchemy as sa

from pydantic import ValidationError
from sqlalchemy.dialects import postgresql

import models


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


def insert_data_idempotent(table, insertion_data):
    converted_data = [obj.model_dump() for obj in insertion_data]
    with engine.connect() as connection:
        stmt = postgresql.insert(table)\
            .values(converted_data)\
            .on_conflict_do_nothing()
        connection.execute(stmt)
        connection.commit()


def insert_aggregated_agreement_summary_idempotent():
    with engine.connect() as connection:
        loan_num = sa.select(
            models.Loan.client_id,
            sa.func.count(models.Loan.id).label("loan_num_total"),
            sa.func.count(models.Loan.id).filter(
                models.CloseLoan.closed_fl.is_(True)
            ).label("loan_num_closed")
        ).join(
            models.CloseLoan,
            models.CloseLoan.loan_id == models.Loan.id,
        ).group_by(
            models.Loan.client_id,
        ).cte("loan_num_cte")

        selection_stmt = sa.select(
            models.Agreement.id.label("agreement_id"),
            models.Agreement.target,
            models.Client.age,
            models.Client.gender,
            models.Client.child_total,
            models.Client.dependants,
            models.Client.socstatus_work_fl,
            models.Client.socstatus_pens_fl,
            models.Client.fl_presence_fl,
            models.Client.own_auto,
            models.Salary.personal_income,
            sa.func.coalesce(loan_num.c.loan_num_total, 0).label("loan_num_total"),
            sa.func.coalesce(loan_num.c.loan_num_closed, 0).label("loan_num_closed"),
        ).join(
            models.Client,
            models.Agreement.client_id == models.Client.id,
        ).join(
            models.Salary,
            models.Salary.client_id == models.Client.id,
        ).join(
            loan_num,
            loan_num.c.client_id == models.Client.id,
            isouter=True,
        )

        insertion_stmt = postgresql.insert(
            models.AgreementSummary
        ).from_select(
            ["agreement_id", "target", "age", "gender", "child_total", "dependants",
             "socstatus_work_fl", "socstatus_pens_fl", "fl_presence_fl", "own_auto",
             "personal_income", "loan_num_total", "loan_num_closed"],
            selection_stmt,
        ).on_conflict_do_nothing()
        connection.execute(insertion_stmt)
        connection.commit()
