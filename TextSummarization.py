import spacy
nlp = spacy.load('C:\\Users\\i6167189\\PycharmProjects\\neuralcoref\\en_coref_md-3.0.0\\en_coref_md')
doc = nlp(u'My sister has a dog. She loves him.')

doc._.has_coref
doc._.coref_clusters