
import streamlit as st

st.set_page_config(
    page_title="Confirm Payment",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 Confirm Payment")
st.subheader("Step 3: Account Verification")

if "payment_amount" not in st.session_state:
    st.warning("Please enter the payment amount first.")
    st.stop()

if "spending_balance" not in st.session_state:
    st.error("Wallet is not initialized.")
    st.stop()

st.write(
    f"Recipient: **{st.session_state.recipient}**"
)

st.write(
    f"Amount to be paid: "
    f"**₹{st.session_state.payment_amount:,.2f}**"
)

password = st.text_input(
    "Enter Account Password",
    type="password",
    max_chars=6
)

col1, col2 = st.columns(2)

with col1:
    if st.button("Back"):
        st.switch_page(
            "pages/payment_amount.py"
        )

with col2:

    if st.button("Pay Now", type="primary"):

        if password != "123456":

            st.error("Incorrect account password.")

        else:

            amount = st.session_state.payment_amount

            spending = st.session_state.spending_balance
            savings = st.session_state.savings_balance

            if amount <= spending:

                # Deduct only from Spending
                st.session_state.spending_balance -= amount

                # Update total balance
                st.session_state.total_balance = (
                    st.session_state.savings_balance
                    + st.session_state.spending_balance
                )

                st.session_state.payment_status = "Success"

            elif amount <= spending + savings:

                st.session_state.payment_status = (
                    "Insufficient Spending Balance"
                )

            else:

                st.session_state.payment_status = (
                    "Insufficient Wallet Balance"
                )

            st.switch_page(
                "pages/payment_result.py"
            )
