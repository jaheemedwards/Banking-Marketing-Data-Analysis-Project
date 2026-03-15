import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(layout="wide")

# -------------------------
# TABS
# -------------------------
tab1, tab2, tab3 = st.tabs([
    "Overview",
    "Dashboard Screenshots",
    "Data Collection"
])

# -------------------------
# OVERVIEW TAB
# -------------------------
with tab1:

    st.title("Bank Marketing Campaign Analytics")

    col1, col2 = st.columns([1,2])

    with col1:
        st.write(
        """
        This project analyzes a **bank marketing campaign dataset** using a 
        dashboard built in **Microsoft Power BI**.

        The dashboard explores:
        - Campaign performance
        - Customer engagement
        - Conversion insights
        - Customer review sentiment
        """
        )

    with col2:

        video_path = "screenshots_and_video/Dashboard Demo video.mp4"

        with open(video_path, "rb") as f:
            video_bytes = f.read()

        video_base64 = base64.b64encode(video_bytes).decode()

        video_html = f"""
        <video width="100%" autoplay loop muted playsinline>
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """

        components.html(video_html, height=546)     # actual video height

    st.divider()

    st.subheader("Download Full Dashboard Report")

    with open("screenshots_and_video/Banking Marketing Data Analysis Project by Jaheem Edwards.pdf", "rb") as file:
        st.download_button(
            label="Download Dashboard PDF",
            data=file,
            file_name="screenshots_and_video/Banking Marketing Data Analysis Project by Jaheem Edwards.pdf.pdf",
            mime="application/pdf"
        )


# -------------------------
# SCREENSHOTS TAB
# -------------------------
with tab2:

    st.header("Power BI Dashboard Screenshots")

    col1, col2 = st.columns(2)

    with col1:
        st.image("screenshots_and_video/overview_screenshop.png", caption="Overview Dashboard")

        st.image("screenshots_and_video/social_media_details_screenshot.png", caption="Social Media Details")

    with col2:
        st.image("screenshots_and_video/conversion_details_screenshot.png", caption="Conversion Details")

        st.image("screenshots_and_video/customer_review_details_screenshot.png", caption="Customer Review Details")


# -------------------------
# DATA COLLECTION TAB
# -------------------------
with tab3:

    st.title("Data Collection")

    st.write(
    """
    This project uses **synthetic banking data**.

    Locations such as **towns and cities in Trinidad and Tobago** were scraped 
    from Wikipedia to enrich the dataset.

    Additional enrichment includes **sentiment analysis of customer reviews**
    performed using Python.
    """
    )

    st.subheader("Dataset Tables")

    tables = [
        "data/banking_campaigns.csv",
        "data/banking_engagement_data.csv",
        "data/banking_products.csv",
        "data/customer_journey_data.csv",
        "data/customer_reviews_sentiment.csv",
        "data/customer_reviews.csv",
        "data/synthetic_bank_customers.csv",
        "data/trinidad_and_tobago_all_cities_towns.csv"
    ]

    dataset_choice = st.selectbox("Select a dataset to explore", tables)

    df = pd.read_csv(dataset_choice)

    st.write("Dataset Preview")

    st.dataframe(df)

    st.write("Dataset Shape:", df.shape)

    st.write("Column Names:", df.columns.tolist())