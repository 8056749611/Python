# -*- coding: utf-8 -*-
"""Python bootcamp project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q00FJYtoKVMwHtN9u4bnViN-sz5R5I5s

1.CORRELATION
"""

Correlation Between Features In The Datase:

Data Correlation: Is a way to understand the relationship between multiple variables and attributes in your dataset. Using Correlation, you can get some insights such as: One or multiple attributes depend on another attribute or a cause for another attribute.

there are theree types of correlations 1.personal's coefficient 2.spearman's coefficient 3.kendall coeffcient

Two Strong Correlation:

The rule of correlation coefficients,the strongest correlation is considered when the value is closest to +1 (positive correlation) or -1 (negative correlation). A positive correlation coefficient indicates that the value of one variable depends on the other variable directly.

"""2.OUTLIERS

"""

Which feature has more outliers:

Outliers can also come in different flavours, depending on the environment: 
point outliers, contextual outliers, or collective outliers. Point outliers are single data
points that lay far from the rest of the distribution. Contextual outliers can be noise in data, such as punctuation
symbols when realizing text analysis or background noise signal when doing speech recognition. Collective outliers
can be subsets of novelties in data such as a signal that may indicate the discovery of new phenomena.

import sklearn
from sklearn.datasets import load_boston
import pandas as pd
import matplotlib.pyplot as plt

bos_hou = load_boston()

column_name = bos_hou.feature_names
df_boston = pd.DataFrame(bos_hou.data)
df_boston.columns = column_name
df_boston.head()

import seaborn as sns
sns.boxplot(df_boston['DIS'])

from scipy.stats import pearsonr
import matplotlib.pyplot as plt
 
X = [1,2,3,4,5,6,7,8,9,10,11,12,13]
Y = [7,8,8,11,10,11,12,15,20,14,16,15,19]

plt.scatter(X,Y)
plt.show()

"""3.DIABETES"""

import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        df= pd.read_csv('/kaggle/input/diabetes-dataset/diabetes2.csv')
        df.head()
        df.info()
        df.describe()
        sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')
        sns.countplot(x='Outcome',data=df)
        sns.distplot(df['Age'].dropna(),kde=True)
        df.corr()
        sns.heatmap(df.corr())
        sns.pairplot(df)
        plt.subplots(figsize=(20,15))
        sns.boxplot(x='Age', y='BMI', data=df)
        x = df.drop('Outcome',axis=1)
        y = df['Outcome']
        from sklearn.model_selection import train_test_split
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=101)
        from sklearn.linear_model import LogisticRegression
        logmodel = LogisticRegression()
        logmodel.fit(x_train,y_train)
        predictions = logmodel.predict(x_test)
        from sklearn.metrics import classification_report
        print(classification_report(y_test,predictions))
        from sklearn.metrics import confusion_matrix
        confusion_matrix(y_test,predictions)

