# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 15:18:08 2023

@author: user
"""

import pandas
import collections
import statistics
import networkx as nx
import matplotlib.pyplot as plt

excel_df = pandas.read_excel(r'C:\\Users\\user\\Desktop\\final.xlsx')

count = collections.Counter()
check = ['-','_', '(', '[', ':', '\'', '\"', '#', '.', '$', '*', '<', '`', '/']
for text in excel_df['subject']:
    tmp = text.strip()
    tmp = tmp.split(' ')
    for word in tmp:
        if len(word) > 3 and word[0].isdigit() == False and word[0] not in check:
            count[word.lower()] += 1


relation = collections.defaultdict(set)
relationCount = collections.defaultdict(dict)
task = collections.defaultdict(int)
subject = collections.defaultdict(int)
node = []
edges = set()
same = []
for index, peo in excel_df.iterrows():
    subject[peo['subject'].lower()] += 1
    owner = peo['owner_id']
    task[int(owner)] += 1
    reviewer = peo['reviewer_id']
    reviewer = reviewer[1:-1]
    node.append(int(owner))
    if reviewer:
        tmp = reviewer.split(',')
        for i in tmp:
            relation[int(owner)].add(int(i))
            relationCount[int(owner)][int(i)] = relationCount[int(owner)].get(int(i), 0) +1
            if int(owner) != int(i):
                edges.add((int(owner), int(i)))
            else:
                same.append(int(owner))
            
sortcount = {key: dict(sorted(value.items(), key=lambda item: item[1], reverse=True)) for key, value in relationCount.items()}






    
