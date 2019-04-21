import os
import lexnlp
import lexnlp.nlp.en.tokens
import nltk
import gensim
import ast

directory="CaseLawcutfacts"
# directory="CaseLawcompletecutfacts"
# directory="CaseLawtxt"
filen=os.listdir(directory)
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

###get title for each id
# titles = [line.rstrip('\n') for line in open('title_alldoc.txt',encoding='utf-8')]
# ids = [line.rstrip('\n') for line in open('listOfIDs.txt',encoding='utf-8')]
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
#
# appliclist=["applicant","applicants"]
# ##prepocess to list of tokens and replace applicant with title name
# for filen in os.listdir(directory):
#     file = open(directory + "\\" + filen, "r", encoding='utf-8')
#     newf = open("Preprocessing\\Embedding1000+45\\"  + filen, "w", encoding='utf-8')
#     text=file.readlines()
#     id = filen.rstrip('.txt')
#     app = orgdict[id]
#     for line in text:
#         tokens = tokenizer.tokenize(line)
#         # print(tokens)
#         for tok in tokens:
#             token = lexnlp.nlp.en.tokens.get_token_list(tok,stopword=False)
#             # print(str(token))
#             for i in range(len(token)):
#                 if token[i].lower() in appliclist:
#                     if app != "unknown":
#                             token[i]=app
#             newf.write(str(token) + '\n')

sent=[]

# get total number of sentences from files
# directoryemb="Preprocessing\\Embedding1000+45\\"
# for filen in os.listdir(directoryemb):
#     file = open(directoryemb  + filen, "r", encoding='utf-8')
#     text = file.readlines()
#     for line in text:
#         lines=ast.literal_eval(line)
#         sent.append(lines)
# #
# #
# # print(len(sent))
emb_size=100
wind_size=5
# #
# model=gensim.models.Word2Vec(sentences=sent,size=emb_size,window=wind_size,workers=4,min_count=1)
# model.train(sent, total_examples=len(sent), epochs=15)
# model.save("mod1000_15ep.model")
model= gensim.models.Word2Vec.load("modfulltext_15ep.model")
model2= gensim.models.Word2Vec.load("modfulltext_20ep.model")
model3= gensim.models.Word2Vec.load("model10000_20ep.model")
model4= gensim.models.Word2Vec.load("model10000_15ep.model")
model5= gensim.models.Word2Vec.load("mod1000_15ep.model")
model6= gensim.models.Word2Vec.load("mod1000_20ep.model")
print(model.wv.most_similar('zabezpe?ení'))
print(model2.wv.most_similar('zabezpe?ení'))
print(model3.wv.most_similar('zabezpe?ení'))
print(model4.wv.most_similar('zabezpe?ení'))
print(model5.wv.most_similar('zabezpe?ení'))
print(model6.wv.most_similar('zabezpe?ení'))
# # print(model.wv['naffra'] )
# print(len(list(model.wv.vocab)))
# print(len(list(model2.wv.vocab)))