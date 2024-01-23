# The Study of code review assignment
### Aim of this project
OpenStack has been used for code review for many repositories. Allocating the code review tasks to code reviewers is time-consuming and requires significant expertise. It is important to categorize the type of code check-ins. Please take a look at [https://review.opendev.org/Links](https://review.opendev.org/Links) to an external site., export a list of more than 500 check-ins, or use the attached file [Code_Review_Project-1.csv](https://github.com/IHsuanHu/Study_of_code_review_assignment/blob/master/Code_Review_Project-1.csv)clustering each row/sample based on their architectural attributes, example, documentation related, performance improvement, test coverage or improve testability, security enhancement, etc.  The clustering methods can be simply keywords-based, machine learning-based, or any other approaches you would like to explore.

## Introduction
In the context of cloud computing, OpenStack is an essential infrastructure-as-a-service (IaaS) platform that represents an open, free standard. OpenStack, which is widely used in both public and private cloud settings, gives customers access to a variety of resources and virtual machines. Its software platform consists of networked components that coordinate various hardware pools that include networking, storage, and computing resources in data centers.

OpenStack's code review process involves several repositories, therefore assigning responsibilities to code reviewers is necessary. But since it takes a lot of time and knowledge, this procedure is not without its difficulties. Classifying code check-ins, optimizing efficiency, and expediting the review process are important components of this endeavor. OpenStack is accessed by users using several interfaces, including an intuitive online dashboard, command-line utilities, and RESTful.

## Method
Based on the material of “Code Review Project-1.csv”, we had subjects with its owner and the reviewer of the subjects. We aimed to find the relationship between the subject and its owner, and the relationship between the owner and reviewers. Therefore, two methods were applied in this study.

For the relationship between subject and owner, we used a project, sentence-transformers, from Github, and the models of this project are based on transformer networks like BERT / RoBERTa, etc. The subjects were embedded in vector space so that similar subjects were closer and could efficiently be found using cosine similarity. We also used the algorithm, fast_clustering.py, in this project to cluster the subjects as an efficient method. After clustering, we grouped the owners and reviewers for each cluster and removed not significantly relative subjects to have simply keywords-based.

On the other way, we used Principal Component Analysis (PCA) to cluster owners via the relationship between owners and reviewers. We collected all the owners’ dependencies which were reviewers reviewing the owner’s work. After that, we use a distance matrix to represent the present frequency of the reviewer to the owner. Reviewer distance (frequency) is calculated as follows:

Reviewer frequency = Number of times of the reviewer/ Total of reviewing times of all reviewer
Reference

Once we got the distance matrix, we applied the PAC model to the matrix to do dimension reduction, and then we did a 3D plot to show the result. Meanwhile, we used the Elbow Method to find the optimal K and then used k-means clustering.

## Result
By using the Sentence Transformers method, the result showed that we could classify the majority of sentences into 7 clusters, and each cluster had its group of owners and reviewers.

![fig1](https://github.com/IHsuanHu/Study_of_code_review_assignment/blob/master/fig1.png)
<div align="center">
Fig. 1. Group of owners by using Sentence Transformers
</div>  

![fig2](https://github.com/IHsuanHu/Study_of_code_review_assignment/blob/master/fig2.png)
<div align="center">
Fig. 2. Group of reviewers by using Sentence Transformers
</div>  

![table1](https://github.com/IHsuanHu/Study_of_code_review_assignment/blob/master/table1.PNG)

There is a 2359 x 2359 distance matrix for PCA analysis and after dimension reduction, we retain 3 columns for the x, y, and z-axis. The result of the Elbow Method showed that K = 6 has a significant change in the rate of decrease, which means clustering into 6 could be a good fit for this data. As a result, all the owners and reviewers could be assigned to 6 groups.

![fig3](https://github.com/IHsuanHu/Study_of_code_review_assignment/blob/master/fig3.png)
<div align="center">
Fig. 3. The result of the Elbow Method
</div> 

![fig4](https://github.com/IHsuanHu/Study_of_code_review_assignment/blob/master/fig4.png)
<div align="center">
Fig. 4. The result of K-Means clustering
</div>

<div align="center">
<img src="https://github.com/IHsuanHu/Study_of_code_review_assignment/blob/master/fig5.png">
Fig. 5 All id were classified into 6 groups
</div>

## Discussion
With the model of Sentence Transformers, we could cluster most of the subjects into 7 groups, and for each group, we can see that all the subjects were relative. Therefore, we can conclude keywords for each cluster, which is helpful in that we can assign relative subjects to the owners and reviewers. However, the miner subjects might be neglected as they are not the majority in this project, so this approach might lose some of the clusters. As a result, it may be difficult to assign edge subjects to the right reviewers.

In the analysis of the relationship between owners and reviewers, the result of the Elbow Method showed that dividing into 6 clusters was the optimal solution, and all the ID was assigned. Here is the top 10 most frequently used word in each cluster after removing all the preposition and common words presented in all clusters:
```
0: ['context', 'port', 'api', 'neutron', 'container', 'pod', 'guide', 'driver', 'fixes', 'implement']
1: ['port', 'api', 'neutron', 'instance', 'quantum', 'plugin', 'nova', 'nsx', 'make', 'driver']
2: ['port', 'api', 'neutron', 'instance', 'nova', 'refactor', 'fixes', 'bug', 'fixed', 'plugin']
3: ['guide', 'openstack', 'section', 'networking', 'rst', 'notes', 'link', 'file', 'docs', 'nova']
4: ['context', 'container', 'pod', 'implement', 'missing', 'port', 'pods', 'containers', 'policy', 'nsx']
5: ['modified', 'networking', 'infoblox', 'unit', 'common', 'dnm', 'nova', 'context', 'neutron', 'stable']
```
However, we could not easily find distinguish keywords for each cluster. The only thing we knew was we could cluster all IDs into 6 groups based on their relationship. This could be a problem if we want to assign subjects to reviewers to review in the future as there are no keywords for each cluster.

In conclusion, the Sentence Transformers approach can give specific keywords for each cluster but some information about overall subjects may be lost. In the PCA and K-Means approach, we can group all IDs via their relationship; however, the keywords for each group are ambiguous. As a result, another analysis method is required to have a more explicit result in the future study.

## Reference
1. [OpenStack Open Source Cloud Computing Software](https://www.openstack.org/)
2. [Sentence Transformers](https://github.com/UKPLab/sentence-transformers/blob/master/README.md)
3. [fast_clustering.py](https://github.com/UKPLab/sentence-transformers/blob/master/examples/applications/clustering/fast_clustering.py)
4. [Principal Component Analysis (PCA)](https://www.datacamp.com/tutorial/principal-component-analysis-in-python)
5. [Elbow Method for the optimal value of k in KMeans](https://www.geeksforgeeks.org/elbow-method-for-optimal-value-of-k-in-kmeans/)
6. [K-Means Clustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
