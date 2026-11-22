
import streamlit as st
import re


st.set_page_config(
    page_title="Payments",
    page_icon="💳",
    layout="wide"
)


st.title("💳 Make a Payment")


# --------------------------------
# INITIALIZE PAYMENT STEP
# --------------------------------

if "payment_step" not in st.session_state:
    st.session_state.payment_step = 1




# --------------------------------
# STEP 1: RECIPIENT DETAILS
# --------------------------------

if st.session_state.payment_step == 1:

    st.subheader("Step 1: Recipient Details")

    payment_method = st.radio(
        "Select Payment Method",
        ["Enter Mobile Number", "Scan QR Code"]
    )

    if payment_method == "Enter Mobile Number":

        mobile = st.text_input(
            "Recipient Mobile Number",
            max_chars=10,
            placeholder="Enter 10-digit mobile number"
        )

        if st.button("Continue", type="primary"):

            if not re.fullmatch(r"[6-9]\d{9}", mobile):
                st.error("Please enter a valid mobile number.")

            else:
                st.session_state.recipient = mobile
                st.session_state.payment_method = "Mobile Number"
                st.session_state.payment_step = 2
                st.rerun()

    else:

        qr_file = st.file_uploader(
            "Upload recipient QR code",
            type=["png", "jpg", "jpeg"]
        )

        if qr_file is not None:

            st.image(qr_file, width=250)

            st.info(
                "QR code decoding is not implemented yet. "
                "Please use mobile number payment for now."
            )


# --------------------------------
# STEP 2: PAYMENT AMOUNT
# --------------------------------

elif st.session_state.payment_step == 2:

    st.subheader("Step 2: Enter Payment Amount")

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

            st.session_state.payment_step = 1
            st.rerun()

    with col2:

        if st.button("Continue", type="primary"):

            if amount <= 0:

                st.error("Enter an amount greater than zero.")

            else:

                st.session_state.payment_amount = amount
                st.session_state.payment_step = 3
                st.rerun()


# --------------------------------
# STEP 3: ACCOUNT PASSWORD
# --------------------------------

elif st.session_state.payment_step == 3:

    st.subheader("Step 3: Confirm Payment")

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

            st.session_state.payment_step = 2
            st.rerun()

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

                st.session_state.payment_step = 4
                st.rerun()


# --------------------------------
# STEP 4: PAYMENT RESULT
# --------------------------------

elif st.session_state.payment_step == 4:

    st.subheader("Step 4: Payment Result")

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
    # NEW PAYMENT
    # --------------------------------

    if st.button("Make Another Payment", type="primary"):

        for key in [
            "recipient",
            "payment_method",
            "payment_amount",
            "payment_status"
        ]:

            st.session_state.pop(key, None)

        st.session_state.payment_step = 1
        st.rerun()
