import pandas as pd
import numpy as np


columnNames = ['cap-shape',
                      'cap-surface',
                      'cap-color',
                      'bruises',
                      'odor',
                      'gill-attachment',
                      'gill-spacing',
                      'gill-size',
                      'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring',
'stalk-color-above-ring','stalk-color-below-ring', 'veil-type','veil-color', 'ring-number', 'ring-type',
                      'spore-print-color', 'population', 'habitat']

X_train_in = pd.DataFrame(pd.read_csv('dev-0/in.tsv', encoding="utf-8", delimiter='\t', header=None, names=columnNames))

"""
featureDict = {'cap-shape': 0,
                      'cap-surface': 1,
                      'cap-color': 2,
                      'bruises': 3,
                      'odor': 4,
                      'gill-attachment': 5,
                      'gill-spacing': 6,
                      'gill-size': 7,
                      'gill-color': 8,
                      'stalk-shape': 9,
                      'stalk-root': 10,
                      'stalk-surface-above-ring': 11,
                      'stalk-surface-below-ring': 12,
                      'stalk-color-above-ring': 13,
                      'stalk-color-below-ring': 14,
                      'veil-type': 15,
                      'veil-color': 16,
                      'ring-number': 17,
                      'ring-type': 18,
                      'spore-print-color': 19,
                      'population': 20,
                      'habitat': 21}
"""

def one_hot_encoding(X_df):
    for colName_to_OneHotEncode in list(X_df.columns.values):
            one_hot = pd.get_dummies(X_df[colName_to_OneHotEncode])
            X_df = X_df.drop(colName_to_OneHotEncode, axis=1)
            # Join the encoded df
            X_df = X_df.join(one_hot, lsuffix='_l', rsuffix='_r')
    return X_df

df_with_dummies = pd.get_dummies( X_train_in, columns = columnNames )
print (df_with_dummies)
"""
#print(one_hot)
newdf = X_train_in[X_train_in.columns[2:4]]
print(newdf)
X_one_hot = one_hot_encoding(newdf)
print (X_one_hot)
"""

