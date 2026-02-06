import pandas as pd
import logging


def clean_price_quantity(df, price_col, quantity_col, max_deviation):

    missing_price = df[price_col].isna().sum()
    missing_quantity = df[quantity_col].isna().sum()

    original_count = len(df)

    df_cleaned = df.dropna(subset=[price_col, quantity_col])
    dropped_count = original_count - len(df_cleaned)

    if original_count == 0:
        logging.warning("Input DataFrame is empty.")
        return df

    deviation = dropped_count / original_count

    if deviation > max_deviation:
        logging.error(
            "Deviation %.2f exceeds max allowed %.2f. Returning original data.",
            deviation,
            max_deviation
        )
        return df
    else:
        logging.info(
            "Data cleaned successfully. Dropped %d rows (deviation %.2f). "
            "Missing price: %d, missing quantity: %d.",
            dropped_count,
            deviation,
            missing_price,
            missing_quantity
        )
        return df_cleaned
