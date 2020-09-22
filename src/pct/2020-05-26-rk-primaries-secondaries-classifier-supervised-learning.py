#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

# show all columns and rows:
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# ## Read Data from Filesystem

# In[ ]:


PATH = '../../data/2020-02-04_18-30_Proton_230MeV_Head-Phantom.csv'
df = pd.read_csv(PATH, nrows=5000)
# df = pd.read_csv(PATH)


# Look into content:

# In[ ]:


df.head()


# Calculate the number of hits induced by primaries and hits induced
# by secondaries. I assume the $'parentID' == 0$ stands for a primary
# hit and $'parentID' != 0$ stands for a secondary hit.

# In[ ]:


hits_primary = len(df[df['parentID'] == 0])
hits_secondary = len(df[df['parentID'] != 0])

print('number of primary hits =', hits_primary)
print('number of secondary hits =', hits_secondary)


# Show primaries and secondaries in different colors in a 3D plot.
# I will choose ```plotly``` for this purpose.

# In[ ]:


# Proof of plotly.express
import plotly.express as px
df_example = px.data.election()
fig = px.scatter_3d(df_example, x="Joly", y="Coderre", z="Bergeron", color="winner", size="total", hover_name="district",
                  symbol="result", color_discrete_map = {"Joly": "blue", "Bergeron": "green", "Coderre":"red"})
fig.show()


# In[ ]:


df['isPrimary'] = df['parentID'] == 0


# “IEEE2020Summary.Pdf.” n.d.

# In[ ]:


def get_cluster_size(energy_deposition):
    return 2.4 * energy_deposition ** 0.338


# In[ ]:


df['cluster_size'] = df['edep'].apply(get_cluster_size)


# In[ ]:


fig = px.histogram(df, x='cluster_size')
fig.show()


# In[ ]:


fig = px.scatter_3d(df, x="posX", y="posY", z="posZ", color="isPrimary", size="cluster_size", opacity=0.5)
fig.show()


# In[ ]:




