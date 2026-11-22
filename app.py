
import streamlit as st

st.set_page_config(
    page_title="Spending Analyser",
    page_icon="💰",
    layout="wide"
)

# --------------------------------
# APPLICATION NAVIGATION
# --------------------------------

home = st.Page(
    "home.py",
    title="Home",
    icon="🏠",
    default=True
)

spending = st.Page(
    "spending_analyser.py",
    title="Spending Analyser",
    icon="📊"
)

discretionary = st.Page(
    "pages/Discretionary_Spending.py",
    title="Discretionary Spending",
    icon="💸"
)

payments = st.Page(
    "pages/payments.py",
    title="Payments",
    icon="💳"
)

wallet = st.Page(
    "pages/wallet.py",
    title="Wallet",
    icon="👛"
)

# --------------------------------
# INITIALIZE WALLET BALANCES
# --------------------------------

if "total_balance" not in st.session_state:
    st.session_state.total_balance = 10000.0

if "savings_balance" not in st.session_state:
    st.session_state.savings_balance = 0.0

if "spending_balance" not in st.session_state:
    st.session_state.spending_balance = 10000.0

# --------------------------------
# SIDEBAR
# --------------------------------

pg = st.navigation(
    [
        home,
        spending,
        discretionary,
        payments,
        wallet
    ]
)

pg.run()
