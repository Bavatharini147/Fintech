
import streamlit as st

st.set_page_config(
    page_title="Payment Amount",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Payment Details")
st.subheader("Step 2: Enter Amount")

if "recipient" not in st.session_state:
    st.warning("Please enter recipient details first.")
    st.stop()

st.write(
    f"Recipient Mobile Number: "
    f"**{st.session_state.recipient}**"
)

amount = st.number_input(
    "Enter Amount (₹)",
    min_value=0.0,
    step=100.0,
    format="%.2f"
)

col1, col2 = st.columns(2)

with col1:
    if st.button("Back"):
        st.switch_page("pages/payments.py")

with col2:
    if st.button("Continue", type="primary"):

        if amount <= 0:
            st.error("Enter an amount greater than zero.")

        else:
            st.session_state.payment_amount = amount

            st.switch_page(
                "pages/payment_confirm.py"
            )
