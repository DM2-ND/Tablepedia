# Created by Wenhao Yu at 19/02/2019
"""
Feature: #Enter feature name here
# Enter feature description here
Scenario: #Enter scenario name here
# Enter steps here
Test File Location: # Enter]
"""

'''
if running tabula-java with python,
you should install the package by following command
$ pip install tabula-py
'''

from tabula import convert_into

def convert_pdf_to_csv(input_pdf, output_csv):
    convert_into(input_pdf, output_csv,  output_format='tsv')

convert_pdf_to_csv('tabula-test/test.pdf', 'tabula-test/test.csv')