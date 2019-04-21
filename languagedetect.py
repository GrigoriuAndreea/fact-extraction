import langdetect
import os
from docx import Document

# directory="CaseLawcomplete"
directory="CaseLawtxt"

filename=os.listdir(directory)
not_eng=[]
# for filename in os.listdir(directory):
#     try:
#          document = Document(directory + "\\" + filename)
#     except:
#         continue
#     file = filename.strip('docx')
#     newf = open("CaseLawtxt\\" + file + "txt", 'w', encoding='utf-8')
#     for para in document.paragraphs:
#         newf.write(para.text)

filen=open("notenglishfile.txt",'w')
for filename in os.listdir(directory):
    file = open(directory + "\\" + filename, "r", encoding='utf-8')
    text = file.readlines()
    if langdetect.detect(str(text))!='en':
        print(filename+"  "+langdetect.detect(str(text)))
        filen.write(filename)
        not_eng.append(filename)

print(len(not_eng))