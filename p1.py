# Importing the libraries
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

# Importing the mall dataset with pandas
dataset = pd.read_csv('Mall_Customers.csv')
x = dataset.iloc[:, [3, 4]].values

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
	kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
	kmeans.fit(x)
	wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Applying k-means to the mall dataset
kMeans = KMeans(n_clusters = 5, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
yKmeans = kMeans.fit_predict(x)

# Visualising the clusters
plt.scatter(x[yKmeans == 0, 0], x[yKmeans == 0, 1], s = 100, c='red', label = 'Careful')
plt.scatter(x[yKmeans == 1, 0], x[yKmeans == 1, 1], s = 100, c='blue', label = 'Standard')
plt.scatter(x[yKmeans == 2, 0], x[yKmeans == 2, 1], s = 100, c='green', label = 'Target')
plt.scatter(x[yKmeans == 3, 0], x[yKmeans == 3, 1], s = 100, c='cyan', label = 'Careless')
plt.scatter(x[yKmeans == 4, 0], x[yKmeans == 4, 1], s = 100, c='magenta', label = 'Sensible')
plt.scatter(kMeans.cluster_centers_[:, 0], kMeans.cluster_centers_[:, 1], s = 300, c='yellow', label = 'Centroids')
plt.title('Clusters of clients')
plt.xlabel('Annual Income(k$)')
plt.ylabel('Spending Score(1-100)')
plt.legend()
plt.show()

