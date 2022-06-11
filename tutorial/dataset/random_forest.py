import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

iris = pd.read_csv("iris.data")

#check the iris dataset
print(iris.shape)

#get the training X features of the iris data
X=iris.iloc[:, :-1].values
print(f'the training feature shape is  {X.shape}')


y=iris.iloc[:, -1].values
print(f'the lable of iris {y}')


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2,
                                                    random_state = 123)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print('The accuracy of the Random forest is:',metrics.accuracy_score(y_pred,y_test))
