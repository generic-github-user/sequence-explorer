#!/usr/bin/env python
# coding: utf-8

# In[11]:


get_ipython().run_line_magic('matplotlib', 'widget')

import numpy as np
import matplotlib.pyplot as plt
import string
import random


# In[46]:


fig.clear()


# In[51]:


default_symbols = list(string.ascii_uppercase[:5])
def lstr(x):
    return ''.join(x)

class Rule:
    def __init__(self, conditions=[], symbols=default_symbols):
        self.conditions = conditions
        self.symbols = symbols
