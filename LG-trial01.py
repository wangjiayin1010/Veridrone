
# coding: utf-8

# In[12]:

f = open("trial02.csv", 'r')


# In[13]:

import numpy as np


# In[14]:

data =  np.loadtxt(fname = f, delimiter = ',')


# In[23]:

# X are features, which are altitudes and their delta; Y is either 1 or 0
X = data[:, 0:2]
y = data[:, 2]


# In[16]:

from sklearn import linear_model


# In[17]:

clf = linear_model.LogisticRegression(C=300)


# In[18]:

clf.fit(X, y)  


# In[19]:

clf.predict([[50,-0.05]])


# In[20]:

p = data[:, 3:5]


# In[21]:

clf.predict(p)


# In[22]:

# print out the correct value
correct = data[:,5]
print (correct)


# In[ ]:



