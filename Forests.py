#Jasmine Simmons
#Feb. 28 2017

#Testing Forests of Randomized Trees

f = open("trial02.csv", 'r')

import numpy as np

data = np.loadtxt(fname = f, delimiter = ',')

X = data[:, 0:2]
Y = data[:, 2]


from sklearn.ensemble import RandomForestClassifier
#X = [[0, 0], [1, 1]]
#Y = [0, 1]

clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(X, Y)
clf.predict([[50, -0.5]])

p = data[:, 3:5]

x = clf.predict(p)
print (x)


correct = data[:,5]
print (correct)

