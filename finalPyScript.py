# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 22:22:04 2023

@author: user
"""

import pandas as pd

path = input("Enter file path: ")

data = pd.read_csv(path, encoding='cp1252')


excel_writer = pd.ExcelWriter(r'C:\Users\user\Desktop\final.xlsx', engine='openpyxl')

data[['url', 'subject', 'description', 'owner_id','owner_name','reviewer_id',
      'reviewer_name']].to_excel(excel_writer, index=False, sheet_name='Sheet1')
worksheet = excel_writer.sheets['Sheet1']
width = [12, 35, 50, 10, 15, 15, 15]
count = 0
for col in worksheet.columns:
    colletter = col[0].column_letter
    worksheet.column_dimensions[colletter].width = width[count]
    count += 1

excel_writer.save()


