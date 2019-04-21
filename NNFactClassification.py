from keras.models import load_model
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras import models
from keras import layers
import os
import pandas as pd
import ast
import gensim
import  numpy
from sklearn.model_selection import StratifiedKFold
from sklearn.utils import shuffle
from keras.constraints import max_norm
import matplotlib.pyplot as plt

# # print(model.wv['naffra'] )
model2= gensim.models.Word2Vec.load("modfulltext_20ep.model")
# directory='LabeledPairs\\'
directory='LabeledPairs2\\'
classes=[]
pairs=[]
count=0

n=[0] * 100
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
           try:
                pairline.append(model2.wv[j[0]])
           except:
                pairline.append(n)
        # print(pairline)
        pairs.append(pairline)
# print(classes)

flattened_class = [y for x in classes for y in x]
# # print(flattened_class)
# print(flattened_class.count(1))
# print(flattened_class.count(0))


X=np.array(list(map(lambda x: np.concatenate(x), pairs)))
Y=np.asarray(flattened_class)
print(X.shape)
#build ANNN

# print(pairs.shape)
print(Y.shape)

# Xr=X.reshape(,300)
# print(Xr.shape)
# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42) #build train/test set

# print(X_train.shape)
# Z = X_train.reshape(797,300)
# # print(X_test.shape)
# z=X_test.reshape(394,300)
# print(Z.shape)
model = models.Sequential()
# Input - Layer
model.add(layers.Dense(2, activation = "relu", input_shape=(300,)))
# Hidden - Layers
model.add(layers.Dense(20, activation = "relu"))
# model.add(layers.Dense(15, activation = "softmax"))
# model.add(layers.Dense(10, activation = "softmax"))
# model.add(layers.Dropout(0.4, noise_shape=None, seed=None))
# Output- Layer
model.add(layers.Dense(1, activation = "sigmoid"))
model.summary()
# compiling the model
model.compile(
 optimizer = "adam",
 loss = "binary_crossentropy",
 metrics = ["accuracy"]
)
history = model.fit(
    X, Y,
 epochs= 20,
    # batch_size = ,
    validation_split=0.2,
shuffle=True
)
# Plot training & validation accuracy values
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()
model.save('NNFactallv2.h5')
model.save_weights('NNFactwallv2.h5')
# define 10-fold cross validation test harness
# seed = 7
# numpy.random.seed(seed)
# kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
# cvscores = []
#
# for train, test in kfold.split(Xr,Y):
#   # create model
#     model = models.Sequential()
#     # Input - Layer
#     model.add(layers.Dense(2, activation="relu", input_shape=(300,)))
#     # Hidden - Layers
#     model.add(layers.Dense(20, activation = "relu"))
#     # Output- Layer
#     model.add(layers.Dense(1, activation = "sigmoid"))
#     model.summary()
#     # compiling the model
#
# 	# Compile model
#     model.compile(
#      optimizer = "adam",
#      loss = "binary_crossentropy",
#      metrics = ["accuracy"])
#         # Fit the model
#     model.fit(Xr[train], Y[train], epochs=200,  shuffle=True)
# 	# evaluate the model
#     scores = model.evaluate(Xr[test], Y[test], verbose=0)
#     print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
#     cvscores.append(scores[1] * 100)
# print("%.2f%% (+/- %.2f%%)" % (numpy.mean(cvscores), numpy.std(cvscores)))