# -*- coding: utf-8 -*-

import numpy as np
import collections
import pandas
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import re


excel_df = pandas.read_excel(r'C:\\Users\\user\\Desktop\\final.xlsx')
allid = set()
original = collections.defaultdict(dict)
idtosubject = {}
for index, text in excel_df.iterrows():
    tmp = text['subject']
    tmp = re.sub(r'[^a-zA-Z0-9]', ' ', tmp)
    idtosubject.setdefault(int(text['owner_id']), set()).add(tmp)
    
    reviewer = text['reviewer_id'][1:-1]
    if reviewer:
        for i in reviewer.split(','):
            idtosubject.setdefault(int(i), set()).add(tmp)


for index, peo in excel_df.iterrows():
    owner = int(peo['owner_id'])
    allid.add(owner)
    reviewer = peo['reviewer_id'][1:-1]
    total = 0
    if 'total' in original[owner]:
        total = original[owner].get('total')
    tmp = reviewer.split(',')
    if reviewer:
        for i in tmp:
            allid.add(int(i))
            original[owner][int(i)] = original[owner].get(int(i), 0) + 1
            total += 1
            
        original[owner]['total'] = total
# distance for pca
distance_matrix = np.zeros((len(allid), len(allid)))

allid = sorted(list(allid))
keypair = {key:index for index, key in enumerate(allid)}
toid = {index:key for index, key in enumerate(allid)}

for key, value in original.items():
    for i, j in value.items():
        if i != 'total':
            dis = j/ original[key].get('total')
            distance_matrix[keypair[key], keypair[i]] = dis


my_pca = PCA(n_components=3, whiten=True)
scaled_data = (distance_matrix - distance_matrix.mean()) / distance_matrix.std()  # Standardizing the data
my_pca_result = my_pca.fit_transform(scaled_data)

# # View the principal component loading
# print(my_pca.components_)
# # See the principal components
# print(my_pca_result)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x1 = my_pca_result[:, 0]
y1 = my_pca_result[:, 1]
z1 = my_pca_result[:, 2]

ax.scatter(x1, y1, z1)
ax.set_xlim([-3, 7])
ax.set_ylim([-3, 7])
ax.set_zlim([-3, 7])
ax.set_title('Dataset')
plt.show()
# x1 = my_pca_result[:, 0]
# y1 = my_pca_result[:, 1]
# plt.plot()
# plt.xlim([-3, 7])
# plt.ylim([-3, 7])
# plt.title('Dataset')
# plt.scatter(x1, y1)
# plt.show()

# create new plot and data
plt.plot()
# X = np.array(list(zip(x1, y1))).reshape(len(x1), 2)
X = np.array(list(zip(x1, y1, z1)))
colors = ['b', 'g', 'r']
markers = ['o', 'v', 's']
# k means determine k
distortions = []
K = range(2, 9)
for k in K:
    kmeanModel = KMeans(n_clusters=k).fit(X)
    distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])
# Plot the elbow
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()


# Specify the number of clusters (k)
k = 6
X = my_pca_result
# Perform k-means clustering
kmeans = KMeans(n_clusters=k)
kmeans.fit(X)

# Get the cluster labels and centroids
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

cluster_indices = {}
for i in range(k):
    cluster_indices[i] = np.where(labels == i)[0]
res = {}
for cluster_id, indices in cluster_indices.items():
    tmp = []
    for i in indices:
        tmp.append(toid[i])
    res[cluster_id] = tmp
    
# Plot the data points with different colors for each cluster
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Assuming x1, y1, and z1 are the columns of my_pca_result
ax.scatter(x1, y1, z1, c=labels, cmap='viridis', edgecolors='k', s = 10)
ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2], c='red', marker='X', s=100, label='Centroids')

ax.set_title(f'K-Means Clustering (k={k})')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()
plt.show()

# # Plot the data points with different colors for each cluster
# plt.scatter(x1, y1, c=labels, cmap='viridis', edgecolors='k')
# plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
# plt.title(f'K-Means Clustering (k={k})')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.legend()
# plt.show()

ressubject = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
for index, i in enumerate(res.values()):
    for j in i:
        ressubject[index] = ressubject[index] + list(idtosubject[int(j)])
        
textcounter = {}
for index, i in enumerate(ressubject.values()):
    tmp = ' '.join(i).split(' ')
    textcounter[index] = {}
    for k in tmp:
        if len(k) >2 and k.lower() not in ['security', 'group', 'groups', 'rules', 
            'rule', 'with', 'for', 'the', 'and', 'from', 'when', 'add', 'fix', 'update', 
            'tests', 'not', 'use', 'remove', 'create', 'added', 'adding', 'delete', 'allow',
            'list', 'adds', 'test', 'name', 'support', 'default'] and not k.isdigit():
            textcounter[index][k.lower()] = textcounter[index].get(k.lower(), 0) +1
            
sorted_textcounter = {index: dict(sorted(values.items(), key=lambda item: item[1], reverse=True))
                      for index, values in textcounter.items()}
for i in sorted_textcounter.values():
    firstten = []
    for key in list(i)[:10]:
        firstten.append(key)
    print(firstten)