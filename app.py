import streamlit as st
import pandas as pd
import requests
import io

st.title("Log Classification Using Hybrid Classifier")

# Upload CSV
uploaded_file = st.file_uploader("Upload your log CSV file", type=["csv"])

if uploaded_file:
    # Read the uploaded CSV
    logs_df = pd.read_csv(uploaded_file)
    st.write("Preview of Uploaded Logs:")
    st.dataframe(logs_df)

    # Classification trigger
    if st.button("Classify Logs"):
        try:
            # Send file to FastAPI backend
            files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")}
            response = requests.post("http://localhost:8000/classify/", files=files)

            if response.status_code == 200:
                # Read the returned classified CSV
                classified_df = pd.read_csv(io.BytesIO(response.content))
                st.success("Logs successfully classified!")
                st.dataframe(classified_df)

                # Download button
                csv = classified_df.to_csv(index=False).encode("utf-8")
                st.download_button("Download Classified CSV", csv, "classified_logs.csv", "text/csv")
            else:
                st.error(f"Error from API: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
