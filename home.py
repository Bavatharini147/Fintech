
import streamlit as st

st.set_page_config(
    page_title="Home | Spending Analyser",
    page_icon="🏠",
    layout="wide"
)

# --------------------------------
# HEADER
# --------------------------------

st.title("💰 Welcome to Spending Analyser")

st.subheader(
    "Understand your money. Manage your spending. "
    "Build better financial habits."
)

st.write(
    """
    Spending Analyser is an intelligent personal finance
    management application designed to help users understand
    their spending patterns, manage their wallet and make
    informed financial decisions.
    """
)

st.divider()


# --------------------------------
# ABOUT THE APPLICATION
# --------------------------------

st.header("🌟 What Can You Do Here?")

col1, col2 = st.columns(2)

with col1:

    st.subheader("📊 Spending Analysis")

    st.write(
        """
        Upload your UPI transaction statement and
        understand your spending patterns through
        transaction summaries, charts and insights.
        """
    )

    st.subheader("💸 Discretionary Spending")

    st.write(
        """
        Identify non-essential purchases, classify
        transactions and understand how much money
        goes towards discretionary expenses.
        """
    )

    st.subheader("🧠 AI-Powered Insights")

    st.write(
        """
        Use AI to classify transactions, identify
        spending patterns and generate useful
        financial recommendations.
        """
    )


with col2:

    st.subheader("👛 Digital Wallet")

    st.write(
        """
        Manage your wallet using separate Savings
        and Spending compartments. Transfer money
        between them whenever required.
        """
    )

    st.subheader("💳 Payments")

    st.write(
        """
        Make simulated payments using a mobile number
        or QR code interface, with payments restricted
        to your Spending compartment.
        """
    )

    st.subheader("📜 Transaction History")

    st.write(
        """
        Review your payment and wallet transfer
        activities in one place.
        """
    )


st.divider()


# --------------------------------
# HOW TO GET STARTED
# --------------------------------

st.header("🚀 How to Get Started")

st.write(
    """
    1. Open **Spending Analyser** to upload your UPI statement.

    2. Visit **Discretionary Spending** to review and classify
       your purchases.

    3. Open **Wallet** to view balances and transfer money
       between compartments.

    4. Visit **Payments** to make a payment using your
       Spending balance.

    5. Explore AI insights to understand your financial habits.
    """
)


st.divider()


# --------------------------------
# FOOTER
# --------------------------------

st.caption(
    "Spending Analyser | Intelligent Personal Finance Management"
)
