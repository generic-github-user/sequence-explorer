#!/usr/bin/env python
# coding: utf-8

# In[11]:


get_ipython().run_line_magic('matplotlib', 'widget')

import numpy as np
import matplotlib.pyplot as plt
import string
import random


# In[60]:


fig.clear()


# In[61]:


default_symbols = list(string.ascii_uppercase[:5])
def lstr(x):
    return ''.join(x)

class Sequence:
    def __init__(self, terms=None, rule=None):
        if terms is None:
            terms = []
        self.terms = terms
        self.rule = rule
        
    def __iadd__(self, a):
        self.terms.append(a)
        return self
        
    def __str__(self):
        return ''.join(self.terms)

    def __iter__(self):
        return iter(self.terms)
    
class Rule:
    def __init__(self, conditions=[], symbols=default_symbols):
        self.conditions = conditions
        self.symbols = symbols
    
    def sample(self, length=10):
        seq = Sequence()
        seq += random.choice(self.symbols)
        for i in range(length-1):
            possible = list(filter(lambda s: all([c(str(seq)+s) for c in self.conditions]), self.symbols))
            seq += random.choice(possible)
        return seq

fig, ax = plt.subplots()
R = Rule(
    [lambda p: p[-1]!=p[-2]]
)
test = R.sample()
test = np.expand_dims([R.symbols.index(c) for c in test], 0)
im = ax.imshow(test, cmap='inferno')

indices = list(range(1, 11))
ax.set_xticks(np.arange(len(indices)))
# ax.set_yticks(np.arange(len()))
ax.set_xticklabels(indices)
# ax.set_yticklabels()

plt.setp(ax.get_xticklabels(), rotation=0, ha="right",
         rotation_mode="anchor")

for i in range(len([0])):
    for j in range(len(farmers)):
        text = ax.text(j, i, test[i, j], ha="center", va="center", color="w")

ax.set_title('')
# fig.tight_layout()
plt.show()


# In[ ]:




