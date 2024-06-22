# Task to perform
# Calculate total cases (confirmed, deaths, recovered).
# Identify countries/states with the highest and lowest cases.
import exception as ex
import pandas as pd
import streamlit as sl
# import matplotlib.pyplot as plt
df= pd.read_csv("cleaned_data.csv")
print(df)
sl.title("Anylsis")
sl.write(df)
print(df.info())
sl.write("Confirmed cases:",df["Confirmed"].sum())
sl.write("Recovered cases:",df["Recovered"].sum())
sl.write("Death cases:",df["Deaths"].sum())
name=df.columns
print(name)
try:
    df.sort_values(df.columns[-14],axis=0,ascending=[False],inplace=True)
    sl.write("Country with minimum cases:",df.tail(1))
    sl.write("Country with maximum cases:",df.head(1))
except ex.order as e:
    print(e)