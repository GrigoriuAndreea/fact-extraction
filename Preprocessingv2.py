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

grammar =r"""
    NP: {<DT>?<JJ>*<NN>}
    NP: {<NN>?<NN>}
    NP: {<NNP>}
    NP:{<NNP>?<NN>}
    VP:{<V.>}
"""
directory="Preprocessing\\POStagsentencev2\\"
# >>> cp = nltk.RegexpParser(grammar) [3]
# >>> result = cp.parse(sentence)
# cp = nltk.RegexpParser(grammar)
# for filen in os.listdir(directory):
#     file = open(directory + filen, "r", encoding='utf-8')
#     # newf = open(directory + "N+Vpairs\\" + filen, "w", encoding='utf-8')
#     text=file.readlines()
#     for line in text:
#         lines = ast.literal_eval(line)
#         tup= [tuple(i) for i in lines]
#         tree = cp.parse(tuple(tup))
#         for subtree in tree.subtrees():
#             if subtree.label() == 'NP':
#                 print(subtree)
#             if subtree.label() == 'VP':
#                 print(subtree)
# #         # blob=TextBlob(str(text))
# #         # print(blob.noun_phrases)
# ##build list of entities from Stanford
# ent_d={}
# temp=[]
# for filen in os.listdir("Preprocessing\\StanfordNER\\"):
#     file = open( "Preprocessing\\StanfordNER\\"+filen, "r", encoding='utf-8')
#     filen=filen.split(".")
#     # ent_d[filen[0]]=
#     text = file.readlines()
#     for line in text:
#         # print(list(line))
#         if line not in ["Persons\n","Locations\n","Organizations\n"]:
#         ###MaxEnt
#         # if line not in ["Persons\n", "Geopolitical\n", "Companies\n"]:
#             lines = ast.literal_eval(line)
#             lines=[x for x in lines if x!=[]]
#             lines=[x for sub_list in lines for x in sub_list]
#             lines=list(set(lines))
#             temp.append(lines)
#             lines=[]
#     ent_d[filen[0]] =temp
#     temp=[]
# for filen in os.listdir(directory):
#     file = open(directory + filen, "r", encoding='utf-8')
#     text = file.readlines()
#     fileid=filen.split(".")
#     l=[j for i in ent_d[fileid[0]] for j in i]
#     # print(l)
#     for line in text:
#        if any(ext in line for ext in l):
#           line=ast.literal_eval(line)
#           if str(line[1]).startswith('V'):
#               print(line[1])
    # for line in text:

######
###get title for each id
titles = [line.rstrip('\n') for line in open('title_alldoc.txt')]
ids = [line.rstrip('\n') for line in open('listOfIDS.txt')]
casedict=dictionary = dict(zip(ids, titles))
# print(casedict)
orgdict=dictionary = dict(zip(ids, titles))

# print(orgdict)
listt=[]
for key,value in orgdict.items():
    listt=value.split('v.')
    # print(list[0])
    listt[0]=listt[0].split('OF ')
    orgdict[key]=(listt[0][1])
    # print(value)
# print(casedict)
# print(orgdict)

appliclist=["applicant","applicants"]
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# directory="CaseLawGEcutfacts\\"
########add applicant from title
# for filen in os.listdir(directory):
#     file = open(directory  + filen, "r", encoding='utf-8')
#     newf = open("Preprocessing\\Cases45noapp\\"+ filen, 'w', encoding='utf-8')
#     text=file.readlines()
#     id=filen.rstrip('.txt')
#     app=orgdict[id]
#     for line in text:
#         # lis=line.split()
#         tokens = tokenizer.tokenize(line)
#         for tok in tokens:
#             token = lexnlp.nlp.en.tokens.get_token_list(tok,stopword=False)
#             print(token)
#             for i in range(len(token)):
#                 if token[i].lower() in appliclist:
#                     token[i]=app
#             newf.write(str(token)+ '\n')



# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# STANFORD_DEFAULT_TAG_MODEL = os.path.join(STANFORD_POS_PATH, "models", "english-bidirectional-distsim.tagger")
# STANFORD_POS_FILE = os.path.join(STANFORD_POS_PATH, "stanford-postagger.jar")
# STANFORD_TAGGER = StanfordPOSTagger(STANFORD_DEFAULT_TAG_MODEL, STANFORD_POS_FILE)
#
# # pos = STANFORD_TAGGER.tag(tokens)
# for filen in os.listdir("Preprocessing\\Cases45noapp"):
#     file = open("Preprocessing\\Cases45noapp" + "\\" + filen, "r", encoding='utf-8')
#     newf = open("Preprocessing\\POStagsentencev2\\"  + filen, "w", encoding='utf-8')
#     text=file.readlines()
#     for line in text:
#             token=ast.literal_eval(line)
#             pos = STANFORD_TAGGER.tag(token)
#         # print(pos)
#             newf.write(str(pos) + '\n')

######coreference
# file = open("Preprocessing\\POStagsentencev2\\001-57865.txt")
# print(file.readlines())
# pronouns=["she","he","they","him","her"]
# compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
# for filen in os.listdir(directory):
#     file = open("Preprocessing\\POStagsentencev2\\" + filen, "r", encoding='utf-8')
#     newf = open("Preprocessing\\POStagsentencev2\\NoPronouns\\" + filen, "w", encoding='utf-8')
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

# rem=[]
# E1 =['NN','NNS','NNP','NNPS']
# E2 = ['NN','NNS','NNP','NNPS']
# V=['VB','VBD','VBN','VBP','VBZ']
# from string import punctuation
# listpct=set(punctuation)
# for filen in os.listdir("Preprocessing\\POStagsentencev2\\NoPronouns\\"):
#     file = open("Preprocessing\\POStagsentencev2\\NoPronouns\\" + filen, "r", encoding='utf-8')
#     newf = open("Preprocessing\\POStagsentencev2\\NoPronouns\\" + "N+V\\" + filen, "w", encoding='utf-8')
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

# ### pairs of 3 N V N
# for filen in os.listdir("Preprocessing\\POStagsentencev2\\NoPronouns\\"):
#     file = open("Preprocessing\\POStagsentencev2\\NoPronouns\\" +"N+V\\"+ filen, "r", encoding='utf-8')
#     newf = open("Preprocessing\\POStagsentencev2\\NoPronouns\\" + "N+Vpairs\\" + filen, "w", encoding='utf-8')
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
##build list of entities from Stanford
ent_d={}
temp=[]
for filen in os.listdir("Preprocessing\\StanfordNER\\"):
    file = open( "Preprocessing\\StanfordNER\\"+filen, "r", encoding='utf-8')
    # file = open("Preprocessing\\EntitiesMaxEnt\\" + filen, "r", encoding='utf-8')
    filen=filen.split(".")
    # ent_d[filen[0]]=
    text = file.readlines()

    app = orgdict[filen[0]]
    for line in text:
        # print(list(line))
        if line not in ["Persons\n","Locations\n","Organizations\n"]:
        ###MaxEnt
        # if line not in ["Persons\n", "Geopolitical\n", "Companies\n"]:
            lines = ast.literal_eval(line)
            lines=[x for x in lines if x!=[]]
            lines=[x for sub_list in lines for x in sub_list]
            lines.append(app)
            lines=list(set(lines))
            temp.append(lines)
            lines=[]
    ent_d[filen[0]] =temp
    temp=[]
#
newf = open("Preprocessing\\" +"NVpairsStanfordnew.txt" , "w", encoding='utf-8')
pairs=[]
count=0
# ## build file with list where N from Entity Stanford,
for filer in os.listdir("Preprocessing\\POStagsentencev2\\NoPronouns\\" +"N+Vpairs\\"):
    file = open("Preprocessing\\POStagsentencev2\\NoPronouns\\" +"N+Vpairs\\"+ filer, "r", encoding='utf-8')
    text2 = file.readlines()
    filer=filer.split('.')
    lista = [y for x in ent_d[filer[0]] for y in x]
    # print(filer[0])
    for linie in text2:
        count=count+1
        linii = ast.literal_eval(linie)
        # print(lista)
        for l in linii:
                if any(l[0] in s for s in lista) and linie not in pairs:
                    pairs.append(linie)

                    # linie=linie+1
for p in pairs:
    newf.write(p)
print(count)
              # #####jaro_winkler
                # if type(lista[i])==tuple:
                #     dist=distance.get_jaro_distance(l[0], lista[i][0], winkler=True, scaling=0.1)
                #     if dist>=0.8:
                #       newf.write(linie)
                #       # print(linie)
                #       break
                # else:
                #     dist = distance.get_jaro_distance(l[0], lista[i], winkler=True, scaling=0.1)
                #     if dist>=0.8:
                #       newf.write(linie)
                #       # print(linie)
                #       break

