#steps:Tokenizer, Sentence Splitter, POS Tagger, Named-entity Recognizer, and Parser (Constituency and Dependency)->the Berkeley Parser
Actor=['physician','expert','company','judge','prosecutor','driver','officer','inspector']
Artifact=['document','agreement','certificate','licence','permit','warrant','pass']
Condition=['if','in case of','provided that','in the context of','limit','who','whose','which']
Exception=['with the exception of ','except for','derogation','apart from','other than']
Location=['site','place','street','intersection','pedestrian crossing','railway track']
Modality= ['may', 'must','shall','can','need to','is authorized to','is prohibited from']
Reason=['in order to', 'for the purpose of','so as to','so that','in the interest of','in view of']
Sanction=['punishment','jail sentence','imprisonment','prison term','fine']
Situation=['renewal','inspection','parking','registration','deliberation']
Time = ['before','after','temporary','permanent','period','day','year','month','date']
Violation=['offence','crime','misdemeanor','civil wrong','infraction','transgression']

import nltk
import os
from nltk.tokenize import word_tokenize
#tried malt parser, useless


#########sentence splitter + tokenizer + POS
# directorys="TregexRules\\Preprocessed"
# directory="TregexRules"
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# filename=os.listdir(directory)
# for filen in filename:
#     file = open(directory + "\\" + filen, "r", encoding='utf-8')
#     newf = open(directorys + "\\" +"stpos" +filen, "w", encoding='utf-8')
#     text=file.readlines()
#     for line in text:
#         tokens=tokenizer.tokenize(line)
#         for tok in tokens:
#             results=word_tokenize(tok)
#             resultpos = nltk.pos_tag(results)
#             newf.write(str(resultpos) + '\n')



# from nltk.parse.malt import MaltParser
# mp = MaltParser('C:\\Users\\i6167189\\AppData\\Local\\Python\\Python36\\maltparser-1.8.1', 'C:\\Users\\i6167189\\AppData\\Local\\Python\\Python36\\engmalt.poly-1.7.mco')
# sent1 = 'I shot an elephant in my pajamas .'.split()
# print(mp.parse_one(sent1).tree())



import os
from nltk.parse import stanford
from nltk.parse import CoreNLPParser


parser = CoreNLPParser(url='http://localhost:9000')

##server error
# directorys="TregexRules\\Parsed"
# directory="TregexRules"
# filename=os.listdir(directory)
# for filen in filename:
#     file = open(directory + "\\" + filen, "r", encoding='utf-8')
#     newf = open(directorys + "\\" +"pars" +filen, "w", encoding='utf-8')
#     text=file.readlines()
#     for line in text:
#         par=parser.raw_parse(line)
#         newf.write(str(list(par)) + '\n')
##
import requests

url = "http://localhost:9000/tregex"

# request_params = {"pattern": "(NP[$VP]>S)|(NP[$VP]>S\\n)|(NP\\n[$VP]>S)|(NP\\n[$VP]>S\\n)"}
#action
# request_params = {"pattern": "VP"}
request_params={"pattern":"NP < (judge)"}
# request_params={"pattern":"•(NP(!<<(((violation(marker)(|((!<<((time(marker)(|((!<<((situation(marker)((|(!<<((sanction(marker)(|((!<<((reference(marker)(|((!<<((location(marker)(|((!<<((actor(marker)"}

text = "judge Pusheen  and  judge Smitha judge walked along the beach judge ran t the car judge ."
r = requests.post(url, data=text, params=request_params)
print(r.json())