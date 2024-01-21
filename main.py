import pandas as pd
import streamlit as st


st.header('Introduction to java programming', divider='rainbow')
st.header('java is :blue[cool] :sunglasses:')

image_path = "C:/Users/Admin/Downloads/download.png"
st.image(image_path)

# Modify the DataFrame to include "Python Preference" and show the increase in the current year
data_df = pd.DataFrame(
    {
        "python preference": [0, 4, 26, 80, 100, 40],
        "java preference": [10, 30, 60, 90, 120, 150],  # Adjust these values for Python Preference
    }
)

# Use the modified DataFrame and column_config
st.data_editor(
    data_df,
    column_config={
        "java preference": st.column_config.BarChartColumn(
            "Java Preference (last 6 months)",
            help="The Java preference volume in the last 6 months",
            y_min=0,
            y_max=250,  # Adjust the y_max value based on your data
        ),
        "python preference": st.column_config.BarChartColumn(
            "Python Preference (last 6 months)",
            help="The Python preference volume in the last 6 months",
            y_min=0,
            y_max=250,  # Adjust the y_max value based on your data
        ),
    },
    hide_index=True,
)
