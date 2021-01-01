#!/usr/bin/env python
# coding: utf-8

# In[3]:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
#%matplotlib inline


# In[4]:
data=pd.read_csv("train.csv")
#data_test=pd.read_csv("test.csv")
data.head()


# In[6]:
label = data['label']
print(label)


# In[7]:


#drop the label feature and store data in d
d= data.drop("label", axis=1)


# In[8]:


print(d.shape)


# In[11]:


print(label.shape)


# In[20]:


plt.figure(figsize = (7,7))
idx=130

grid_data=d.iloc[idx].to_numpy().reshape(28,28)
plt.imshow(grid_data, interpolation= "none", cmap="Greys")
plt.show()

print(label[idx])


# In[ ]:




