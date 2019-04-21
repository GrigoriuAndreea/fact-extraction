import spacy
nlp = spacy.load('en_core_web_md')
doc1=nlp('Office indicted B')
doc2=nlp('Office extended indictment')
print(doc1[0].similarity(doc2[0]))