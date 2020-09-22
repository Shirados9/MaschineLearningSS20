#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv('../../data/pctdata.csv')


# ## Comments
# 
# * point
# * point

# In[ ]:


df.info()


# In[ ]:


df['id_plane'].unique()


# In[ ]:


df['id_x'].hist(bins=100)
df['id_y'].hist(bins=100)
plt.show()


# ## Duplicates
# 
# Afterimage. The electronic and the chip is kind of slow discharge
# of charge.
# 
# ## Time Line
# 
# What is going on there.
# 
# ## Try to cluster events by means of
# 
# * KNN
# * DBSCAN
# * OPTICS
# * etc. etc.
# 
# ## 3D Scatter Plot

# In[ ]:


df.describe()


# ## Try to prove that 'id_plane' consists only of [0, 1, 2]

# In[ ]:


# type(df[['id_plane']])
# type(df)
df['id_plane'].unique()


# ## Try to plot the time line 'i_time_stamp'

# In[ ]:


df['i_time_stamp'].plot(kind='line')
plt.show()


# ## Intend to show a 2D Scatter Plot of plane 0

# In[ ]:


df_0 = df[df['id_plane'] == 0]
print('Length of df = ', len(df))
print('Length of df_0 = ', len(df_0))
df_0.plot.scatter(x='id_x', y='id_y', s=2)
plt.show()


# In[ ]:


get_ipython().run_line_magic('pinfo', 'df_0.plot.scatter')

