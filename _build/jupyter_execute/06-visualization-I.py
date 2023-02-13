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


# ## Basic Plots
# 
# - Histogram: one continuous set of values
# - Line Plot: two continuous values
# - Bar Plot: counts of categories
# - Scatter Plot: two continuous values
# - Boxplot: one continuous value

# In[7]:


import seaborn as sns


# In[8]:


titanic = sns.load_dataset('titanic')
penguins = sns.load_dataset('penguins')


# In[9]:


#titanic time


# In[10]:


#age vs. fare


# In[11]:


#counts per class


# In[12]:


#fare vs. age


# In[13]:


#boxplot of survivals by age


# ### Using Seaborn

# In[14]:


#scatterplot


# In[15]:


#distplot


# In[16]:


#countplot


# In[17]:


#boxplot


# In[18]:


#swarmplot


# ### `.groupby`

# In[19]:


#group by gender


# In[20]:


#group by island


# In[21]:


#group by island and species


# In[22]:


#group by age


# In[23]:


#multiple summaries


# ### Subplots

# In[24]:


#single subplot


# In[25]:


#two columns 


# In[26]:


#two rows


# In[27]:


#two rows two columns


# ### Saving and Displaying Figures

# In[28]:


#same image


# In[29]:


#view in markdown cell

