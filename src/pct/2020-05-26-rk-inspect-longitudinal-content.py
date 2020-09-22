#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


PATH = '../../data/Carbon-Data-ALPIDE-CHIP-Longitudinal/151218_04237.csv'

df = pd.read_csv(PATH,
                 converters={"column": lambda vol: vol.strip("[]").split(";"),
                             "row": lambda vol: vol.strip("[]").split(";") },
                 nrows=3000)


# In[ ]:


df.head(n=30)


# Making assumptions about
# 
# * 'ru_id' always being ```1```
# * 'stave_id' always being ```0```
# * 'chip_id' always being ```5```

# In[ ]:


assert df['ru_id'].unique() == 1
assert df['stave_id'].unique() == 0
assert df['chip_id'].unique() == 5


# Drop 'ru_id', 'stave_id' and 'chip_id' because they contain
# no useful information for our purposes

# In[ ]:


df.drop(['ru_id', 'stave_id', 'chip_id'], axis='columns', inplace=True)
df.head()


# Explode python lists in columns to row values...
# 
# [https://www.w3resource.com/pandas/dataframe/dataframe-explode.php](https://www.w3resource.com/pandas/dataframe/dataframe-explode.php)
# [https://stackoverflow.com/a/53218939](https://stackoverflow.com/a/53218939)

# In[ ]:


def unnesting(df, explode):
    idx = df.index.repeat(df[explode[0]].str.len())
    df1 = pd.concat([
        pd.DataFrame({x: np.concatenate(df[x].values)}) for x in explode], axis=1)
    df1.index = idx
    return df1.join(df.drop(explode, 1), how='left').reset_index(drop=True)


# In[ ]:


df = unnesting(df, ['column', 'row'])
df.head()


# The data are now 'tidy' and we can make scatter plots.

# In[ ]:


df_selection = df.iloc[:2000:, :]
type(df_selection)


# In[ ]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


plt.scatter(df_selection['column'], df_selection['row'])
plt.show()


# In[ ]:


df.describe()


# In[ ]:


df_frame_id = df[df['frame_id'] == 1.]


# In[ ]:


df_frame_id.describe()


# In[ ]:


plt.scatter(df_frame_id['column'], df_frame_id['row'])
plt.show()

