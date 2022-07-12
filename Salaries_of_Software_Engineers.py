#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
from IPython.display import Image
from wordcloud import WordCloud, STOPWORDS


# In[52]:


data_set=pd.read_csv(r"C:\Users\skkr1\OneDrive\Desktop\Software_Professional_Salaries.csv")
data_set.head()


# In[53]:


data_set.tail()


# In[54]:


data_set.info()
data_set.duplicated().sum()


# In[56]:


data_set.nunique()


# In[57]:


data.ndim


# In[44]:


salary=data[:500,3]
print('min_salary: {}'.format(salary.min()))
print('max_salary: {}'.format(salary.max()))
print('average_salary: {}'.format(salary.mean()))


# In[45]:


data_set.describe()


# In[46]:


data_set.isnull()


# In[47]:


pd.value_counts(data_set["Company Name"])


# In[48]:


jobs=data_set[["Company Name", "Job Title", "Salary"]]
jobs


# In[49]:


companies=data_set.groupby(["Company Name", "Salary","Location","Job Title"]).count()
companies


# In[58]:


companies.tail(10)


# # Location 

# In[132]:


plt.figure(figsize = (5, 5))
plt.ticklabel_format(style = 'plain')
sns.barplot(x = data_set["Salary"], y = data_set["Location"], palette = "terrain_r");


# In[138]:


top_cities= data_set.Location.head(5)
plt.figure(figsize = (5, 5))
plt.ticklabel_format(style = 'plain')
sns.barplot(x = data_set["Location"].head(6), y = data_set["Salary"].head(6), palette = "terrain_r");


# # Company

# In[95]:


plt.figure(figsize = (25, 10))
plt.xticks(rotation = 90)
plt.ticklabel_format(style = 'plain')
data_set.sort_values("Salary", axis = 0, ascending = False, inplace = True)
sns.barplot(x = data_set["Company Name"][1:51],
            y = data_set["Salary"][1:51],
            palette = "deep");


# In[98]:


data_set["Job Title"].value_counts()


# In[126]:


top_cities= data_set.Location.head(5)
plt.figure(figsize = (5, 5))
plt.ticklabel_format(style = 'plain')
sns.barplot(x = data_set["Location"], y = data_set["Salary"], palette = "terrain_r");


# In[139]:


plt.figure(figsize=(10,8))
data_set['Job Title'].value_counts().head(5).plot(kind='pie', autopct='%.0f%%', colormap="Set3")
plt.show()


# In[127]:


plt.figure(figsize=(10,8))
plt.title('Rating')
sns.histplot(data_set.Rating, palette="colors", bins=10)
plt.show()


# In[ ]:




