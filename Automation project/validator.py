import logging
import os
import csv


def validate_csv(file_path, required_columns):
    if not os.path.exists(file_path):
        logging.error("File does not exist: %s", file_path)
        return False

    if os.path.getsize(file_path) == 0:
        logging.warning("File is empty: %s", file_path)
        return False
    if not file_path.lower().endswith('.csv'):
        logging.error("Not a CSV file: %s", file_path)
        return False

    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            columns = reader.fieldnames

            if columns is None:
                logging.error('CSV has no header row')
                return False

            missing = [col for col in required_columns if col not in columns]

            if missing:
                logging.error(
                    "Missing required columns: %s. Found: %s",
                    missing, columns
                )
                return False

            logging.info(
                "CSV validated succesfully.Required column '%s' exists.",
                required_columns
            )
            return True

    except Exception as e:
        logging.exception("falied to read CSV file")
        return False
