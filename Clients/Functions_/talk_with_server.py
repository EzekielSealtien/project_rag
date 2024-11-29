import streamlit as st
import bcrypt

import requests

# Base URL for the FastAPI server
BASE_URL = "http://127.0.0.1:8000"


st.set_page_config(page_title="Medical System", page_icon="🌻", layout="centered")

# Helper function to create a new doctor
def create_doctor(doctor_data):
    url = f"{BASE_URL}/doctor/create_doctor"
    response = requests.post(url, json=doctor_data)
    return response.json()


def verify_password(stored_hash, entered_password):
    return bcrypt.checkpw(entered_password.encode('utf-8'), stored_hash.encode('utf-8'))



# Helper function to authenticate doctor
def login_doctor(email, password):
    url = f"{BASE_URL}/doctor"

    response = requests.get(url, params={"email": email})

    if response.status_code == 200:
        user_info = response.json()
        if verify_password(user_info["password"],password):
            return user_info
    return None




# Helper function to create a new report
def create_report(report_data):
    url = f"{BASE_URL}/report/create_report"
    response = requests.post(url, json=report_data)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle errors
        raise Exception(f"Failed to create report: {response.status_code}, {response.text}")



def update_abonnement(doctor_data):
    url = f"{BASE_URL}/doctor/update_abonnement"
    response = requests.put(url, json=doctor_data)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle errors
        raise Exception(f"Failed to update abonnement: {response.status_code}, {response.text}")
