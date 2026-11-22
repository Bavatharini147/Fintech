
import streamlit as st

st.set_page_config(
    page_title="Payment Result",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Payment Result")

if "payment_status" not in st.session_state:

    st.warning("No payment result available.")
    st.stop()

status = st.session_state.payment_status

if status == "Success":

    st.success("✅ Payment Successful!")

    st.write(
        f"Recipient: **{st.session_state.recipient}**"
    )

    st.write(
        f"Amount Paid: "
        f"**₹{st.session_state.payment_amount:,.2f}**"
    )

elif status == "Insufficient Spending Balance":

    st.error("Insufficient Spending Balance")

else:

    st.error("Insufficient Wallet Balance")


# --------------------------------
# BACK TO HOME
# --------------------------------

if st.button("Back to Home", type="primary"):

    for key in [
        "recipient",
        "payment_method",
        "payment_amount",
        "payment_status"
    ]:
        st.session_state.pop(key, None)

    st.switch_page("app.py")
