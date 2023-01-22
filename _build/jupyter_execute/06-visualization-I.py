#!/usr/bin/env python
# coding: utf-8

# # Plotting with `Matplotlib`
# 
# 

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[2]:


#define some points


# In[3]:


#a basic plot


# In[4]:


#add a title


# In[5]:


#change the color and marker


# In[6]:


#add x and y labels


# In[7]:


import pandas as pd


# ## Basic Plots
# 
# - Histogram: one continuous set of values
# - Line Plot: two continuous values
# - Bar Plot: counts of categories
# - Scatter Plot: two continuous values
# - Boxplot: one continuous value

# In[8]:


import seaborn as sns


# In[9]:


titanic = sns.load_dataset('titanic')
penguins = sns.load_dataset('penguins')


# In[10]:


#titanic time


# In[11]:


#age vs. fare


# In[12]:


#counts per class


# In[13]:


#fare vs. age


# In[14]:


#boxplot of survivals by age


# ### Using Seaborn

# In[15]:


#scatterplot


# In[16]:


#distplot


# In[17]:


#countplot


# In[18]:


#boxplot


# In[19]:


#swarmplot


# ### `.groupby`

# In[20]:


#group by gender


# In[21]:


#group by island


# In[22]:


#group by island and species


# In[23]:


#group by age


# In[24]:


#multiple summaries


# ### Subplots

# In[25]:


#single subplot


# In[26]:


#two columns 


# In[27]:


#two rows


# In[28]:


#two rows two columns


# ### Saving and Displaying Figures

# In[29]:


#same image


# In[30]:


#view in markdown cell

