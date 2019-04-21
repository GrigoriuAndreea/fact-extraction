
######Extraction based on pattern ( all kinds of info) -> get_x() , where x is type of info
# import lexnlp.extract.en.amounts
# import lexnlp.extract.en.citations
# import lexnlp.extract.en.conditions
# import lexnlp.extract.en.constraints
# import lexnlp.extract.en.copyright
# import lexnlp.extract.en.courts
# import lexnlp.extract.en.dates
# import lexnlp.extract.en.definitions
# import lexnlp.extract.en.distances
# import lexnlp.extract.en.durations
# import lexnlp.extract.en.geoentities
# import lexnlp.extract.en.money
# import lexnlp.extract.en.percents
# import lexnlp.extract.en.pii
# import lexnlp.extract.en.ratios
# import lexnlp.extract.en.regulations
# import lexnlp.extract.en.trademarks
# import lexnlp.extract.en.urls
import os
####Extraction based on tagged POS classifiers
import lexnlp
##### NER with NLTK maximum entropy classifier
# nltk.download('all')
from lexnlp.extract.en.entities.nltk_maxent import get_companies
from lexnlp.extract.en.entities.nltk_maxent import get_geopolitical
from lexnlp.extract.en.entities.nltk_maxent import get_persons

######## NER with NLTK and regular expressions
from lexnlp.extract.en.entities.nltk_re import get_companies
from lexnlp.extract.en.entities.nltk_re import get_parties_as

######## NER with Stanford Named Entity Recognition (NER) models
from lexnlp.extract.en.entities.stanford_ner import get_persons
from lexnlp.extract.en.entities.stanford_ner import get_locations
from lexnlp.extract.en.entities.stanford_ner import get_organizations


#####Maxent
directory="CaseLawGEcutfacts"
filename=os.listdir(directory)
persons=[]
geopolitical=[]
companies=[]
for j in range(0,10):
    file=open(directory+"\\"+filename[j],"r",encoding='utf-8')
    newf = open("LEXNLP_annotations\\Maxent\\" + filename[j], 'w', encoding='utf-8')
    text=file.readlines()
    for line in text:
            persons.append(list(lexnlp.extract.en.entities.nltk_maxent.get_persons(line)))
            geopolitical.append(list(lexnlp.extract.en.entities.nltk_maxent.get_geopolitical(line)))
            companies.append(list(lexnlp.extract.en.entities.nltk_maxent.get_companies(line)))
    newf.write("Persons\n")
    newf.write(str(persons)+'\n')
    persons=[]
    newf.write("Geopolitical\n")
    newf.write(str(geopolitical)+'\n')
    geopolitical=[]
    newf.write("Companies\n")
    newf.write(str(companies)+'\n')
    companies = []

####Regular expressions-> performs extremely BAD!!!
# directory="CaseLawGEcutfacts"
# filename=os.listdir(directory)
# parties=[]
# companies=[]
# for j in range(0,10):
#     file=open(directory+"\\"+filename[j],"r",encoding='utf-8')
#     newf = open("LEXNLP_annotations\\Regex\\" + filename[j], 'w', encoding='utf-8')
#     text=file.readlines()
#     for line in text:
#             parties.append(list(lexnlp.extract.en.entities.nltk_re.get_parties_as(line)))
#             companies.append(list(lexnlp.extract.en.entities.nltk_re.get_companies(line)))
#     newf.write("Parties\n")
#     newf.write(str(parties)+'\n')
#     parties=[]
#     newf.write("Companies\n")
#     newf.write(str(companies)+'\n')
#     companies = []

####STANFORD
directory="CaseLawGEcutfacts"
filename=os.listdir(directory)


persons=[]
locations=[]
organizations=[]
for j in range(0,10):
    file=open(directory+"\\"+filename[j],"r",encoding='utf-8')
    newf = open("LEXNLP_annotations\\Stanford\\" + filename[j], 'w', encoding='utf-8')
    text=file.readlines()
    for line in text:
            persons.append(list(lexnlp.extract.en.entities.stanford_ner.get_persons(line)))
            locations.append(list(lexnlp.extract.en.entities.stanford_ner.get_locations(line)))
            organizations.append(list(lexnlp.extract.en.entities.stanford_ner.get_organizations(line)))
    newf.write("Persons\n")
    newf.write(str(persons)+'\n')
    persons=[]
    newf.write("Locations\n")
    newf.write(str(locations)+'\n')
    locations=[]
    newf.write("Organizations\n")
    newf.write(str(organizations)+'\n')
    organizations = []