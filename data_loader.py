# Assistant 
# /my_streamlit_project/data_loader.py
import pandas as pd

def load_data(uploaded_file):
    """
    Load data from the uploaded CSV file.

    Parameters:
    - uploaded_file (object): Uploaded CSV file object.

    Returns:
    - pandas.DataFrame: Loaded DataFrame.
    """
    # Read CSV file
    df = pd.read_csv(uploaded_file)
    return df
