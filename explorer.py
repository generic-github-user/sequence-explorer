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

class Sequence:
    def __init__(self, terms=None, rule=None):
        if not terms:
            self.terms = []
        self.terms = terms
        self.rule = rule
        
    def __iadd__(self, a):
        self.terms.append(a)

class Rule:
    def __init__(self, conditions=[], symbols=default_symbols):
        self.conditions = conditions
        self.symbols = symbols
    
    def sample(self, length=10):
        seq = []
        seq += random.choice(self.symbols)
        for i in range(length-1):
            possible = list(filter(lambda s: all([c(lstr(seq)+s) for c in self.conditions]), self.symbols))
            seq += random.choice(possible)
        return seq
