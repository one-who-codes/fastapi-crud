import streamlit as st
import requests

st.title("FastAPI Crud app")

API_URL = "http://127.0.0.1:8000/items/"

st.header("Add details")
name = st.text_input("Name")
address = st.text_input("Address")

if st.button("Add item"):
    item = {"name":name, "address":address}
    response = requests.post(API_URL,json=item)
    if response.status_code == 200:
        st.success("Item added successfully!")
    else:
        st.error("Failed to add item.")


st.header("Data Table")
try:
    response = requests.get(API_URL)
    if response.status_code == 200:
        try:
            items = response.json()  
            if items:
                st.table(items)
            else:
                st.warning("No data available.")
        except ValueError:
            st.error("Response is not valid JSON.")
    else:
        st.error(f"Failed to retrieve data. Status Code: {response.status_code}")
except Exception as e:
    st.error(f"An error occurred while fetching data: {e}")