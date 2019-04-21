# https://hudoc.echr.coe.int/eng#{%22languageisocode%22:[%22ENG%22],%22documentcollectionid2%22:[%22GRANDCHAMBER%22,%22CHAMBER%22]}
# https://hudoc.echr.coe.int/eng#{%22itemid%22:[%22001-190028%22]}
import requests
import  json
import  os
import urllib.request
##45
# newf=open("itemid_gender_equality2.txt",'w',encoding='utf-8')
# newtitle=open('title_gender_equality2.txt','w',encoding='utf-8')
# # response=requests.get('https://hudoc.echr.coe.int/app/query/results?query=contentsitename%3AECHR%20AND%20(NOT%20(doctype%3DPR%20OR%20doctype%3DHFCOMOLD%20OR%20doctype%3DHECOMOLD))%20AND%20(gender%20equality)%20AND%20((documentcollectionid%3D%22GRANDCHAMBER%22)%20OR%20(documentcollectionid%3D%22CHAMBER%22))&select=sharepointid,Rank,ECHRRanking,languagenumber,itemid,docname,doctype,application,appno,conclusion,importance,originatingbody,typedescription,kpdate,kpdateAsText,documentcollectionid,documentcollectionid2,languageisocode,extractedappno,isplaceholder,doctypebranch,respondent,ecli,appnoparts,sclappnos&sort=&start=20&length=100&rankingModelId=22222222-eeee-0000-0000-000000000000')
# response=requests.get("https://hudoc.echr.coe.int/app/query/results?query=contentsitename%3AECHR%20AND%20(NOT%20(doctype%3DPR%20OR%20doctype%3DHFCOMOLD%20OR%20doctype%3DHECOMOLD))%20AND%20((languageisocode%3D%22ENG%22))%20AND%20((kpthesaurus%3D%22464%22))%20AND%20((documentcollectionid%3D%22GRANDCHAMBER%22)%20OR%20(documentcollectionid%3D%22CHAMBER%22))&select=sharepointid,Rank,ECHRRanking,languagenumber,itemid,docname,doctype,application,appno,conclusion,importance,originatingbody,typedescription,kpdate,kpdateAsText,documentcollectionid,documentcollectionid2,languageisocode,extractedappno,isplaceholder,doctypebranch,respondent,ecli,appnoparts,sclappnos&sort=&start=20&length=100&rankingModelId=11111111-0000-0000-0000-000000000000")
# parsed=json.loads(response.content)
# for x in range (len(parsed["results"])):
#     # print(parsed["results"][x]["columns"]["itemid"])
#     newf.write(parsed["results"][x]["columns"]["itemid"]+ "\n")
# for x in range (len(parsed["results"])):
#     # print(parsed["results"][x]["columns"]["itemid"])
#     newtitle.write(parsed["results"][x]["columns"]["docname"]+ "\n")

# file=open("itemid_gender_equality2.txt","r")
# # filetitle=open('title_gender_equality.txt','r')
#
# base_url = "http://hudoc.echr.coe.int/app/conversion/docx/?library=ECHR&filename=please_give_me_the_document.docx&id="
# from time import sleep
# with open("itemid_gender_equality2.txt", 'r') as IDlist:
#     for docID in IDlist:
#         filename = "%s.docx"%(docID.strip())
#         filename = os.path.join('CaseLawGenderEquality', filename)
#         url = base_url + docID.strip()
#         r = requests.get(url, stream=True)
#         if not r.ok:
#             print("Failed to fetch document %s"%(docID))
#             print("URL: %s"%(url))
#             # print("Permalink: %s"%(perma_url + docID.strip()))
#             continue
#         with open(filename, 'wb') as f:
#             for block in r.iter_content(1024):
#                 f.write(block)
#         print("request complete, see %s"%(filename))

###all documents
import requests
import json
import os
from time import sleep
length=500
newtitle=open('title_committee.txt','w',encoding='utf-8')
#cache the list of all document IDs
base_url="https://hudoc.echr.coe.int/app/query/results?query=contentsitename%3AECHR%20AND%20(NOT%20(doctype%3DPR%20OR%20doctype%3DHFCOMOLD%20OR%20doctype%3DHECOMOLD))%20AND%20((languageisocode%3D%22ENG%22))%20AND%20((documentcollectionid%3D%22GRANDCHAMBER%22)%20OR%20(documentcollectionid%3D%22CHAMBER%22))&select=sharepointid,Rank,ECHRRanking,languagenumber,itemid,docname,doctype,application,appno,conclusion,importance,originatingbody,typedescription,kpdate,kpdateAsText,documentcollectionid,documentcollectionid2,languageisocode,extractedappno,isplaceholder,doctypebranch,respondent,ecli,appnoparts,sclappnos,echradvopidentifier,echradvopstatus&sort=&rankingModelId=11111111-0000-0000-0000-000000000000"
with open("listOfIDscom.txt", 'w') as IDlist:
    #fetch all index pages up to the current result count
    for start in range(0,19173, length):
        print("Fetching and writing %d.json"%(start))
        with open("%d.json"%(start), 'wb') as f:
            url = base_url + "&start=%d&length=%d"%(start, length)
            r = requests.get(url, stream=True)
            if not r.ok:
                print("Failed to fetch %d to %d"%(start, length))
                continue
            for block in r.iter_content(1024):
                f.write(block)
        jsonObject = json.load(open("%d.json"%(start),'r',encoding='utf-8'))
        for item in jsonObject['results']:
            IDlist.write("%s%s"%(item['columns']['itemid'], os.linesep))
            newtitle.write("%s%s"%(item['columns']['docname'], os.linesep))
file=open("listOfIDscom.txt","r")
filetitle=open('title_alldoccom.txt','r')

base_url = "http://hudoc.echr.coe.int/app/conversion/docx/?library=ECHR&filename=please_give_me_the_document.docx&id="
i=0
error_ids=open("wrongids.txt",'w')
with open("listOfIDs.txt", 'r') as IDlist:
    for docID in IDlist:
        if docID.strip() != "":
            filename = "%s.docx"%(docID.strip())
            if not os.path.isfile("CaseLawcomplete\\"+filename):
                filename = os.path.join('CaseLawcomplete', filename)
                url = base_url + docID.strip()
                r = requests.get(url, stream=True)
                if not r.ok:
                    # print("Failed to fetch document %s"%(docID))
                    # print("URL: %s"%(url))
                    # print("Permalink: %s"%(perma_url + docID.strip()))
                    error_ids.write(docID+"\n")
                    # print(docID)
                    continue
                with open(filename, 'wb') as f:
                    for block in r.iter_content(1024):
                        f.write(block)
                print("request complete, see %s"%(filename))
