#!/usr/bin/env python
# coding: utf-8

# * [https://www.w3resource.com/pandas/dataframe/dataframe-explode.php](https://www.w3resource.com/pandas/dataframe/dataframe-explode.php)
# * [https://stackoverflow.com/a/45846853](https://stackoverflow.com/a/45846853)
# * [https://stackoverflow.com/a/53218939](https://stackoverflow.com/a/53218939)
# 
# Before 'explode':

# In[ ]:


import pandas as pd

df = pd.DataFrame({'A': ['x1','x2','x3', 'x4'], 'B':[['v1','v2'],['v3','v4'],['v5','v6'],['v7','v8']], 'C':[['c1','c2'],['c3','c4'],['c5','c6'],['c7','c8']],'D':[['d1','d2'],['d3','d4'],['d5','d6'],['d7','d8']], 'E':[['e1','e2'],['e3','e4'],['e5','e6'],['e7','e8']]})
df


# After 'explode':

# In[ ]:


df_exploded = (df.set_index('A')
              .apply(lambda x: x.apply(pd.Series).stack())
              .reset_index()
              .drop('level_1', 1))
df_exploded


# Second approach:
# 
# [https://stackoverflow.com/a/53218939](https://stackoverflow.com/a/53218939)

# In[ ]:


df = pd.DataFrame({'A': ['x1','x2','x3', 'x4'],
                   'B':[['v1','v2'],['v3','v4'],['v5','v6'],['v7','v8']],
                   'C':[['c1','c2'],['c3','c4'],['c5','c6'],['c7','c8']],
                   'D':[['d1','d2'],['d3','d4'],['d5','d6'],['d7','d8']],
                   'E':[['e1','e2'],['e3','e4'],['e5','e6'],['e7','e8']],
                   'F': ['y1', 'y2', 'y3', 'y4']})


# In[ ]:


import numpy as np
def unnesting(df, explode):
    idx = df.index.repeat(df[explode[0]].str.len())
    df1 = pd.concat([
        pd.DataFrame({x: np.concatenate(df[x].values)}) for x in explode], axis=1)
    df1.index = idx

    return df1.join(df.drop(explode, 1), how='left').reset_index(drop=True)


# In[ ]:


unnesting(df,['B','C','D','E'])

