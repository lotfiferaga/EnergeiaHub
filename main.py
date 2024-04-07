import streamlit as st
import requests
import pandas as pd

def home_section():
    st.title("Home")
    st.write("Welcome to the Home section.")
    # Add more content as needed

def energy_consumption_section():
    st.title("Energy Consumption")
    st.write("This section provides information about energy consumption.")
    # Getting into the data about energy consumption
    st.subheader("Electricity")
    st.write("This subsection provides information about Electricity.")

    # Allow user to input URL dynamically

def energy_production_section():
    st.title("Energy Production")
    st.write("This section provides information about energy production.")
    # Add more content as needed

def energy_storage_section():
    st.title("Energy Storage")
    st.write("This section provides information about energy storage.")
    # Add more content as needed

def energy_infrastructure_section():
    st.title("Energy Infrastructure")
    st.write("This section provides information about energy infrastructure.")
    # Add more content as needed
def contact_us_section():
    st.title("Contact Us")
    st.write("Please fill out the form below to contact us.")

    with st.form(key='contact', clear_on_submit=True):
        first_name = st.text_input('First Name')
        last_name = st.text_input('Last Name')
        email = st.text_input('Email')
        message = st.text_area('Message', height=100)

        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            # You can add your logic here to handle the form submission
            st.success("Form submitted successfully!")
            st.write(f"First Name: {first_name}")
            st.write(f"Last Name: {last_name}")
            st.write(f"Email: {email}")
            st.write(f"Message: {message}")


def main():
    # Sidebar
    st.sidebar.title("Menu")

    # Display buttons without icons
    if st.sidebar.button('Home'):
        home_section()

    if st.sidebar.button('Energy Consumption'):
        energy_consumption_section()

    if st.sidebar.button('Energy Production'):
        energy_production_section()

    if st.sidebar.button('Energy Storage'):
        energy_storage_section()

    if st.sidebar.button('Energy Infrastructure'):
        energy_infrastructure_section()

    if st.sidebar.button('Contact Us'):
        contact_us_section()


if __name__ == "__main__":
    main()
