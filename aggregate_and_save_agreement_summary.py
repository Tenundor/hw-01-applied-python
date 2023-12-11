import logging

from services import insert_aggregated_agreement_summary_idempotent


if __name__ == "__main__":
    logging.info("The function for aggregate and save agreement summary has "
                 "begun execution")
    insert_aggregated_agreement_summary_idempotent()
    logging.info("Jon completed successfully")
