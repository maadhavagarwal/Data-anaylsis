import matplotlib.pyplot as plt
import pandas as pd
import streamlit as sl
# df = pd.read_csv('cleaned_data.csv')
def plot_total_cases(df):
    # plt.figure(900*100)
    plt.figure().set_figheight(40)
    sl.write("Total cases vs Country")
    sl.write("Confrim cases")
    plt.scatter(df['Confirmed'], df['Country/Region'])
    sl.pyplot(plt)
    plt.savefig("confim.png")
    sl.write("Death cases")
    
    plt.scatter(df['Deaths'], df['Country/Region'])
    sl.pyplot(plt)
    plt.savefig("death.png")
    sl.write("Recoverd cases")
    plt.scatter(df['Recovered'], df['Country/Region'])
    plt.savefig("recoverd.png")
    sl.pyplot(plt)
    # plt.savefig("")
def plot_top_countries(df):
     plt.scatter( df['Country/Region'])
     sl.pyplot(plt)
     plt.savefig("top_countries.png")
def plot_daily_cases(df):
      plt.figure().set_figheight(35)
      plt.scatter(df['New cases'], df['Country/Region'])
      plt.savefig("daily_cases.png")
      sl.pyplot(plt)
plot_daily_cases()
plot_total_cases()

     

    