
import streamlit as st

st.set_page_config(
    page_title="My Wallet",
    page_icon="💰",
    layout="wide"
)

st.title("💰 My Wallet")


# --------------------------------
# DEFAULT ACCOUNT NUMBER
# --------------------------------

ACCOUNT_NUMBER = "123456"


# --------------------------------
# INITIALIZE WALLET
# --------------------------------

if "total_balance" not in st.session_state:
    st.session_state.total_balance = 10000.0

if "savings_balance" not in st.session_state:
    st.session_state.savings_balance = 0.0

if "spending_balance" not in st.session_state:
    st.session_state.spending_balance = 10000.0


# --------------------------------
# ACCOUNT VERIFICATION
# --------------------------------

if "wallet_verified" not in st.session_state:
    st.session_state.wallet_verified = False


if not st.session_state.wallet_verified:

    st.subheader("🔐 Wallet Account Verification")

    account_input = st.text_input(
        "Enter your account number",
        type="password",
        max_chars=6
    )

    if st.button("View Wallet"):

        if account_input == ACCOUNT_NUMBER:

            st.session_state.wallet_verified = True
            st.rerun()

        else:

            st.error("Invalid account number. Please try again.")

    st.stop()


# --------------------------------
# WALLET OVERVIEW
# --------------------------------

st.subheader("Wallet Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Balance",
        f"₹{st.session_state.total_balance:,.2f}"
    )

with col2:
    st.metric(
        "Savings Balance",
        f"₹{st.session_state.savings_balance:,.2f}"
    )

with col3:
    st.metric(
        "Spending Balance",
        f"₹{st.session_state.spending_balance:,.2f}"
    )


st.divider()


# --------------------------------
# TRANSFER MONEY
# --------------------------------

st.subheader("🔄 Transfer Between Compartments")

source = st.selectbox(
    "Transfer From",
    ["Spending", "Savings"]
)

destination = (
    "Savings" if source == "Spending"
    else "Spending"
)

st.write(f"Transfer To: **{destination}**")

amount = st.number_input(
    "Enter Transfer Amount (₹)",
    min_value=0.0,
    step=100.0,
    format="%.2f"
)


# --------------------------------
# TRANSFER BUTTON
# --------------------------------

if st.button("Transfer Money"):

    if amount <= 0:

        st.error("Enter an amount greater than zero.")

    elif source == "Spending":

        if amount > st.session_state.spending_balance:

            st.error("Insufficient Spending balance.")

        else:

            st.session_state.spending_balance -= amount
            st.session_state.savings_balance += amount

            st.success(
                f"₹{amount:,.2f} transferred from Spending to Savings!"
            )

            st.rerun()

    else:

        if amount > st.session_state.savings_balance:

            st.error("Insufficient Savings balance.")

        else:

            st.session_state.savings_balance -= amount
            st.session_state.spending_balance += amount

            st.success(
                f"₹{amount:,.2f} transferred from Savings to Spending!"
            )

            st.rerun()


# --------------------------------
# LOCK WALLET
# --------------------------------

st.divider()

if st.button("🔒 Lock Wallet"):

    st.session_state.wallet_verified = False
    st.rerun()
