import logging

from models import (
    Agreement,
    Client,
    CloseLoan,
    Loan,
    Salary,
)
from services import insert_data_idempotent, read_and_validate
from schemas import (
    AgreementModel,
    ClientModel,
    CloseLoanModel,
    LoanModel,
    SalaryModel,
)


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    logging.info("The function for loading banking data from csv files into the "
                 "database has begun execution")
    filenames_with_models = (
        ("datasets/D_clients.csv", ClientModel, Client),
        ("datasets/D_target.csv", AgreementModel, Agreement),
        ("datasets/D_salary.csv", SalaryModel, Salary),
        ("datasets/D_loan.csv", LoanModel, Loan),
        ("datasets/D_close_loan.csv", CloseLoanModel, CloseLoan),
    )
    for filename, pydantic_model, table_model in filenames_with_models:
        logging.info(f"Reading from file '{filename}'")
        insertion_data = read_and_validate(filename, pydantic_model)
        logging.info(f"Inserting '{filename}' data to table '{table_model.__tablename__}'")
        insert_data_idempotent(table_model, insertion_data)
    logging.info("Job completed successfully")


if __name__ == "__main__":
    main()
