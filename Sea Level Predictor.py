#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv("epa-sea-level.csv")

def draw_plot():
    fig, ax = plt.subplots()

    # Scatter
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Line 1 (all data)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = pd.Series(range(df['Year'].min(), 2051))
    ax.plot(years, res.intercept + res.slope * years, 'r')

    # Line 2 (from 2000)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    ax.plot(years_recent, res_recent.intercept + res_recent.slope * years_recent, 'g')

    # Labels
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    fig.savefig("sea_level_plot.png")
    return fig


# In[ ]:




