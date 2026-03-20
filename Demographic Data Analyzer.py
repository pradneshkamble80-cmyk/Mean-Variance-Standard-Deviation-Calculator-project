#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import urllib.request

url = "https://raw.githubusercontent.com/freeCodeCamp/boilerplate-demographic-data-analyzer/main/adult.data.csv"
urllib.request.urlretrieve(url, "adult.data.csv")


# In[5]:


import os
os.listdir()


# In[6]:


import pandas as pd

df = pd.read_csv("adult.data.csv")
df.head()


# In[7]:


race_count = df['race'].value_counts()
race_count


# In[8]:


average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
average_age_men


# In[9]:


percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)
percentage_bachelors


# In[11]:


higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])


# In[12]:


higher_edu_rich = round((df[higher_edu]['salary'] == '>50K').mean() * 100, 1)
higher_edu_rich


# In[15]:


higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
lower_edu = ~higher_edu


# In[16]:


lower_edu_rich = round((df[lower_edu]['salary'] == '>50K').mean() * 100, 1)
lower_edu_rich


# In[17]:


min_work_hours = df['hours-per-week'].min()
min_work_hours


# In[18]:


min_workers = df[df['hours-per-week'] == min_work_hours]

rich_percentage = round((min_workers['salary'] == '>50K').mean() * 100, 1)
rich_percentage


# In[19]:


country_salary = df.groupby('native-country')['salary'].apply(
    lambda x: (x == '>50K').mean() * 100
)

highest_earning_country = country_salary.idxmax()
highest_earning_country_percentage = round(country_salary.max(), 1)

highest_earning_country, highest_earning_country_percentage


# In[20]:


top_IN_occupation = df[
    (df['native-country'] == 'India') &
    (df['salary'] == '>50K')
]['occupation'].value_counts().idxmax()

top_IN_occupation


# In[21]:


print("Race count:\n", race_count)
print("Average age of men:", average_age_men)
print("% Bachelors:", percentage_bachelors)
print("Higher edu >50K:", higher_edu_rich)
print("Lower edu >50K:", lower_edu_rich)
print("Min hours:", min_work_hours)
print("Rich % among min workers:", rich_percentage)
print("Top country:", highest_earning_country)
print("Top country %:", highest_earning_country_percentage)
print("Top occupation India:", top_IN_occupation)


# In[ ]:




