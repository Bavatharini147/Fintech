import streamlit as st

from utils.pdf_extractor import extract_transactions
from utils.data_cleaner import clean_data
from utils.analyzer import analyze_transactions

import hashlib
from utils.expense_classifier import classify_merchant



# --------------------------------
# INITIALIZE SESSION STATE
# --------------------------------

if "transactions" not in st.session_state:
    st.session_state.transactions = None

if "transaction_file_id" not in st.session_state:
    st.session_state.transaction_file_id = None

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="UPI Spending Analyzer",
    page_icon="💰",
    layout="wide"
)


# --------------------------------
# TITLE
# --------------------------------

st.title("💰 UPI Spending Analyzer")

st.write(
    "Upload your UPI transaction statement "
    "to discover where your money is going."
)



# --------------------------------
# PDF UPLOAD
# --------------------------------

uploaded_file = st.file_uploader(
    "Upload your transaction statement",
    type=["pdf"]
)

if uploaded_file is not None:

    # Generate a unique ID for the uploaded PDF
    file_id = hashlib.md5(
        uploaded_file.getvalue()
    ).hexdigest()

    # Process only if this is a new PDF
    if st.session_state.transaction_file_id != file_id:

        with st.spinner("Reading transaction statement..."):

            # Extract transactions
            df = extract_transactions(uploaded_file)

            if df.empty:
                st.error("Could not extract transactions from this PDF.")
                st.stop()

            # Clean transactions
            df = clean_data(df)

            # Store cleaned transactions
            st.session_state.transactions = df.copy()

            # Store PDF ID
            st.session_state.transaction_file_id = file_id

            # Reset old classifications when a new PDF is uploaded
            st.session_state.pop("discretionary_classifications", None)

    # Retrieve stored transactions
    df = st.session_state.transactions.copy()

    # Analyze transactions
    results = analyze_transactions(df)

    # --------------------------------
    # MAIN SUMMARY
    # --------------------------------

    st.subheader("📊 Spending Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Spent",
            f"₹{results['total_spent']:,.2f}"
        )

    with col2:
        st.metric(
            "Total Received",
            f"₹{results['total_received']:,.2f}"
        )

    with col3:
        st.metric(
            "Current Balance",
            f"₹{results['current_balance']:,.2f}"
        )

    # --------------------------------
    # MAIN INSIGHT
    # --------------------------------

    st.subheader("🔍 Where Did You Spend the Most?")

    st.success(
        f"You spent the most on "
        f"**{results['top_recipient']}** — "
        f"₹{results['top_recipient_amount']:,.2f}"
    )

    # --------------------------------
    # MOST FREQUENT
    # --------------------------------

    st.info(
        f"🔄 Your most frequent payment recipient "
        f"was **{results['most_frequent']}**."
    )

    # --------------------------------
    # RECIPIENT ANALYSIS
    # --------------------------------

    st.subheader("💸 Spending by Person / Merchant")

    recipient_summary = (
        results["recipient_summary"]
        .rename(
            columns={
                "total_spent": "Total Spent (₹)",
                "transaction_count": "Number of Transactions"
            }
        )
    )

    st.dataframe(
        recipient_summary,
        use_container_width=True
    )

    # --------------------------------
    # SPENDING CHART
    # --------------------------------

    st.subheader("📈 Where Your Money Goes")

    chart_data = (
        results["recipient_summary"]["total_spent"].head(10)
    )

    st.bar_chart(chart_data)

    # --------------------------------
    # LARGEST TRANSACTION
    # --------------------------------

    st.subheader("💰 Largest Single Payment")

    largest = results["largest_transaction"]

    st.warning(
        f"Your largest single payment was "
        f"**₹{largest['Amount (INR)']:,.2f}** "
        f"to **{largest['Description']}** "
        f"on **{largest['Date'].strftime('%d-%m-%Y')}**."
    )

    # --------------------------------
    # DAILY SPENDING
    # --------------------------------

    st.subheader("📅 Daily Spending")

    st.line_chart(results["daily_spending"])

    # --------------------------------
    # RAW TRANSACTIONS
    # --------------------------------

    with st.expander("View All Transactions"):

        st.dataframe(
            df,
            use_container_width=True
        )
