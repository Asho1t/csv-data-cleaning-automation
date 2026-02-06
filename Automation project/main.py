import pandas as pd
import logging

from logger_config import setup_logger
from validator import validate_csv
from cleaner import clean_price_quantity
setup_logger()


def main():
    # 1️⃣ Setup logger

    logging.info("Automation started")

    # 2️⃣ User input
    file_path = input("Enter CSV file path: ").strip()
    price_col = input("Enter price column name: ").strip()
    quantity_col = input("Enter quantity column name: ").strip()
    max_deviation = float(input("Enter max allowed deviation (e.g. 0.05): "))

    required_columns = [price_col, quantity_col]

    # 3️⃣ Validate file
    if not validate_csv(file_path, required_columns):
        logging.error("Validation failed. Automation stopped.")
        return

    # 4️⃣ Read CSV
    try:
        df = pd.read_csv(file_path)
        logging.info("CSV loaded successfully. Rows: %d", len(df))
    except Exception as e:
        logging.exception("Failed to load CSV")
        return

    # 5️⃣ Clean data
    cleaned_df = clean_price_quantity(
        df,
        price_col,
        quantity_col,
        max_deviation
    )

    # 6️⃣ Save output
    output_path = "cleaned_output.csv"
    cleaned_df.to_csv(output_path, index=False)
    logging.info("Cleaned file saved as %s", output_path)

    logging.info("Automation finished successfully")


if __name__ == "__main__":
    main()
