import nltk
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import ast
from textblob import TextBlob

stop_words = set(stopwords.words('english'))
lemmatizer=WordNetLemmatizer()
######Preprocessing

#Conversion to lower case
# directory="CaseLawGEcutfacts"
# filename=os.listdir(directory)
# persons=[]
# geopolitical=[]
# companies=[]
# for j in range(0,10):
#     file=open(directory+"\\"+filename[j],"r",encoding='utf-8')
#     newf = open("FARS_annotation\\Preprocessed\\" + filename[j], 'w', encoding='utf-8')
#     text=file.readlines()
#     for line in text:
#             newf.write(line.lower())

#stop words removal
# directory="FARS_annotation\\Preprocessed"
# filename=os.listdir(directory)
# for filen in filename:
#     file = open(directory + "\\" + filen, "r", encoding='utf-8')
#     newf = open(directory + "\\" +"sw" +filen, "w", encoding='utf-8')
#     text=file.readlines()
#     for line in text:
#         tokens=word_tokenize(line)
#         result=[i for i in tokens if not i in stop_words]
#         newf.write(str(result)+'\n')

#lemmatization
# directory="FARS_annotation\\Preprocessed\\StopWord"
# directoryn="FARS_annotation\\Preprocessed\\Lemm"
# filename=os.listdir(directory)
# for filen in filename:
#     file = open(directory + "\\" + filen, "r", encoding='utf-8')
#     newf = open(directoryn + "\\" + "lm" + filen, "w", encoding='utf-8')
#     text=file.readlines()
#     for ls in text:
#         tokens=ast.literal_eval(ls)
#         lemm=[lemmatizer.lemmatize(i) for i in tokens]
#         newf.write(str(lemm) + '\n')


#POS tagging
directory="FARS_annotation\\Preprocessed\\Lemm"
directoryn="FARS_annotation\\Preprocessed\\POS"
filename=os.listdir(directory)
for filen in filename:
    file = open(directory + "\\" + filen, "r", encoding='utf-8')
    newf = open(directoryn + "\\" + "POS" + filen, "w", encoding='utf-8')
    text=file.readlines()
    for ls in text:
        tokens=ast.literal_eval(ls)
        result = nltk.pos_tag(tokens)
        newf.write(str(result) + '\n')
