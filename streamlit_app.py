import streamlit as st

st.title("Portfolio Prioritization Agent")
st.write("This app will help evaluate and prioritize portfolio initiatives.")
import pandas as pd

data = {
    "Initiative": [
        "Claims Automation",
        "Customer Service AI",
        "Legacy Platform Upgrade"
    ],
    "Business Value": [9, 8, 7],
    "Strategic Alignment": [9, 8, 9],
    "Urgency": [8, 7, 6],
    "Effort": [6, 5, 9],
    "Risk": [5, 4, 7]
}

portfolio = pd.DataFrame(data)

st.subheader("Portfolio Initiatives")

st.dataframe(portfolio)
