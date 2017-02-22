# File Name: decisionTree.py
# Author: Lichen (Brittany) Zhang
# Description: TODO
# Date: Feb 19 2017


from sklearn import tree 

from sklearn.datasets import load_iris

from sklearn import tree

import os

import pydotplus

from IPython.display import Image 

# DecisionTreeClassifier takes input two arrays
# array X holding the training samples
# array Y of integer values
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)


# construct a tree using the Iris dataset
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)


# once trained, export the tree in Graphviz format using export_graphviz exporter
# below is an example export of a tree trained on the entire iris dataset
with open("iris.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)
    
    
# use Graphviz's dot tool to create a PDF file (or any other supported file type)
os.unlink('iris.dot')


# alternatively, if have Python module pydotplus installed
# we can generate a PDF file (or any other supported file type)
dot_data = tree.export_graphviz(clf, out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf("iris.pdf") #try .csv here


# The export_graphviz exporter also supports a vriety of aesthetic options, including coloring nodes by their class
# IPython notebooks can also render these plots inline using the Image() function
dot_data = tree.export_graphviz(clf, out_file=None,
                                 feature_names=iris.feature_names,
                                 class_names=iris.target_names,
                                 filled=True, rounded=True,
                                 special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())


# After being fitted, the model can then be used to predict the class of samples
clf.predict(iris.data[:1, :])

# Alternatively, the probability of each class can be predicted,
# which is the fraction of training samples of the same class in a leaf
clf.predict_proba(iris.data[:1, :])





    
    
    
    
    
    
    
    
    
    
    


