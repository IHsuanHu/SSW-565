# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 14:07:01 2023

@author: user
"""
import re
import numpy as np
from sklearn.cluster import AgglomerativeClustering
import time
import collections
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-MiniLM-L6-v2')
import pandas

excel_df = pandas.read_excel(r'C:\\Users\\user\\Desktop\\final.xlsx')
# sentences = set()
sentences = []
senowner = {}
senreview = {}

for index, text in excel_df.iterrows():
    tmp = text['subject']
    tmp = re.sub(r'[^a-zA-Z0-9]', ' ', tmp)
    sentences.append(tmp)

    if tmp in senowner:
        senowner[tmp].append(int(text['owner_id']))
    else:
        senowner[tmp] = [int(text['owner_id'])]
    
    reviewer = text['reviewer_id'][1:-1]
    a = reviewer.split(',')
    
    if reviewer:
        for i in a:
       
            if tmp in senreview:
                senreview[tmp].append(int(i))
            else:
                senreview[tmp] = [int(i)]

# option 1

# sentence_embeddings = model.encode(sentences)
# # Normalize the embeddings to unit length
# sentence_embeddings = sentence_embeddings /  np.linalg.norm(sentence_embeddings, axis=1, keepdims=True)

# # Perform kmean clustering
# clustering_model = AgglomerativeClustering(n_clusters=None, distance_threshold=1.5) #, affinity='cosine', linkage='average', distance_threshold=0.4)
# clustering_model.fit(sentence_embeddings)
# cluster_assignment = clustering_model.labels_

# clustered_sentences = {}
# for sentence_id, cluster_id in enumerate(cluster_assignment):
#     if cluster_id not in clustered_sentences:
#         clustered_sentences[cluster_id] = []

#     clustered_sentences[cluster_id].append(sentences[sentence_id])

# for i, cluster in clustered_sentences.items():
#     print("Cluster ", i+1)
#     print(cluster)
#     print("")


ownergroup = {i:[] for i in range(7)}
reviewergroup = {i:[] for i in range(7)}
subject = {}


corpus_embeddings = model.encode(sentences, batch_size=64, show_progress_bar=True, convert_to_tensor=True)


print("Start clustering")
start_time = time.time()

#Two parameters to tune:
#min_cluster_size: Only consider cluster that have at least 25 elements
#threshold: Consider sentence pairs with a cosine-similarity larger than threshold as similar
clusters = util.community_detection(corpus_embeddings, min_community_size=25, threshold=0.75)

print("Clustering done after {:.2f} sec".format(time.time() - start_time))

#Print for all clusters the top 3 and bottom 3 elements
for i, cluster in enumerate(clusters):
    # print("\nCluster {}, #{} Elements ".format(i+1, len(cluster)))
    # for sentence_id in cluster[0:10]:
    #     print("\t", sentences[sentence_id])
    # print("\t", "...")
    # for sentence_id in cluster[-5:]:
    #     print("\t", sentences[sentence_id])
    tmp = set()
    for sentence_id in cluster:
        tmp.add(sentences[sentence_id])
        if sentences[sentence_id] in senowner:
            ownergroup[i] += senowner[sentences[sentence_id]]
        if sentences[sentence_id] in senreview:
            reviewergroup[i] += senreview[sentences[sentence_id]]
    subject[i] = tmp

ansowner = { i: sorted(list(set(j))) for i, j in ownergroup.items()}
ansreview = { i: sorted(list(set(j))) for i, j in reviewergroup.items()}    


