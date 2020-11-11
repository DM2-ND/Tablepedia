# Created by Wenhao Yu at 19/02/2019
"""
Feature: #Enter feature name here
# Enter feature description here
Scenario: #Enter scenario name here
# Enter steps here
Test File Location: # Enter]
"""

import os
import pandas as pd

def get_all_files(path):

    """"
    Gets all files in a directory
    """

    if os.path.isfile(path): return [path]
    return [f for d in os.listdir(path)
              for f in get_all_files(os.path.join(path, d))]


# for file in get_all_files('csv-files'):

#     try:
#         file_data = pd.read_csv(file, encoding='gbk')
#     except UnicodeDecodeError:
#         file_data = pd.read_csv(file, encoding='utf-8')

#     '''
#     The output should be formatted as:

#     (Table Body)
#     xxx, xxx, xxx, ..., xxx
#     xxx, ..., ..., ..., xxx
#     xxx, ..., ..., ..., xxx

#     (Table Caption)
#     Table 1: xxx, xxx.

#     '''
#     print(file_data)

for indx, file in enumerate(get_all_files('csv-files')):

    os.rename(file, 'csv-files/anonymous_table_{}.csv'.format(indx))