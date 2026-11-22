
import streamlit as st
import pandas as pd

from ai.ai_classifier import classify_transaction


st.title("💸 Discretionary Spending Analysis")


# --------------------------------
# GET TRANSACTIONS FROM HOME PAGE
# --------------------------------

if st.session_state.get("transactions") is None:

    st.warning(
        "Please upload your PDF on the Spending analyser page first."
    )

    st.stop()


df = st.session_state.transactions.copy()


# --------------------------------
# FILTER DEBIT TRANSACTIONS ONLY
# --------------------------------

df = df[
    df["Type"].astype(str).str.strip().str.lower() == "debit"
].copy()


if df.empty:

    st.warning("No debit transactions found.")

    st.stop()



# --------------------------------
# INITIAL AI CLASSIFICATION
# --------------------------------

# Consider debit transactions only
df = df[
    df["Type"].astype(str).str.strip().str.lower() == "debit"
].copy()

if "discretionary_classifications" not in st.session_state:

    with st.spinner("AI is analyzing your transactions..."):

        ai_results = [
            classify_transaction(description)
            for description in df["Description"]
        ]

        df["Classification"] = [
            result["classification"]
            for result in ai_results
        ]

        df["AI Confidence"] = [
            round(result["confidence"] * 100, 2)
            for result in ai_results
        ]

        df["AI Reason"] = [
            result["reason"]
            for result in ai_results
        ]

        st.session_state.discretionary_classifications = df.copy()


# --------------------------------
# GET CLASSIFIED DATA
# --------------------------------

classified_df = (
    st.session_state.discretionary_classifications.copy()
)


# --------------------------------
# VIEW / HIDE TRANSACTIONS BUTTON
# --------------------------------

if "show_discretionary_transactions" not in st.session_state:

    st.session_state.show_discretionary_transactions = False


button_label = (
    "Hide Transactions"
    if st.session_state.show_discretionary_transactions
    else "View Transactions"
)


if st.button(button_label):

    st.session_state.show_discretionary_transactions = (
        not st.session_state.show_discretionary_transactions
    )


# --------------------------------
# EDIT TRANSACTION CLASSIFICATION
# --------------------------------

if st.session_state.show_discretionary_transactions:

    st.subheader("📝 Review Your Transactions")

    edited_df = st.data_editor(

        classified_df,

        column_config={

            "Classification":
                st.column_config.SelectboxColumn(
                    "Expense Type",
                    options=[
                        "Essential",
                        "Discretionary",
                        "Needs Review"
                    ],
                    required=True
                )
        },

        disabled=[
            col for col in classified_df.columns
            if col != "Classification"
        ],

        hide_index=True,

        use_container_width=True,

        key=f"classification_editor_{st.session_state.get('transaction_file_id', 'default')}"
    )

    # Save edited classifications
    st.session_state.discretionary_classifications = (
        edited_df.copy()
    )

    classified_df = edited_df.copy()


# --------------------------------
# DISCRETIONARY TRANSACTIONS
# --------------------------------

discretionary_df = classified_df[
    classified_df["Classification"] == "Discretionary"
].copy()


# --------------------------------
# CALCULATE TOTAL SPENDING
# --------------------------------

total_spent = classified_df["Amount (INR)"].sum()

total_discretionary = discretionary_df["Amount (INR)"].sum()


# Calculate percentage

percentage = (

    (total_discretionary / total_spent) * 100

    if total_spent > 0 else 0

)


# --------------------------------
# SPENDING SUMMARY
# --------------------------------

st.subheader("📊 Discretionary Spending Summary")


col1, col2 = st.columns(2)


with col1:

    st.metric(

        "Total Discretionary Spending",

        f"₹{total_discretionary:,.2f}"

    )


with col2:

    st.metric(

        "Percentage of Total Spending",

        f"{percentage:.2f}%"

    )


# --------------------------------
# HIGHEST DISCRETIONARY PURCHASE
# --------------------------------

st.subheader("🏆 Highest Discretionary Spending")


if not discretionary_df.empty:

    merchant_summary = (

        discretionary_df
        .groupby("Description")["Amount (INR)"]
        .sum()
        .sort_values(ascending=False)

    )


    top_merchant = merchant_summary.index[0]

    top_amount = merchant_summary.iloc[0]


    st.success(

        f"Your highest discretionary spending was at "
        f"**{top_merchant}** — ₹{top_amount:,.2f}"

    )


    # --------------------------------
    # DISCRETIONARY SPENDING CHART
    # --------------------------------

    st.subheader("📈 Spending by Merchant")


    st.bar_chart(merchant_summary)


    # --------------------------------
    # DISCRETIONARY TRANSACTION DETAILS
    # --------------------------------

    st.subheader("📋 Discretionary Purchase Details")


    st.dataframe(

        discretionary_df[
            ["Date", "Description", "Amount (INR)"]
        ],

        use_container_width=True,

        hide_index=True

    )


else:

    st.info(
        "No transactions are currently classified as Discretionary. "
        "Click View Transactions to review your classifications."
    )
