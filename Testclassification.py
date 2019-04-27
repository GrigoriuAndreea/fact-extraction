import os
import nltk
import ast
from textblob import TextBlob
import lexnlp
import lexnlp.nlp.en.tokens
from nltk.tag import StanfordPOSTagger
from lexnlp.config.stanford import STANFORD_POS_PATH
import nltk
from pyjarowinkler import distance
import collections
from keras.models import load_model
import gensim
import numpy as np
import pickle
import random
##########################PREPROCESSING

###get title for each id
# titles = [line.rstrip('\n') for line in open('title_alldoc.txt',encoding='utf-8')]
# ids = [line.rstrip('\n') for line in open('listOfIDs.txt',encoding='utf-8')]
# idsge=[line.rstrip('\n') for line in open('itemid_gender_equality2(45).txt',encoding='utf-8')]
# casedict=dictionary = dict(zip(ids, titles))
# orgdict=dictionary = dict(zip(ids, titles))
# listt=[]
# for key,value in orgdict.items():
#     listt=value
#     listt=value.split('v.')
#     # print(list[0])
#     if "CASE OF " in listt[0]:
#         listt[0]=listt[0].split('OF ')
#         orgdict[key]=(listt[0][1])
#     else:
#         orgdict[key] = "unknown"
# uniq=[x for x in os.listdir('CaseLawcompletecutfacts') if x not in idsge]
# rand=random.sample(uniq, 10)
# rand_items=rand
# print(rand_items)
#
#
# appliclist=["applicant","applicants"]
# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# # files='001-177677.txt'
# # # directory="CaseLawGEcutfacts\\"
# # ########add applicant from title
# for filen in rand_items:
#     file = open("CaseLawcompletecutfacts\\"  + filen, "r", encoding='utf-8')
#     newf = open("Unseendata\\"+ "noapp"+filen, 'w', encoding='utf-8')
#     text=file.readlines()
#     id=filen.rstrip('.txt')
#     app=orgdict[id]
#     for line in text:
#         tokens = tokenizer.tokenize(line)
#         for tok in tokens:
#             token = lexnlp.nlp.en.tokens.get_token_list(tok,stopword=False)
#                 # print(token)
#             for i in range(len(token)):
#                 if token[i].lower() in appliclist:
#                     token[i]=app
#             newf.write(str(token)+ '\n')
#
#
#
# # tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# STANFORD_DEFAULT_TAG_MODEL = os.path.join(STANFORD_POS_PATH, "models", "english-bidirectional-distsim.tagger")
# STANFORD_POS_FILE = os.path.join(STANFORD_POS_PATH, "stanford-postagger.jar")
# STANFORD_TAGGER = StanfordPOSTagger(STANFORD_DEFAULT_TAG_MODEL, STANFORD_POS_FILE)
# #
# # # pos = STANFORD_TAGGER.tag(tokens)
# # for filen in os.listdir("Preprocessing\\Cases45noapp"):
# for filen in rand_items:
#     file = open("Unseendata\\"+ "noapp"+filen, "r", encoding='utf-8')
#     newf = open("Unseendata\\"+ "pos"+filen , "w", encoding='utf-8')
#     text=file.readlines()
#     for line in text:
#             token=ast.literal_eval(line)
#             pos = STANFORD_TAGGER.tag(token)
#         # print(pos)
#             newf.write(str(pos) + '\n')
#
# ######coreference
# # file = open("Preprocessing\\POStagsentencev2\\001-57865.txt")
# # print(file.readlines())
# pronouns=["she","he","they","him","her"]
# # compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
# # for filen in os.listdir(directory):
# for filen in rand_items:
#     file = open("Unseendata\\"+ "pos"+filen, "r", encoding='utf-8')
#     newf = open("Unseendata\\"+ "npron"+filen, "w", encoding='utf-8')
#     text = file.readlines()
#     # print(l)
#     for l in range(len(text)):
#           linelst=ast.literal_eval(text[l])
#           print(linelst)
#           # linelst=[list(x) for x in linelst]
#           for i in range(len(linelst)):
#               if str(linelst[i][0]).lower() in pronouns:
#                   if l!=0:
#                     for j in reversed(ast.literal_eval(text[l-1])):
#                         if str(j[1]) =='NNP':
#                             linelst[i]=str(j)
#                             break
#           print(linelst)
#           newf.write(str(linelst)+ '\n')
#
# rem=[]
# E1 =['NN','NNS','NNP','NNPS']
# E2 = ['NN','NNS','NNP','NNPS']
# V=['VB','VBD','VBN','VBP','VBZ']
# from string import punctuation
# listpct=set(punctuation)
# # for filen in os.listdir("Preprocessing\\POStagsentencev2\\NoPronouns\\"):
# for filen in rand_items:
#     file = open("Unseendata\\"+ "npron"+filen, "r", encoding='utf-8')
#     newf = open("Unseendata\\"+ "N+V"+filen, "w", encoding='utf-8')
#     text=file.readlines()
#     for line in text:
#         lines=ast.literal_eval(line)
#         # print(lines)
#         for i in range(len(lines)):
#             if lines[i][0] not in listpct:
#                 if lines[i][1] in E1 or lines[i][1] in V or lines[i][0]==',':
#                     # del lines[i]
#                     rem.append(lines[i])
#         newf.write(str(rem) + "\n")
#         rem=[]
#
# # ### pairs of 3 N V N
# # for filen in os.listdir("Preprocessing\\POStagsentencev2\\NoPronouns\\"):
# for filen in rand_items:
#     file = open("Unseendata\\"+ "N+V"+filen, "r", encoding='utf-8')
#     newf = open("Unseendata\\"+ "N+Vpair"+filen, "w", encoding='utf-8')
#     text=file.readlines()
#     for line in text:
#         lines=ast.literal_eval(line)
#         lines=[lines[i] for i in range(len(lines)) if lines[i][0] != ',']
#         # print(lines)
#         rel_list=[]
#         i=0
#         # for i in range(len(lines)):
#         while i+2 < len(lines)-1:
#                 if lines[i][1].startswith('N') and lines[i+1][1].startswith('V') and lines[i+2][1].startswith('N'):
#                     rel_list.append(lines[i])
#                     rel_list.append(lines[i+1])
#                     rel_list.append(lines[i + 2])
#                 i=i+1
#                 if len(rel_list)==3:
#                     # print(rel_list)
#                     newf.write(str(rel_list) + "\n")
#                     rel_list=[]

model = load_model("NNFactallv2.h5")
model.load_weights("NNFactwallv2.h5")
# model=pickle.load(open('SVMEmbv2.sav', 'rb'))
# model=pickle.load(open('SVMEmb+POSv2.sav', 'rb'))
# model=pickle.load(open('RandomForestEmbv2.sav', 'rb'))
# model=pickle.load(open('RandomForestEmb+POSv2.sav', 'rb'))
E1 = ['NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBN', 'VBP', 'VBZ']
n=[0] * 100
def class_assigment(y):
    classes=[]
    for item in y:
        if item>0.8:
            classes.append(1)
        else:
            classes.append(0)
    return classes
for files in os.listdir('Unseendata\\Classification\\sample'):
    df =open("Unseendata\\Classification\\sample\\"+files, "r", encoding='utf-8')
    newf=open("Unseendata\\Classification\\NNv2\\Emb\\"+files,'w',encoding='utf-8')
    text=df.readlines()
    pairs=[]
    model2= gensim.models.Word2Vec.load("modfulltext_20ep.model")
    K=list(range(0,len(E1)))
    pos=dict(zip(E1,K))
    for x in text:
        # count = count + 1
        listx = ast.literal_eval(x)
        pairline = []
        for j in listx:
            # print(j[0])
            try:
                pairline.append(model2.wv[j[0]])
                # new_v = np.append(model2.wv[j[0]], pos[j[1]])
                # pairline.append(new_v)
            except:
                # new_v = np.append(n, pos[j[1]])
                # pairline.append(new_v)
                pairline.append(n)
        pairs.append(pairline)
    X=np.array(list(map(lambda x: np.concatenate(x), pairs)))
    # print(X.shape)
    ynew = model.predict(X)
    c=class_assigment(ynew)
    newf.write(str(c))
# print(c)
