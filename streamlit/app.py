# Importing the required modules
import streamlit as st
import pyrebase

choice=st.sidebar.title("Login")
email=st.sidebar.text_input("Email")
password=st.sidebar.text_input("Password",type="password")


if st.sidebar.button("Login"):
    firebaseConfig = {
        # Enter your firebase credentials here
    }
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        st.sidebar.success("Logged in as {}".format(login['email']))
        st.sidebar.info("Welcome to the dashboard")
        st.sidebar.info("Select a page from the dropdown")
        page = st.sidebar.selectbox("Select a page", ["Home", "Data"])
        if page == "Home":
            st.title("Home")
            st.write("This is the home page")
        elif page == "Data":
            st.title("Data")
            st.write("This is the data page")
    except:
        st.sidebar.error("Incorrect email/password")