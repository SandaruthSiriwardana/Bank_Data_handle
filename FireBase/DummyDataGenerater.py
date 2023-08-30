import pyrebase
from datetime import datetime
import hashlib  # For password hashing

# Config for Firebase
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

# Firebase Authentication

firebase=pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Firebase Database

db=firebase.database() # Database


# Function to hash passwords before storage
def hash_password(password):
    salt = "random_salt_here"  # Add a random salt for security
    return hashlib.sha256((password + salt).encode()).hexdigest()

# Create New Account ---------------------------------------------
def CreateAccount(UserName, userEmail, userAccountType, InitialBalance, password):

    hashed_password = hash_password(password)

    user=auth.create_user_with_email_and_password(userEmail,password)

    current_datetime = datetime.now()
    transactionRecipient = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    account_data = {
        "name": UserName,
        "email": userEmail,
        "account_type": userAccountType,
        "balance": InitialBalance,
        "account_number": user['localId'],
        "password": hashed_password,  # Store the hashed password
        "transactions": {
            "type": "Open Account",
            "amount": InitialBalance,
            "recipient": transactionRecipient
        }
    }
    db.child("Account").child(user['localId']).set(account_data)

    print(f"Account {user['localId']} has been created with an initial balance of {InitialBalance} {userAccountType} for {UserName} at {transactionRecipient}")
    # return accountNumber

CreateAccount("ks","ks@gmail.com","saving",100,"123456")