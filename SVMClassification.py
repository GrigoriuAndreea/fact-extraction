from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import gensim
import ast
import pandas as pd
import os
import numpy as np
import sklearn
from sklearn.metrics import accuracy_score,recall_score,confusion_matrix
from sklearn.model_selection import cross_val_score
import pickle
from sklearn import svm


model2= gensim.models.Word2Vec.load("modfulltext_20ep.model")
directory='LabeledPairs\\'
classes=[]
pairs=[]
n=[0] * 100
E1 =['NN','NNS','NNP','NNPS','VB','VBD','VBN','VBP','VBZ']
K=list(range(0,len(E1)))
pos=dict(zip(E1,K))
n=[0] * 100
for filen in os.listdir(directory):
    df = pd.read_csv(directory+ filen,encoding='unicode_escape',header=None)
    clas=[]
    clas=df[1].tolist()
    classes.append(clas)
    lines = df[0].tolist()
    # print(lines)
    for x in lines:
        listx=ast.literal_eval(x)
        pairline = []
        for j in listx:
            # print(j[0])
           try:
               # new_v=np.append(model2.wv[j[0]],pos[j[1]])
               # pairline.append(new_v)
               pairline.append(model2.wv[j[0]])

           except:
                # new_v = np.append(n, pos[j[1]])
                # pairline.append(new_v)
                pairline.append(n)
        pairs.append(pairline)
#
flattened_class = [y for x in classes for y in x]
X=np.array(list(map(lambda x: np.concatenate(x), pairs)))
Y=np.asarray(flattened_class)

train_x, test_x, train_y, test_y = train_test_split(X, Y, train_size=0.2)
clf = svm.SVC(coef0=5)

 # clf = svm.SVC(kernel='linear', C=1)
# scores = cross_val_score(clf, iris.data, iris.target, cv=5)
clf.fit(X, Y)
svm_cv_score = cross_val_score(clf, X, Y, cv=10)
# clf.predict
print(svm_cv_score)
print("Mean AUC Score - Random Forest: ", svm_cv_score.mean())
# filename = 'SVMEmb.sav'
# pickle.dump(clf, open(filename, 'wb'))