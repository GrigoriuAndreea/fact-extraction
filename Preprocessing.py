import os
import ast
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
from nltk.metrics import *
from pyjarowinkler import distance
####Extraction based on tagged POS classifiers
import lexnlp
import lexnlp.nlp.en.tokens
from nltk.tag import StanfordPOSTagger
from lexnlp.config.stanford import STANFORD_POS_PATH
import nltk
# import
##### NER with NLTK maximum entropy classifier
# nltk.download('all')
from lexnlp.extract.en.entities.nltk_maxent import get_companies
from lexnlp.extract.en.entities.nltk_maxent import get_geopolitical
from lexnlp.extract.en.entities.nltk_maxent import get_persons
####STANFORD
from lexnlp.extract.en.entities.stanford_ner import get_persons
from lexnlp.extract.en.entities.stanford_ner import get_locations
from lexnlp.extract.en.entities.stanford_ner import get_organizations
import time
from string import punctuation
listpct=set(punctuation)
####STANFORD
# start=time.time()
# print(start)
# directory="CaseLawGEcutfacts"
# filename=os.listdir(directory)
# persons=[]
# locations=[]
# organizations=[]
# for filename in os.listdir(directory):
#     file=open(directory+"\\"+filename,"r",encoding='utf-8')
#     newf = open("Preprocessing\\TimeTest\\StanfordNER\\" + filename, 'w', encoding='utf-8')
#     text=file.readlines()
#     for line in text:
#             persons.append(list(lexnlp.extract.en.entities.stanford_ner.get_persons(line)))
#             locations.append(list(lexnlp.extract.en.entities.stanford_ner.get_locations(line)))
#             organizations.append(list(lexnlp.extract.en.entities.stanford_ner.get_organizations(line)))
#     newf.write("Persons\n")
#     newf.write(str(persons)+'\n')
#     persons=[]
#     newf.write("Locations\n")
#     newf.write(str(locations)+'\n')
#     locations=[]
#     newf.write("Organizations\n")
#     newf.write(str(organizations)+'\n')
#     organizations = []
# end=time.time()-start
# print(str(time.time()-1553704654.5984917))


##############Entities with Maxent
# start2=time.time()
# print(start2)
# directory="CaseLawGEcutfacts"
# filename=os.listdir(directory)
# persons=[]
# geopolitical=[]
# companies=[]
# for filename in os.listdir(directory):
#     file=open(directory+"\\"+filename,"r",encoding='utf-8')
#     newf = open("Preprocessing\\TimeTest\\EntitiesMaxEnt\\" +filename, 'w', encoding='utf-8')
#     text=file.readlines()
#     for line in text:
#             persons.append(list(lexnlp.extract.en.entities.nltk_maxent.get_persons(line)))
#             geopolitical.append(list(lexnlp.extract.en.entities.nltk_maxent.get_geopolitical(line)))
#             companies.append(list(lexnlp.extract.en.entities.nltk_maxent.get_companies(line)))
#     newf.write("Persons\n")
#     newf.write(str(persons)+'\n')
#     persons=[]
#     newf.write("Geopolitical\n")
#     newf.write(str(geopolitical)+'\n')
#     geopolitical=[]
#     newf.write("Companies\n")
#     newf.write(str(companies)+'\n')
#     companies = []
# end2=time.time()-start2
# print("Time"+str(end2))
# print(lexnlp.nlp.en.tokens.get_tokens_list(text))
#########sentence splitter + tokenizer + POS
# directory="CaseLawGEcutfacts"
# filen=os.listdir(directory)
# directory="Preprocesing\\POStag\\"
# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# STANFORD_DEFAULT_TAG_MODEL = os.path.join(STANFORD_POS_PATH, "models", "english-bidirectional-distsim.tagger")
# STANFORD_POS_FILE = os.path.join(STANFORD_POS_PATH, "stanford-postagger.jar")
# STANFORD_TAGGER = StanfordPOSTagger(STANFORD_DEFAULT_TAG_MODEL, STANFORD_POS_FILE)
# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# # pos = STANFORD_TAGGER.tag(tokens)
#
# for filen in os.listdir(directory):
#     file = open(directory + "\\" + filen, "r", encoding='utf-8')
#     newf = open("Preprocessing\\POStagsentence\\"  + filen, "w", encoding='utf-8')
#     text=file.readlines()
#     for line in text:
#         # tokens=lexnlp.nlp.en.tokens.get_token_list(line)
#         tokens = tokenizer.tokenize(line)
#         for tok in tokens:
#             token = lexnlp.nlp.en.tokens.get_tokens(tok,stopword=False)
#             pos = STANFORD_TAGGER.tag(token)
#         # print(pos)
#             newf.write(str(pos) + '\n')


###get title for each id
# titles = [line.rstrip('\n') for line in open('title_gender_equality2(45).txt')]
# ids = [line.rstrip('\n') for line in open('itemid_gender_equality2(45).txt')]
# casedict=dictionary = dict(zip(ids, titles))
# # print(casedict)
# orgdict=dictionary = dict(zip(ids, titles))
#
# # print(orgdict)
# listt=[]
# for key,value in orgdict.items():
#     listt=value
#     listt=value.split('v.')
#     # print(list[0])
#     listt[0]=listt[0].split('OF ')
#     orgdict[key]=(listt[0][1])
#     # print(value)
# # print(casedict)
# # print(orgdict)
#
# appliclist=["applicant","applicants"]
#
# directory="Preprocessing\\POStagsentence\\"
#########add applicant from title
# for filen in os.listdir(directory):
#     file = open(directory  + filen, "r", encoding='utf-8')
#     newf = open(directory +"POSnoapp\\"+ filen, 'w', encoding='utf-8')
#     text=file.readlines()
#     id=filen.rstrip('.txt')
#     app=orgdict[id]
#     print(app)
#     for line in text:
#         lines=ast.literal_eval(line)
#         lis=[list(elem) for elem in lines]
#         for i in range(len(lis)):
#             if lis[i][0].lower() in appliclist:
#                 lis[i][0]=app
#         newf.write(str(lis)+ '\n')

# directoryw="Preprocessing\\"
# directoryentmax=directoryw+"EntitiesMaxEnt\\"
# directoryentsta=directoryw+"StanfordNER\\"

directory="Preprocessing\\POStagsentence\\POSnoapp\\"

# ########Lemmatization
# for filen in os.listdir(directory):
#     file = open(directory  + filen, "r", encoding='utf-8')
#     newf=open(directory+"Lemversion\\"+filen,"w", encoding='utf-8')
#     text=file.readlines()
#     for line in text:
#         lines=ast.literal_eval(line)
#         for i in range(len(lines)):
#             lines[i][0]=lemmatizer.lemmatize(lines[i][0].lower())
#         newf.write(str(lines)+"\n")
#
# Extraction
grammar="""F:"""
E1 =['NN','NNS','NNP','NNPS']
E2 = ['NN','NNS','NNP','NNPS']
V=['VB','VBD','VBN','VBP','VBZ']

# for i in E1:
#     for j in E2:
#         for a in V:
#           str=" { < "+i+ "> ? <" +a+" > * <" +j+ ">}"
#           grammar=grammar +str+ "\n"
          # print(str)

# cp = nltk.RegexpParser(grammar)
# result = cp.parse(sentence)
# rem=[]
# for filen in os.listdir(directory):
#     # file = open(directory+"Lemversion\\"  + filen, "r", encoding='utf-8')
#     file = open(directory + filen, "r", encoding='utf-8')
#     newf = open(directory + "N+V\\" + filen, "w", encoding='utf-8')
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
            # if lines[i][1].startswith('N'):
                # print(lines[i][0])
            # if lines[i][1].startswith('V'):
            #     print(lines[i][0])

#### pairs of 3 N V N
# for filen in os.listdir("Preprocessing\\POStagsentence\\POSnoapp\\"):
#     file = open("Preprocessing\\POStagsentence\\POSnoapp\\" +"N+V\\"+ filen, "r", encoding='utf-8')
#     newf = open("Preprocessing\\POStagsentence\\POSnoapp\\" + "N+Vpairs\\" + filen, "w", encoding='utf-8')
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
#build list of entities from Stanford
ent_d={}
temp=[]

for filen in os.listdir("Preprocessing\\StanfordNER\\"):
    file = open( "Preprocessing\\StanfordNER\\"+filen, "r", encoding='utf-8')
    # file = open("Preprocessing\\EntitiesMaxEnt\\" + filen, "r", encoding='utf-8')
    filen=filen.split(".")
    # ent_d[filen[0]]=
    text = file.readlines()
    for line in text:
        # print(list(line))
        if line not in ["Persons\n","Locations\n","Organizations\n"]:
        ###MaxEnt
        # if line not in ["Persons\n", "Geopolitical\n", "Companies\n"]:
            lines = ast.literal_eval(line)
            lines=[x for x in lines if x!=[]]
            lines=[x for sub_list in lines for x in sub_list]
            lines=list(set(lines))
            temp.append(lines)
            lines=[]
    ent_d[filen[0]] =temp
    temp=[]

# newf = open("Preprocessing\\" +"NVpairsMaxEnt.txt" , "w", encoding='utf-8')
newf = open("Preprocessing\\" +"NVpairsStandford22.txt" , "w", encoding='utf-8')
count=0
pairs=[]
## build file with list where N from Entity Stanford,
for filer in os.listdir("Preprocessing\\POStagsentence\\POSnoapp\\" +"N+Vpairs\\"):
    file = open("Preprocessing\\POStagsentence\\POSnoapp\\" +"N+Vpairs\\"+ filer, "r", encoding='utf-8')
    text2 = file.readlines()
    filer=filer.split('.')
    # print(filer[0])
    # for linie in text2:
    #     linii = ast.literal_eval(linie)
    #     lista=[y for x in ent_d[filer[0]] for y in x]
    #     count=count+1
    for linie in text2:
        count = count + 1
        linii = ast.literal_eval(linie)
        lista = [y for x in ent_d[filer[0]] for y in x]
        for l in linii:
                    if any(l[0] in s for s in lista) and linie not in pairs:
                        pairs.append(linie)


for p in pairs:
    newf.write(p)
        # print(lista)
#         for l in linii:
#             # print(l)
#             for i in range(len(lista)):
#                 # #####jaro_winkler
#
#                 if type(lista[i])==tuple:
#                     dist=distance.get_jaro_distance(l[0], lista[i][0], winkler=True, scaling=0.1)
#                     if dist>=0.8:
#                       newf.write(linie)
#                       # print(linie)
#                       break
#
#                 else:
#                     dist = distance.get_jaro_distance(l[0], lista[i], winkler=True, scaling=0.1)
#                     if dist>=0.8:
#                       newf.write(linie)
#                       #   print(linie)
#                       break
# #                     # print (l,e)
# #             ###levenstein->bad
# #                 # dist = edit_distance(e, l[0])
# #                 # if dist < 1:
# #                 #     print(l, e)

#
#
print(count)