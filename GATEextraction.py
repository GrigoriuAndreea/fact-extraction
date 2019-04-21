from xml.etree import cElementTree as ET
# xmlstr = """
# <root>
#     <page>
#          <title>Chapter 1</title>
#          <content>Welcome to Chapter 1</content>
#     </page>
#     <page>
#         <title>Chapter 2</title>
#         <content>Welcome to Chapter 2</content>
#     </page>
# </root>
# """
# root = ET.fromstring(xmlstr)
# for page in list(root):
#     title = page.find('title').text
#     content = page.find('content').text
#     print('title: %s; content: %s' % (title, content))
#
import re
file=open("GATE_annotations\\001-57865.txt.xml",'r', encoding='utf-8')
lines=file.readlines()
for line in lines:
    title_search = re.search('<>(.*)<>', line, re.IGNORECASE)
    