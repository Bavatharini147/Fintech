import pdfplumber
import pandas as pd


def extract_transactions(pdf_file):

    rows = []

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            table = page.extract_table()

            if table:
                rows.extend(table)

    if not rows:
        return pd.DataFrame()

    # First row contains column names
    columns = rows[0]

    # Remaining rows contain transactions
    data = rows[1:]

    df = pd.DataFrame(data, columns=columns)

    return df