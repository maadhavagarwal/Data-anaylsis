import pandas as pd
import streamlit as sl
# import matplotlib.pyplot as plt
try:
    df= pd.read_csv("cleaned_data.csv")
    print(df)
    sl.title("Cleaned File")
    sl.write(df)
except Exception as e:
    print(e)