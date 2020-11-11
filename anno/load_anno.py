# Created by Wenhao Yu at 19/02/2019
"""
Feature: #Enter feature name here
# Enter feature description here
Scenario: #Enter scenario name here
# Enter steps here
Test File Location: # Enter]
"""

import json

fr = open('annotated_labels.json', 'r')

'''
label is a dict consisting of
    {
        concept_name_1: label_1,
        concept_name_2: label_2,
        ...,
        concept_name_n: label_n,
    }
'''
labels = json.load(fr)


'''
dataset is list of concept labelled as 'Dataset'
'''
dataset = [k for k, v in labels.items() if v == 'Dataset']
method = [k for k, v in labels.items() if v == 'Method']
metric = [k for k, v in labels.items() if v == 'Metric']

