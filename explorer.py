#!/usr/bin/env python
# coding: utf-8

# In[197]:


get_ipython().run_line_magic('matplotlib', 'widget')

import numpy as np
import matplotlib.pyplot as plt
import string
import random
import math


# In[69]:


fig.clear()
plt.close(fig)


# In[256]:


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
        if vals.size > 30:
            w = math.floor(vals.size ** (1/2))
            q = vals.size / w
            q = math.ceil(q)
            vals = np.pad(vals, ((0, 0), (0, q*w-vals.size),), mode='constant')
            vals = vals.reshape([q, w])
        fig, ax = plt.subplots()
        im = ax.imshow(vals, cmap='cool')

#         num_terms = len(self)
        num_terms = vals.shape[-1]
        indices = list(range(1, num_terms+1))
        ax.set_xticks(np.arange(num_terms))
#         ax.set_xticks([])
        # ax.set_yticks(np.arange(len()))
        ax.set_xticklabels(indices)
        # ax.set_yticklabels()

        plt.setp(ax.get_xticklabels(), rotation=0, ha="right",
                 rotation_mode="anchor")

        if vals.size <= 30:
            col = 'black'
            for i in range(len([0])):
                for j in range(num_terms):
                    box = dict(boxstyle="round", ec=col, fc=col, alpha=0.5)
                    text = ax.text(j, i, self.terms[j], ha="center", va="center", color="w", bbox=box)

        ax.set_title('')
        # fig.tight_layout()
#         plt.axis('off')
        plt.gca().axes.get_yaxis().set_visible(False)
        ax.set_frame_on(False)
        plt.show()
    
    def print(self):
        print(self)
    
    def __iadd__(self, a):
        self.terms.append(a)
        return self
        
    def __str__(self):
        return ''.join(map(str, self.terms))

    def __iter__(self):
        return iter(self.terms)
    
    def __getitem__(self, i):
        return self.terms[i]
    
    def __len__(self):
        return len(self.terms)

class SequenceSet:
    def __init__(self, members):
        self.members = members
    
    def display(self):
        self.members[0].display()
    
    def print(self):
        print(self)
        
    def __str__(self):
        return '\n'.join(map(str, self.members))
    
    def __iadd__(self, a):
        self.members.append(a)
        return self
    
class Rule:
    def __init__(self, conditions=[], symbols=default_symbols):
        self.conditions = conditions
        self.symbols = symbols
    
    def sample(self, length=10, n=1):
        seq_set = SequenceSet([])
        for m in range(n):
            seq = Sequence(rule=self)
            seq += random.choice(self.symbols)
            for i in range(length-1):
                possible = list(filter(lambda s: all([c(str(seq)+s) for c in self.conditions]), self.symbols))
                if possible:
                    seq += random.choice(possible)
            seq_set += seq
        return seq_set

# Sequence of non-consecutive identical/repeated symbols
R = Rule([lambda p: p[-1]!=p[-2]])
# R.sample(5).display()

# Sequence of symbols that cannot occur more than twice in a span of 10 tokens
R = Rule([lambda p: p[-28:-1].count(p[-1])<=2])
R.sample(50, 5).print()


# In[ ]:




