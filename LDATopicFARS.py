import  gensim
import ast
import os


directory="FARS_annotation\\Preprocessed\\Lemm"
processed_docs=[]
filename=os.listdir(directory)
for filen in filename:
    file = open(directory + "\\" + filen, "r", encoding='utf-8')
    text=file.readlines()
    for ls in text:
        tokens=ast.literal_eval(ls)
        processed_docs.append(tokens)

dictionary = gensim.corpora.Dictionary(processed_docs)
count = 0
# for k, v in dictionary.iteritems():
#     print(k, v)
#     count += 1
#     if count > 10:
#         break
bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]
# lda_model = gensim.models.LdaMulticore(bow_corpus, num_topics=10, id2word=dictionary, passes=2, workers=2)
Lda = gensim.models.ldamodel.LdaModel
lda_model = Lda(bow_corpus, num_topics=10, id2word = dictionary, passes=50)
newf = open("FARS_annotation" + "\\" + "LDAtopicskeytermsNOsumtext.txt", "w", encoding='utf-8')
for idx, topic in lda_model.print_topics(-1):
    # print('Topic: {} \nWords: {}'.format(idx, topic))
    newf.write('Topic: {} \nWords: {}'.format(idx, topic))