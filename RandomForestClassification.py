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


model2= gensim.models.Word2Vec.load("modfulltext_20ep.model")
# directory='LabeledPairs\\'
directory='LabeledPairs2\\'
classes=[]
pairs=[]
n=[0] * 100
E1 =['NN','NNS','NNP','NNPS','VB','VBD','VBN','VBP','VBZ']
K=[0]*len(E1)
pos=dict(zip(E1,K))
print(pos)
# print(pos)
for filen in os.listdir(directory):
    df = pd.read_csv(directory+ filen,encoding='unicode_escape',header=None)
    clas=[]
    clas=df[2].tolist()
    classes.append(clas)
    lines = df[0].tolist()
    # print(lines)
    for x in lines:
        listx=ast.literal_eval(x)
        pairline = []
        for j in listx:
            # print(j[0])
            # pos[j[1]]=pos[j[1]]+1
           try:
               new_v=np.append(model2.wv[j[0]],pos[j[1]])
               pairline.append(new_v)
               # pairline.append(model2.wv[j[0]])

           except:
                new_v = np.append(n, pos[j[1]])
                pairline.append(new_v)
                # pairline.append(n)
        pairs.append(pairline)
print(pos)
flattened_class = [y for x in classes for y in x]

X=np.array(list(map(lambda x: np.concatenate(x), pairs)))
Y=np.asarray(flattened_class)

train_x, test_x, train_y, test_y = train_test_split(X, Y,
                                                    train_size=0.2)
#
rfc = RandomForestClassifier()
rfc.fit(train_x,train_y)
rfc_cv_score = cross_val_score(rfc, X, Y, cv=10)
# rfc = RandomizedSearchCV(estimator = rfc, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)

# # predictions
rfc_predict = rfc.predict(test_x)
# print(accuracy_score(rfc_cv_score,test_y))
print(rfc_cv_score)
print("Mean AUC Score - Random Forest: ", rfc_cv_score.mean())
filename = 'RandomForestEmb+POSv2.sav'
pickle.dump(rfc, open(filename, 'wb'))
# #
# #
# # load the model from disk
# loaded_model = pickle.load(open(filename, 'rb'))