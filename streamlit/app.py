# Importing the required modules
import streamlit as st
import pyrebase
from DummyDataGenerater import CreateAccount,GetBalance,GetTransactions

firebaseConfig = {
        "apiKey": "AIzaSyAE3UgqtUQgtYLnhsK75nkTrK2iOytOO2g",
        "authDomain": "banktest-5c63e.firebaseapp.com",
        "databaseURL": "https://banktest-5c63e-default-rtdb.firebaseio.com",
        "projectId": "banktest-5c63e",
        "storageBucket": "banktest-5c63e.appspot.com",
        "messagingSenderId": "857319041488",
        "appId": "1:857319041488:web:35c9fedf1a614ababb31d5",
        "measurementId": "G-2SVWMXSL9V"
    }
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Firebase Database

db=firebase.database() # Database

choice=st.sidebar.title("Login")
email=st.sidebar.text_input("Email")
password=st.sidebar.text_input("Password",type="password")


if st.sidebar.button("Login"):
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        st.sidebar.success("Logged in as {}".format(db.child("Account").child(login['localId']).child("name").get().val()))
        
        # Display the account balance
        st.subheader("Account Balance")
        st.success(GetBalance(login['localId']))

        # Display the account transactions
        st.subheader("Account Transactions")
        tr=GetTransactions(login['localId'])
        if tr:
            for transaction_key, transaction_value in tr.each():
                recipient = transaction_value.get('recipient')
                st.success(f"Recipient: {recipient}")
        else:
            st.info("No transactions found")

    except:
        st.sidebar.error("Incorrect email/password")