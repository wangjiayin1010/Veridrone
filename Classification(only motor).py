
# coding: utf-8

# In[84]:

f1 = open("training.csv",'r')
f2 = open("testing.csv", 'r')


# In[85]:

import numpy as np


# In[86]:

data1 =  np.loadtxt(fname = f1, delimiter = ',',usecols=(8,9,10,11,3))


# In[87]:

x1 =  data1[:,0:4]
print(x1)


# In[88]:

y1 = data1[:,4]


# In[89]:

print(y1)


# In[90]:

from sklearn import svm


# In[91]:

clf_svm = svm.SVC(C=30000) # clf: SVM


# In[92]:

clf_svm.fit(x1, y1)


# In[93]:

data2 =  np.loadtxt(fname = f2, delimiter = ',',usecols=(8,9,10,11,3))


# In[94]:

x2 =  data2[:,0:4]
print(x2)


# In[95]:

y2 = data2[:,4]


# In[96]:

predict = clf_svm.predict(x2)
print(predict)


# In[97]:

correct = 0
for i in range(0, len(predict)):
    if (predict[i] == y2[i]):
        correct = correct+1


# In[98]:

print(correct/len(predict)) # correct rate for SVM


# In[99]:

print(len(predict))


# In[66]:

from sklearn import neighbors
clf2 = neighbors.KNeighborsClassifier(5, weights='distance') # clf2: k nearest neighbours


# In[67]:

clf2.fit(x1,y1)


# In[68]:

predict2 = clf2.predict(x2)


# In[69]:

correct2 = 0
for i in range(0, len(predict2)):
    if (predict2[i] == y2[i]):
        correct2 = correct2+1


# In[70]:

print(correct2/len(predict2)) # correct rate for k nearest neighbours


# In[71]:

from sklearn.linear_model import LogisticRegression


# In[72]:

clf_LR = LogisticRegression(C=1000)


# In[73]:

clf_LR.fit(x1,y1)


# In[74]:

predict_LR = clf_LR.predict(x2)


# In[75]:

correct3 = 0
for i in range(0, len(predict_LR)):
    if (predict_LR[i] == y2[i]):
        correct3 = correct3+1


# In[76]:

print(correct3/len(predict_LR)) # correct rate for logistic regression


# In[77]:

from sklearn import tree
clf_tree = tree.DecisionTreeClassifier()
clf_tree.fit(x1,y1)


# In[78]:

predict_tree = clf_tree.predict(x2)


# In[79]:

correct4 = 0
for i in range(0, len(predict_tree)):
    if (predict_tree[i] == y2[i]):
        correct4 = correct4+1


# In[80]:

print(correct4/len(predict_tree)) # correct rate for decision tree


# In[ ]:



