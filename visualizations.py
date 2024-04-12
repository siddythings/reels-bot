import streamlit as st
import plotly.express as px


def show_sales_trends(df):
    """
    Display sales trends over time.

    Parameters:
    - df (pandas.DataFrame): DataFrame containing sales data.
    """
    st.subheader('Sales Trends Over Time')
    fig = px.line(df, x='Date', y='Sales', title='Sales Trends')
    st.plotly_chart(fig)


def show_geographical_distribution(df):
    """
    Display geographical distribution of sales.

    Parameters:
    - df (pandas.DataFrame): DataFrame containing sales data.
    """
    st.subheader('Geographical Distribution of Sales')
    # Assuming you have latitude and longitude columns in your data
    fig_map = px.scatter_geo(df, lat='Latitude', lon='Longitude',
                             color='Sales',
                             title='Geographical Distribution of Sales')
    st.plotly_chart(fig_map)