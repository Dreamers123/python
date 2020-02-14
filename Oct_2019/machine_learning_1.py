import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
df=pd.read_csv("data/music.csv")
print(df.head())
X=df.drop(columns=['genre'])
y=df['genre']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model=DecisionTreeClassifier()
model.fit(X_train,y_train)
prediction=model.predict([[30.5,1]])
print(prediction)