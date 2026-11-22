def analyze_transactions(df):

    # Only debit transactions
    debit_df = df[
        df["Type"].str.lower() == "debit"
    ]

    # Total amount spent
    total_spent = debit_df["Amount (INR)"].sum()

    # Total amount received
    credit_df = df[
        df["Type"].str.lower() == "credit"
    ]

    total_received = credit_df["Amount (INR)"].sum()

    # Latest balance
    current_balance = df.iloc[-1]["Balance (INR)"]

    # --------------------------------
    # WHERE DID I SPEND THE MOST?
    # --------------------------------

    recipient_summary = (
        debit_df
        .groupby("Description")["Amount (INR)"]
        .agg(
            total_spent="sum",
            transaction_count="count"
        )
        .sort_values(
            by="total_spent",
            ascending=False
        )
    )

    # Person / merchant where most money was spent
    top_recipient = recipient_summary.index[0]

    top_recipient_amount = (
        recipient_summary.iloc[0]["total_spent"]
    )

    # Most frequent recipient
    most_frequent = (
        recipient_summary
        .sort_values(
            by="transaction_count",
            ascending=False
        )
        .index[0]
    )

    # Largest single transaction
    largest_transaction = debit_df.loc[
        debit_df["Amount (INR)"].idxmax()
    ]

    # Daily spending
    daily_spending = (
        debit_df
        .groupby("Date")["Amount (INR)"]
        .sum()
    )

    return {

        "total_spent": total_spent,

        "total_received": total_received,

        "current_balance": current_balance,

        "recipient_summary": recipient_summary,

        "top_recipient": top_recipient,

        "top_recipient_amount": top_recipient_amount,

        "most_frequent": most_frequent,

        "largest_transaction": largest_transaction,

        "daily_spending": daily_spending
    }