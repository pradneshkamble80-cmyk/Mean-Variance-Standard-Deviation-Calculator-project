#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_csv("medical_examination.csv")

# Add overweight column
df['overweight'] = (df['weight'] / ((df['height']/100)**2) > 25).astype(int)

# Normalize cholesterol and glucose
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


def draw_cat_plot():

    # Create DataFrame for cat plot
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol','gluc','smoke','alco','active','overweight']
    )

    # Group and count
    df_cat = df_cat.groupby(['cardio','variable','value']).size().reset_index(name='total')

    # Draw plot
    fig = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar'
    ).fig

    return fig


def draw_heat_map():

    # Clean data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Correlation
    corr = df_heat.corr(numeric_only=True)

    # Mask
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Plot
    fig, ax = plt.subplots(figsize=(10,8))

    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        linewidths=.5,
        cbar_kws={"shrink": .5}
    )

    return fig


# In[ ]:




