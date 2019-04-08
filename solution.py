import pandas
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#tylko dane liczbowe
#dla wartości nan trzeba usunąć/wypełnić

X_train = pandas.read_csv('train/train.tsv',
                    usecols=["Powierzchnia w m2", "Liczba pokoi", "Liczba pięter w budynku", "Rok budowy" ],
                    delimiter='\t', encoding="utf-8").fillna(-1)

y_train = pandas.read_csv('train/train.tsv', usecols=["cena"], delimiter='\t', encoding="utf-8").fillna(-1)

X_test_in = pandas.read_csv('test-A/in.tsv', sep='\t', header=None, usecols=[0, 1, 3, 8]).fillna(-1)

reg = LogisticRegression().fit(X_train, y_train)

y_out = reg.predict(X_test_in)

with open('test-A/out.tsv', 'w') as output_file:
    for out in y_out:
        print('%.0f' % out, file=output_file)


