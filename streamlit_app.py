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

portfolio = st.data_editor(
    portfolio,
    num_rows="dynamic",
    use_container_width=True,
    column_config={
        "Business Value": st.column_config.NumberColumn(
            min_value=1,
            max_value=10,
            step=1
        ),
        "Strategic Alignment": st.column_config.NumberColumn(
            min_value=1,
            max_value=10,
            step=1
        ),
        "Urgency": st.column_config.NumberColumn(
            min_value=1,
            max_value=10,
            step=1
        ),
        "Effort": st.column_config.NumberColumn(
            min_value=1,
            max_value=10,
            step=1
        ),
        "Risk": st.column_config.NumberColumn(
            min_value=1,
            max_value=10,
            step=1
        )
    }
)
portfolio["Priority Score"] = (
    portfolio["Business Value"] * 0.30
    + portfolio["Strategic Alignment"] * 0.30
    + portfolio["Urgency"] * 0.20
    + (11 - portfolio["Effort"]) * 0.10
    + (11 - portfolio["Risk"]) * 0.10
) * 10

portfolio["Priority Score"] = portfolio["Priority Score"].round(1)

prioritized_portfolio = portfolio.sort_values(
    "Priority Score",
    ascending=False
)

st.subheader("Prioritized Portfolio")

st.dataframe(
    prioritized_portfolio,
    use_container_width=True
)
