#!/usr/bin/env python
# coding: utf-8

# ### Make a Map

# **OBJECTIVES**:
# 
# - Make markers with popups
# - Make a choropleth
# - Make a heatmap
# - Make a heatmap with time

# In[1]:


import folium
import pandas as pd
import numpy as np


# In[2]:


sat = pd.read_csv('data/sat_2017.csv')


# In[3]:


sat.head()


# In[4]:


sat.info()


# In[6]:


sat['Participation'] = sat['Participation'].str.replace('%', '').astype('float')


# In[27]:


#basic map
m = folium.Map(location = [39.8283, -98.5795], zoom_start = 4, style = 'Stamen Toner')


# In[28]:


m


# In[32]:


marker_1 = folium.Marker(location = [39.8283, -98.5795], 
                        popup = 'Welcome to the middle.')


# In[33]:


marker_1.add_to(m)


# In[34]:


m


# In[35]:


url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
state_geo = f'{url}/us-states.json'


# In[58]:


abbrevs = '''
Alabama - AL
Alaska - AK
Arizona - AZ
Arkansas - AR
California - CA
Colorado - CO
Connecticut - CT
Delaware - DE
Florida - FL
Georgia - GA
Hawaii - HI
Idaho - ID
Illinois - IL
Indiana - IN
Iowa - IA
Kansas - KS
Kentucky - KY
Louisiana - LA
Maine - ME
Maryland - MD
Massachusetts - MA
Michigan - MI
Minnesota - MN
Mississippi - MS
Missouri - MO
Montana - MT
Nebraska - NE
Nevada - NV
New Hampshire - NH
New Jersey - NJ
New Mexico - NM
New York - NY
North Carolina - NC
North Dakota - ND
Ohio - OH
Oklahoma - OK
Oregon - OR
Pennsylvania - PA
Rhode Island - RI
South Carolina - SC
South Dakota - SD
Tennessee - TN
Texas - TX
Utah - UT
Vermont - VT
Virginia - VA
Washington - WA
West Virginia - WV
Wisconsin - WI
Wyoming - WY
'''

states = [i.split('-') for i in abbrevs.split('\n')[1:-1]]

states_clean = [i[0].rstrip() for i in states]

abbrevs = [i[1].lstrip() for i in states]

state_dict = {s:a for s, a in zip(states_clean, abbrevs)}


# In[61]:


sat['State_A'] = sat['State'].map(state_dict)


# In[62]:


sat.head()


# In[63]:


folium.Choropleth(
    geo_data=state_geo, #the geo json data
    name='choropleth',  #the kind of thing 
    data=sat,    #this is the dataframe
    columns=['State_A', 'Participation'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='SAT Participation Rate'
).add_to(m)


# In[64]:


m


# In[65]:


import json


# In[67]:


import requests


# In[68]:


response = requests.get(state_geo)


# In[70]:


poly_dict = json.loads(response.text)


# In[78]:


poly_dict['features'][0]['properties']['name']


# In[80]:


#!conda install geopandas


# In[81]:


import geopandas as gpd


# In[83]:


# gdf = gpd.GeoDataFrame('data/nyc_bounds')


# ### COVID Map

# In[84]:


cdf = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/12-13-2020.csv')


# In[86]:


cdf.info()


# In[91]:


m = folium.Map(location = [39.8283, -98.5795], zoom_start = 5)

folium.Choropleth(
    geo_data=state_geo, #the geo json data
    name='choropleth',  #the kind of thing 
    data=cdf,    #this is the dataframe
    columns=['Province_State', 'Deaths'],
    key_on='feature.properties.name',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='COVID Death Counts'
).add_to(m)


# In[92]:


m


# In[106]:


from folium.plugins import HeatMap, HeatMapWithTime


# In[108]:


cov_death_time = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv')


# In[109]:


cov_death_time.head()


# ### Make a Heatmap

# In[94]:


cdf.head(4)


# In[104]:


m = folium.Map(location = [39.8283, -98.5795], zoom_start = 5)
HeatMap(cdf[['Lat', 'Long_', 'Deaths']].dropna(subset = ['Lat', 'Long_']), max_val = 0.5, max_zoom = 10).add_to(m)


# In[105]:


m


# In[ ]:




