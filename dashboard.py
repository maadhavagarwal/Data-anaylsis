import pandas as pd
import streamlit as sl
import visulation as vis
df= pd.read_csv("country_wise_latest.csv")
def Drop():
   a=sl.selectbox("choose one",df.columns,index=14)
   if a == "Country/Region":
      i=sl.selectbox("choose one",df["Country/Region"])
      sl.bar_chart(df[i])
   if a == "Deaths" or a == "Confirmed" or a == "Recovered":
      vis.plot_total_cases()
   # date_range = sl.sidebar.date_input('Select Date Range', [df['Deaths'].min(), df['Deaths'].max()])
   # filtered_df = df[(df['Deaths'] >= date_range[0]) & (df['Deaths'] <= date_range[1])]
   # sl.bar_chart(filtered_df['Deaths'])
   return a