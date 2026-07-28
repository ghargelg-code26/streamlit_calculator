# Importing the Streamlit Library
import streamlit as st
#importing the MultiPage class from app_pages.multi_page module
from app_pages.multi_page import MultiPage
 # Importing the calculator_body function from app_pages.page_calculator module
from app_pages.page_calculator import calculator_body 
from app_pages.page1 import page1_body
from app_pages.page2 import page2_body
# Declaring the app name
app = MultiPage(app_name="app with calculator")
# Creating an instance of the MultiPage class with the app name "Calculator App"

app.add_page("Page 1", page1_body)
app.add_page("Page 2", page2_body)
app.add_page("Calculator", calculator_body)

app.run()