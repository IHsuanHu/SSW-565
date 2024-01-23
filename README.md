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
- 
<div align="center">
Table 1. Keywords for each cluster
</div>
c	 |  Keywords of Clusters :
- | -
0	| Fix, create, add, update, and change security group rules
1	| Fix, create, add, remove, and rename security group
2	| Add, allow, update, apply, and test security group port
3	| Add, ingress, and fix pod container security
4	| Add, fix, split, merge, and use tests for security groups
5	| Add, test, switch, normalize, fix, and disable neutron security group
6	| Delete, change, fix, change, and enable default security groups

