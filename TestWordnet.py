from nltk.corpus import wordnet as wn
import os
import ast
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer

print(wn.synsets('dog')) # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
# [Synset('dog.n.01'), Synset('frump.n.01'), Synset('dog.n.03'), Synset('cad.n.01'),
# Synset('frank.n.02'), Synset('pawl.n.01'), Synset('andiron.n.01'), Synset('chase.v.01')]
hit= wn.synsets('hit', pos=wn.VERB) ### get sets of synonyms
# for j in hit:
#     print(j.lemmas()[0].name()) ##get words from set
##Stemming->root, not always word
porter = PorterStemmer()
lancaster=LancasterStemmer()
##Lemming->lemma of the word ( an actual word)
wordnet_lemmatizer = WordNetLemmatizer()

facts=[]
factfile=open("Unseendata\\Classification\\factfile.txt",'r',encoding='utf-8')
factread=factfile.readlines()

# for file in os.listdir("Unseendata\\Classification\\sample\\"):
#     f = open("Unseendata\\Classification\\NN\\Emb\\" +"Emb"+ file, "r", encoding='utf-8')
#     label = f.readlines()
#     labels=ast.literal_eval(label[0])
#     print(type(labels))
#     pairs=open("Unseendata\\Classification\\sample\\" + file, "r", encoding='utf-8')
#     pairst=pairs.readlines()
#     pairlist=[]
#     for l in pairst:
#         pairlist.append(ast.literal_eval(l))
#     for j in range(len(pairlist)):
#         if labels[j]==1:
#             factfile.write(str(pairlist[j])+"\n")
#             facts.append(pairlist[j])

    # print(pairlist)
    # print(label)
nounfile=open('nounfile.txt','a',encoding='utf-8')
for line in factread:
    facts.append(ast.literal_eval(line))
relations=[]
for f in facts:
    relations.append(f[1][0])
    nounfile.write(f[0][0]+'\n')
    nounfile.write(f[2][0]+'\n')

relations_stem_lan=[]
relations_stem_port=[]
relations_lem=[]
for r in relations:
    relations_stem_lan.append(lancaster.stem(r)) #LancasterStemmer is simple, but heavy stemming due to iterations and over-stemming may occur.
                                                    #  Over-stemming causes the stems to be not linguistic, or they may have no meaning.
    relations_stem_port.append(porter.stem(r)) ##better -> **PorterStemmer algorithm does not follow
                                                            # linguistics rather a set of 05 rules for different cases that are applied in phases (step by step) to generate stems**.
    relations_lem.append(wordnet_lemmatizer.lemmatize(r))###best option
# print(len(relations_stem_lan))
# print(len(relations_stem_port))
print(relations_lem)
unique_rel = set(relations_lem)

unique_rel2 = set(relations)
# print(unique_rel)
# print(len(unique_rel))
print(len(unique_rel2))
print(unique_rel2)
#######find words
def get_word_synonyms(word, list):
    word_synonyms = []
    for synset in wn.synsets(word):
        for lemma in synset.lemma_names():
            if lemma in list and lemma != word and lemma not in word_synonyms:
                word_synonyms.append(lemma)
    return word_synonyms

# word = "happy"
# sent = ['I', 'am', 'glad', 'it', 'was', 'felicitous', '.']
for word in unique_rel:
    word_synonyms = get_word_synonyms(word, unique_rel)
    print(word)
    print(word_synonyms)