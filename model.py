import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import pickle
column = ['sepal-length','sepal-width','petal-length','petal-width','class']
df = pd.read_csv('data/iris.csv',names=column)
X = df.iloc[:,:-1].values
Y = df.iloc[:,-1].values
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
classifier = SVC()
classifier.fit(X_train,y_train)

pickle.dump(classifier, open('data/model.pkl','wb'))

y_predict =classifier.predict(X_test)
# Summary of the predictions made by the classifier
print(classification_report(y_test, y_predict))
print(confusion_matrix(y_test, y_predict))

