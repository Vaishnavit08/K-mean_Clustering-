# importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# loading iris dataset


dataset=pd.read_csv('Iris.csv')
x=dataset.iloc[:,[0,1,2,3]].values

# finding the optimum number of clustures for k-mean classification

from sklearn.cluster import KMeans
wcss=[]

for i in range(1,11):
    kmeans=KMeans(n_clusters=i, init='k-means++',max_iter=300,n_init=10, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

# plotting the results onto a line graph , allowing us to observe "the elnow"

plt.plot(range(1,11),wcss)
plt.title('The elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')   #within clustures sum of squares
plt.show()

# applying kmeans to dataset /  creating the kmeans classifier

kmeans=KMeans(n_clusters=3, init='k-means++',max_iter=300, n_init=10,random_state=0)
y_kmeans=kmeans.fit_predict(x)

# visualising the clusters
plt.scatter(x[y_kmeans==0,0],x[y_kmeans==0,1],s=100,c='red',label='Iris-versicolur')

plt.scatter(x[y_kmeans==1,0],x[y_kmeans==1,1],s=100,c='blue',label='Iris-versicolour')

plt.scatter(x[y_kmeans==2,0],x[y_kmeans==2,1],s=100,c='green',label='Iris-Virginica')

# plotting the centroids of the clusters

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c='yellow', label='Centroids')

plt.legend()
plt.show()



