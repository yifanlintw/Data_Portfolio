#!/usr/bin/env python
# coding: utf-8

# # COVID19 Data Analysis Using Python
# 
# In this project we are going to use COVID19 dataset we have consisting of data-related cumulative number of confirmed, recovered, and deaths cases. we are going to prepare this dataset to answer these questions: How does Global Spread of the virus look like? How intensive the spread of the virus has been in the countries? Does covid19 national lockdowns and self-isolations in different countries have actually impact on COVID19 transmission? we are going to use Plotly module, which is a great visualization tool in python, in order to plot some insightful and intuitive graphs to answer the questions.

# ## Loading libaries and dataset

# In[1]:


pip install plotly==4.10.0


# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import time


# In[3]:


# Data urls
dataset_url ="https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"
df = pd.read_csv(dataset_url)
df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# ## Visualizing Global Spread of COVID-19 from first day of the Pandemic
# 
# Using Choropleth map to Visualize Global Spread of COVID-19 from the first day of the pandemic

# In[6]:


df = df[df.Confirmed > 0]


# In[7]:


df.head()


# In[8]:


df[df.Country == "Australia"].tail()


# In[9]:


fig = px.choropleth(df, locations = "Country", locationmode="country names", color = "Confirmed", 
                    animation_frame = "Date")
fig.update_layout(title_text = "Global spread of COVID19")
fig.show()


# In[10]:


fig = px.choropleth(df, locations = "Country", locationmode="country names", color = "Deaths", 
                    animation_frame = "Date")
fig.update_layout(title_text = "Global spread of COVID19")
fig.show()


# ## Visualizing how intensive the Covid19 Transmission has been in each country
# 
# Using a Bar chart to compare different countries in terms of How massive the Spread of the virus has been in there.

# In[11]:


df_china = df[df.Country == "China"]
df_china.head()


# In[12]:


df_china = df_china[['Date','Confirmed']]
df_china.head()


# In[13]:


df_china['Infection rate'] = df_china['Confirmed'].diff()
df_china.head()


# In[14]:


px.line(df_china, x = 'Date', y=['Infection rate','Confirmed'])


# In[15]:


df_china['Infection rate'].max()


# In[16]:


countries = list(df['Country'].unique())
max_infection_rates = []
for c in countries:
    MIR = df[df.Country == c].Confirmed.diff().max()
    max_infection_rates.append(MIR)


# In[17]:


df_MIR = pd.DataFrame()
df_MIR['Country'] = countries
df_MIR['Max Infection Rate'] = max_infection_rates
df_MIR.head()


# In[18]:


px.bar(df_MIR, x='Country', y='Max Infection Rate', color ='Country', 
       title = 'Global Maximum Infection Rate', log_y=True)


# ## National Lockdown Impacts COVID 19 transmission in different countries

# ### COVID19 spread before and after lockdown in Italy
# Visualizing the impact of the national lockdown in Italy on the spread of the virus.

# In[19]:


df.head()


# In[20]:


italy_lockdown_start_date = '2020-03-09'
italy_lockdown_a_month_later = '2020-04-09'


# In[21]:


df_italy = df[df.Country == 'Italy']


# In[22]:


df_italy.head()


# In[23]:


df_italy['Daily Caese'] = df_italy.Confirmed[]


# In[24]:


df_italy['Infection Rate'] = df_italy.Confirmed.diff()
df_italy.head()


# In[25]:


fig = px.line(df_italy, x = 'Date', y = 'Infection Rate', 
              title = 'Before and After Lockdown in Italy')
fig.add_shape(
    dict(
    type = 'line',
    x0 = italy_lockdown_start_date,
    y0 = 0,
    x1 = italy_lockdown_start_date,
    y1 = df_italy['Infection Rate'].max(),
    line = dict(color='red',width = 2)
    )
)

fig.add_annotation(
    dict(
    x= italy_lockdown_start_date,
    y= df_italy['Infection Rate'].max(),
    text = 'starting date of the lockdown'
    )
)

fig.add_shape(
    dict(
    type = "line",
    x0 = italy_lockdown_a_month_later,
    y0 = 0,
    x1 = italy_lockdown_a_month_later,
    y1 = df_italy['Infection Rate'].max(),
    line = dict(color='orange',width = 3)
    )
)

fig.add_annotation(
    dict(
    x= italy_lockdown_a_month_later,
    y= 0,
    text = 'Ending date of the lockdown'
    )
)


# ## Deaths Rate Before and After national Lockdown in Italy
# Visualizing the impact of the national lockdown in Italy on the death rate.

# In[26]:


df_italy.head()


# In[27]:


df_italy['Deaths Rate'] = df_italy.Deaths.diff()


# In[28]:


df_italy.head()


# In[29]:


fig = px.line(df_italy,x='Date', y=['Infection Rate', 'Deaths Rate'])
fig.show()


# Let's normalise the columns.

# In[30]:


df_italy['Infection Rate'] = df_italy['Infection Rate']/df_italy['Infection Rate'].max()
df_italy['Deaths Rate'] = df_italy['Deaths Rate']/df_italy['Deaths Rate'].max()


# In[31]:


fig = px.line(df_italy, x = 'Date', y=['Infection Rate','Deaths Rate'])
fig.add_shape(
    dict(
    type = 'line',
    x0 = italy_lockdown_start_date,
    y0 = 0,
    x1 = italy_lockdown_start_date,
    y1 = df_italy['Infection Rate'].max(),
    line = dict(color='black',width = 2)
    )
)

fig.add_annotation(
    dict(
    x= italy_lockdown_start_date,
    y= df_italy['Infection Rate'].max(),
    text = 'starting date of the lockdown'
    )
)

fig.add_shape(
    dict(
    type = "line",
    x0 = italy_lockdown_a_month_later,
    y0 = 0,
    x1 = italy_lockdown_a_month_later,
    y1 = df_italy['Infection Rate'].max(),
    line = dict(color='orange',width = 3)
    )
)

fig.add_annotation(
    dict(
    x= italy_lockdown_a_month_later,
    y= 0.95,
    text = 'Ending date of the lockdown'
    )
)


# ## COVID19 spread before and after lockdown in Australia
# Visualizing the impact of the national lockdown in Australia on the spread of the virus.

# In[49]:


aus_lockdown_start_date = '2020-03-23'
aus_lockdown_a_month_later = '2020-04-26'
vic_lockdown_start_date = '2020-08-01'
vic_lockdown_end_date ='2020-10-27'


# In[50]:


df_aus = df[df.Country == 'Australia']
df_aus.head()


# In[51]:


df_aus['Infection Rate'] = df_aus.Confirmed.diff()
df_aus.head()


# In[52]:


fig = px.line(df_aus,x='Date', y=['Infection Rate', 'Confirmed','Deaths'])
fig.show()


# In[53]:


df_aus[['Date','Confirmed']]
fig = px.line(df_aus, x='Date', y='Deaths', title = 'The number of death due to COVID19 in Australia')
fig.show()


# In[54]:


fig = px.line(df_aus, x= 'Date', y = 'Infection Rate', title = 'Before and after lockdown in Australia')
fig.add_shape(
    dict(
    type = "line",
    x0 = aus_lockdown_start_date,
    y0 = 0,
    x1 = aus_lockdown_start_date,
    y1 = df_aus['Infection Rate'].max(),
    line = dict(color='red',width = 2)
    )
)

fig.add_annotation(
    dict(
    x= aus_lockdown_start_date,
    y= df_aus['Infection Rate'].max(),
    text = 'starting date of the national lockdown'
    )
)
fig.add_shape(
    dict(
    type = "line",
    x0 = aus_lockdown_a_month_later,
    y0 = 0,
    x1 = aus_lockdown_a_month_later,
    y1 = df_aus['Infection Rate'].max(),
    line = dict(color='orange',width = 2)
    )
)

fig.add_annotation(
    dict(
    x= aus_lockdown_a_month_later,
    y= 500,
    text = 'ending date of the national lockdown'
    )
)
fig.add_shape(
    dict(
    type = "line",
    x0 = vic_lockdown_start_date ,
    y0 = 0,
    x1 = vic_lockdown_start_date,
    y1 = df_aus['Infection Rate'].max(),
    line = dict(color='red',width = 2)
    )
)

fig.add_annotation(
    dict(
    x= vic_lockdown_start_date,
    y= df_aus['Infection Rate'].max(),
    text = 'starting date of the vic stage 3 lockdown'
    )
)
fig.add_shape(
    dict(
    type = "line",
    x0 = vic_lockdown_end_date,
    y0 = 0,
    x1 = vic_lockdown_end_date,
    y1 = df_aus['Infection Rate'].max(),
    line = dict(color='orange',width = 2)
    )
)

fig.add_annotation(
    dict(
    x= vic_lockdown_end_date,
    y= 680,
    text = 'ending date of the vic stage 4 lockdown'
    )
)


# ## Deaths Rate Before and After Lockdown in Australia
# Visualizing the impact of the national lockdown in Australia on the death rate.

# In[55]:


df_aus.head()


# In[56]:


df_aus['Deaths Rate'] = df_aus.Deaths.diff()
df.head()


# Normalise the Infection rate and Deaths rate

# In[58]:


df_aus['Infection Rate'] = df_aus['Infection Rate']/df_aus['Infection Rate'].max()
df_aus['Deaths Rate'] = df_aus['Deaths Rate']/df_aus['Deaths Rate'].max()
fig = px.line(df_aus,x='Date', y=['Infection Rate','Deaths Rate'], title = 'Before and After lockdown in Australia')
fig.add_shape(
    dict(
    type = "line",
    x0 = aus_lockdown_start_date,
    y0 = 0,
    x1 = aus_lockdown_start_date,
    y1 = df_aus['Infection Rate'].max(),
    line = dict(color='Green',width = 2)
    )
)

fig.add_annotation(
    dict(
    x= aus_lockdown_start_date,
    y= df_aus['Infection Rate'].max(),
    text = 'starting date of the national lockdown'
    )
)
fig.add_shape(
    dict(
    type = "line",
    x0 = aus_lockdown_a_month_later,
    y0 = 0,
    x1 = aus_lockdown_a_month_later,
    y1 = df_aus['Infection Rate'].max(),
    line = dict(color='orange',width = 2)
    )
)

fig.add_annotation(
    dict(
    x= aus_lockdown_a_month_later,
    y= 0.95,
    text = 'ending date of the national lockdown'
    )
)
fig.add_shape(
    dict(
    type = "line",
    x0 = vic_lockdown_start_date ,
    y0 = 0,
    x1 = vic_lockdown_start_date,
    y1 = df_aus['Infection Rate'].max(),
    line = dict(color='Green',width = 2)
    )
)

fig.add_annotation(
    dict(
    x= vic_lockdown_start_date,
    y= df_aus['Infection Rate'].max(),
    text = 'starting date of the vic stage 3 lockdown'
    )
)
fig.add_shape(
    dict(
    type = "line",
    x0 = vic_lockdown_end_date,
    y0 = 0,
    x1 = vic_lockdown_end_date,
    y1 = df_aus['Infection Rate'].max(),
    line = dict(color='orange',width = 2)
    )
)

fig.add_annotation(
    dict(
    x= vic_lockdown_end_date,
    y= 0.95,
    text = 'ending date of the vic stage 4 lockdown'
    )
)


# In[ ]:




