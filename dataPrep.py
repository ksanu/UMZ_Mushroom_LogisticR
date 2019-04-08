import pandas
import numpy as np


X_train_in = pandas.read_csv('dev-0/in.tsv', encoding="utf-8", delimiter='\t')
"""
#Nie działa: - zastępuje pierwszy wiersz nazwami kolumn
X_train_in.columns = ['cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor', 'gill-attachment', 'gill-spacing',
'gill-size', 'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring',
'stalk-color-above-ring','stalk-color-below-ring', 'veil-type','veil-color', 'ring-number', 'ring-type',
                      'spore-print-color', 'population', 'habitat']
"""
print (X_train_in[:4])

