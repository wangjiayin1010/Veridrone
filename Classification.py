
# coding: utf-8

# In[ ]:

f1 = open("training.csv",'r')


# In[ ]:

f2 = open("testing.csv", 'r')


# In[ ]:

import numpy as np


# In[ ]:

data1 =  np.loadtxt(fname = f1, delimiter = ',',usecols=(2,5,7,8,9,10,3))


# In[ ]:

x1 =  data1[:,0:6]


# In[ ]:

y1 = data1[:,6]


# In[ ]:

print(y1)


# In[ ]:

from sklearn import svm


# In[ ]:

clf = svm.SVC(C=3000, kernel='linear') # clf: SVM


# In[ ]:

clf.fit(x1, y1)


# In[ ]:

data2 =  np.loadtxt(fname = f2, delimiter = ',',usecols=(2,5,7,8,9,10,3))


# In[ ]:

x2 =  data2[:,0:6]


# In[ ]:

y2 = data2[:,6]


# In[ ]:

predict = clf.predict(x2)


# In[ ]:

print(predict)


# In[ ]:

correct = 0
for i in range(0, len(predict)):
    if (predict[i] == y2[i]):
        correct = correct+1


# In[ ]:

print(correct/len(predict)) # correct rate for SVM


# In[54]:

print(len(predict))


# In[139]:

print(predict[3209]==y2[3209])


# In[4]:

from sklearn import neighbors


# In[21]:

clf2 = neighbors.KNeighborsClassifier(5, weights='distance') # clf2: k nearest neighbours


# In[22]:

clf2.fit(x1,y1)


# In[23]:

predict2 = clf2.predict(x2)


# In[24]:

correct2 = 0
for i in range(0, len(predict2)):
    if (predict2[i] == y2[i]):
        correct2 = correct2+1


# In[25]:

print(correct2/len(predict2)) # correct rate for k nearest neighbours


# In[26]:

from sklearn.linear_model import LogisticRegression


# In[27]:

clf_LR = LogisticRegression(C=1000)


# In[28]:

clf_LR.fit(x1,y1)


# In[29]:

predict_LR = clf_LR.predict(x2)


# In[30]:

correct3 = 0
for i in range(0, len(predict_LR)):
    if (predict_LR[i] == y2[i]):
        correct3 = correct3+1


# In[31]:

print(correct3/len(predict_LR)) # correct rate for k nearest neighbours


# In[ ]:



