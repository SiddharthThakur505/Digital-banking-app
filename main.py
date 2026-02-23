import streamlit as st
from pathlib import Path
import json
import random
import string

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Simple Bank App", page_icon="🏦", layout="centered")

DATA_FILE = "data.json"

# ---------------- HELPER FUNCTIONS ----------------
def load_data():
    if Path(DATA_FILE).exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def generate_account():
    digits = random.choices(string.digits, k=4)
    letters = random.choices(string.ascii_letters, k=4)
    acc = digits + letters
    random.shuffle(acc)
    return "".join(acc)

# ---------------- LOAD DATA ----------------
data = load_data()

# ---------------- UI ----------------
st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Account Details",
        "Update Details",
        "Delete Account"
    ]
)

# ---------------- CREATE ACCOUNT ----------------
if menu == "Create Account":
    st.subheader("Create New Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")
    pin = st.text_input("4 Digit PIN", type="password")

    if st.button("Create Account"):
        if age > 18 and len(pin) == 4:
            account = {
                "name": name,
                "age": age,
                "phoneno.": phone,
                "email": email,
                "pin": int(pin),
                "accountno.": generate_account(),
                "balance": 0
            }
            data.append(account)
            save_data(data)
            st.success("Account Created Successfully 🎉")
            st.info(f"Your Account Number: {account['accountno.']}")
        else:
            st.error("Invalid Age or PIN")

# ---------------- DEPOSIT MONEY ----------------
elif menu == "Deposit Money":
    st.subheader("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        user = next((i for i in data if i["accountno."] == acc and i["pin"] == int(pin)), None)
        if user:
            user["balance"] += amount
            save_data(data)
            st.success("Amount Credited 💰")
        else:
            st.error("User Not Found")

# ---------------- WITHDRAW MONEY ----------------
elif menu == "Withdraw Money":
    st.subheader("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        user = next((i for i in data if i["accountno."] == acc and i["pin"] == int(pin)), None)
        if user:
            if user["balance"] >= amount:
                user["balance"] -= amount
                save_data(data)
                st.success("Amount Debited 💸")
            else:
                st.error("Insufficient Balance")
        else:
            st.error("User Not Found")

# ---------------- ACCOUNT DETAILS ----------------
elif menu == "Account Details":
    st.subheader("View Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show Details"):
        user = next((i for i in data if i["accountno."] == acc and i["pin"] == int(pin)), None)
        if user:
            st.json(user)
        else:
            st.error("User Not Found")

# ---------------- UPDATE DETAILS ----------------
elif menu == "Update Details":
    st.subheader("Update Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    user = next((i for i in data if i["accountno."] == acc and i["pin"] == int(pin)), None)

    if user:
        name = st.text_input("Name", user["name"])
        age = st.number_input("Age", value=user["age"])
        phone = st.text_input("Phone", user["phoneno."])
        email = st.text_input("Email", user["email"])

        if st.button("Update"):
            user["name"] = name
            user["age"] = age
            user["phoneno."] = phone
            user["email"] = email
            save_data(data)
            st.success("Details Updated Successfully ✨")
    elif acc:
        st.error("Invalid Credentials")

# ---------------- DELETE ACCOUNT ----------------
elif menu == "Delete Account":
    st.subheader("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete Account"):
        user = next((i for i in data if i["accountno."] == acc and i["pin"] == int(pin)), None)
        if user:
            data.remove(user)
            save_data(data)
            st.success("Account Deleted ❌")
        else:
            st.error("User Not Found")
