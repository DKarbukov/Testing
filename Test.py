import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Function to display scatter plot
def display_scatter_plot(data):
    st.subheader("Scatter Plot")
    x_axis = st.selectbox("Select X-axis", options=data.columns)
    y_axis = st.selectbox("Select Y-axis", options=data.columns)
    plt.figure(figsize=(10, 6))
    plt.scatter(data[x_axis], data[y_axis])
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot()

def main():
    st.title("Simple Streamlit App with Pandas and Matplotlib")
    
    # File uploader
    st.sidebar.title("Upload File")
    uploaded_file = st.sidebar.file_uploader("Upload CSV", type=['csv'])
    
    if uploaded_file is not None:
        data = load_data(uploaded_file)
        st.write(data.head())
        display_scatter_plot(data)

if __name__ == "__main__":
    main()
