#!/usr/bin/env python
# coding: utf-8

# In[11]:


get_ipython().run_line_magic('matplotlib', 'widget')

import numpy as np
import matplotlib.pyplot as plt
import string
import random


# In[69]:


fig.clear()
plt.close(fig)


# In[83]:


plt.close('all')

default_symbols = list(string.ascii_uppercase[:5])
def lstr(x):
    return ''.join(x)

class Sequence:
    def __init__(self, terms=None, rule=None):
        if terms is None:
            terms = []
        self.terms = terms
        self.rule = rule
    
    def display(self):
        vals = np.expand_dims([self.rule.symbols.index(c) for c in self], 0)
        fig, ax = plt.subplots()
        im = ax.imshow(vals, cmap='cool')

        num_terms = len(self)
        indices = list(range(1, num_terms+1))
        ax.set_xticks(np.arange(num_terms))
        # ax.set_yticks(np.arange(len()))
        ax.set_xticklabels(indices)
        # ax.set_yticklabels()

        plt.setp(ax.get_xticklabels(), rotation=0, ha="right",
                 rotation_mode="anchor")

        for i in range(len([0])):
            for j in range(num_terms):
                text = ax.text(j, i, vals[i, j], ha="center", va="center", color="w")

        ax.set_title('')
        # fig.tight_layout()
        plt.show()
    
    def __iadd__(self, a):
        self.terms.append(a)
        return self
        
    def __str__(self):
        return ''.join(self.terms)

    def __iter__(self):
        return iter(self.terms)
    
    def __getitem__(self, i):
        return self.terms[i]
    
    def __len__(self):
        return len(self.terms)
    
class Rule:
    def __init__(self, conditions=[], symbols=default_symbols):
        self.conditions = conditions
        self.symbols = symbols
    
    def sample(self, length=10):
        seq = Sequence(rule=self)
        seq += random.choice(self.symbols)
        for i in range(length-1):
            possible = list(filter(lambda s: all([c(str(seq)+s) for c in self.conditions]), self.symbols))
            seq += random.choice(possible)
        return seq

# Sequence of non-consecutive identical/repeated symbols
R = Rule([lambda p: p[-1]!=p[-2]])
R.sample(15).display()


# In[ ]:




