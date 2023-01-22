#!/usr/bin/env python
# coding: utf-8

# # Plotting with `seaborn`

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[2]:


tips = sns.load_dataset('tips')


# In[3]:


penguins = sns.load_dataset('penguins')


# In[4]:


titanic = sns.load_dataset('titanic')


# In[5]:


sns.countplot(titanic['sex'], hue = titanic['survived'])


# In[58]:


#seaborn has a special plot for counts
sns.countplot(titanic['survived'])
#titanic['survived'].value_counts().plot(kind = 'bar')


# In[59]:


penguins.head()


# In[84]:


sns.boxplot(x = penguins['species'], y = penguins['flipper_length_mm'])
plt.title('Penguins by Species and Distribution of Bill Length')
plt.xlabel('Species of Penguin');


# In[68]:


penguins.info()


# In[72]:


sns.scatterplot(penguins['bill_length_mm'], penguins['bill_depth_mm']);


# In[80]:


penguins = penguins.dropna()


# In[83]:


sns.pairplot(penguins, hue = 'island')


# In[26]:


titanic.head(1)


# In[19]:


#Histogram of ages on the titanic 
#with appropriate title and x axis labels.
plt.hist(titanic['age']);
plt.title('Ages on the Titanic')
plt.xlabel('Ages');


# In[28]:


titanic.head(1)


# In[31]:


titanic['class'].value_counts()


# In[32]:


#Barplot of counts of passengers by class on titanic.
titanic['pclass'].value_counts().plot(kind = 'bar');


# In[9]:


#Boxplots of penguins


# In[45]:


penguins.head(1)


# In[46]:


penguins['species'].unique()


# In[49]:


colors = []
#write a loop -- loop over the species
#if Adelie -- blue
#if Chinstrap -- yellow
#if Gentoo -- red
for species in penguins['species']:
    #test if Adelie
    if species == 'Adelie':
        colors.append('blue')
    #test if Chinstrap
    elif species == 'Chinstrap':
        colors.append('yellow')
    #test if Gentoo
    else:
        colors.append('red')

#Scatterplot of penguins
plt.scatter(penguins['bill_length_mm'], penguins['bill_depth_mm'], 
            c = colors)


# In[39]:


#barplot for survival
titanic['survived'].value_counts().plot(kind = 'bar')


# In[41]:


survival_counts = titanic['survived'].value_counts()


# In[44]:


plt.bar([0, 1], survival_counts);


# In[12]:


#histograms of flipper lengths


# In[ ]:





# In[ ]:





# In[ ]:





# In[5]:


sns.boxplot(x = 'island', y = 'bill_length_mm', data = penguins);


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[3]:


tips.head()


# In[4]:


sns.stripplot('total_bill', data = tips)


# In[5]:


iris = sns.load_dataset("iris")
sns.catplot(data=iris, orient="h", kind="box");


# In[6]:


sns.catplot(x="day", y="total_bill", hue="smoker",
            col="time", aspect=.6,
            kind="swarm", data=tips);


# In[7]:


titanic = sns.load_dataset("titanic")
sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic);


# In[8]:


from bokeh.plotting import figure 
from bokeh.io import output_notebook, show


# In[9]:


output_notebook()


# In[10]:


x = [1, 2, 3, 4, 5]
y = [4, 2, 5, 6, 2]


# In[11]:


p = figure(width = 600, height = 300)
p.circle(x, y)
show(p)


# In[12]:


p = figure(width = 600, height = 300)
p.circle(x, y,  color = 'red', size = 10, alpha = 0.5)
show(p)


# In[13]:


p = figure(width = 600, height = 400)
p.vbar(x= [0,0.5, 1], bottom = [0, 1, 1], top = [4, 3, 2], width = 0.2)
show(p)


# ### From a DataFrame

# In[14]:


df = pd.read_csv('data/happiness/2015.csv')


# In[15]:


df.head(2)


# In[16]:


from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot
source = ColumnDataSource(df)


p1 = figure(title="Happiness and Economy", width = 600, height = 300)
p1.circle("Happiness Score", "Economy (GDP per Capita)", color="firebrick", size = 10,
          alpha = 0.5, 
          source=source)
p1.xaxis[0].axis_label = "Happiness Score"
p1.yaxis[0].axis_label = "GDP per Capita"

show(p1)


# In[ ]:




