import pandas as pd


def clean_data(df):

    if df.empty:
        return df

    # Remove spaces from column names
    df.columns = df.columns.str.strip()

    # Convert date
    df["Date"] = pd.to_datetime(
        df["Date"],
        dayfirst=True,
        errors="coerce"
    )

    # Clean amount
    df["Amount (INR)"] = (
        df["Amount (INR)"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.replace("₹", "", regex=False)
        .str.strip()
    )

    # Clean balance
    df["Balance (INR)"] = (
        df["Balance (INR)"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.replace("₹", "", regex=False)
        .str.strip()
    )

    # Convert to numbers
    df["Amount (INR)"] = pd.to_numeric(
        df["Amount (INR)"],
        errors="coerce"
    )

    df["Balance (INR)"] = pd.to_numeric(
        df["Balance (INR)"],
        errors="coerce"
    )

    # Clean text columns
    df["Description"] = (
        df["Description"]
        .astype(str)
        .str.strip()
    )

    df["Type"] = (
        df["Type"]
        .astype(str)
        .str.strip()
        .str.capitalize()
    )

    # Remove invalid transactions
    df = df.dropna(
        subset=[
            "Date",
            "Description",
            "Amount (INR)"
        ]
    )
    df = df[df["Type"].isin(["Debit", "Credit"])]
    return df