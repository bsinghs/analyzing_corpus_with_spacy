from curses.ascii import isdigit
from typing import Counter
from urllib import response
import spacy
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# base_url = "https://www.gutenberg.org/"
# url = base_url + "/browse/scores/top"
# response = requests.get(url)


# soup = BeautifulSoup(response.content, "html.parser")
# links = soup.find_all("a")

# for link in links:
#     href = link.get("href")
#     parsed = urlparse(href)
#     if parsed.path.startswith("/ebooks") and not parsed.path.endswith("/"):
#         tokens = parsed.path.split("/")
#         if len(tokens) == 3:
#             if tokens[2].isdigit():
#                 book_url = base_url+parsed.path+".txt.utf-8"
#                 print(parsed)
#                 break

# print(book_url)
# response = requests.get(book_url)

import spacy.attrs

nlp = spacy.load("en_core_web_lg")
#doc = nlp(response.text)
doc = nlp("Jim is there. John sank back. The carriage stopped at the Rectory. She got out to Katty. John is O.K.")
tcount=0
vcount=0
scount=0
import numpy as np
import pandas as pd
from collections import defaultdict

named_entities = {}
namede=[]
for token in doc:
    tcount=tcount+1
    if token.pos_ == "VERB":
        vcount = vcount+1
    #print(token.text, token.pos_, token.dep_)  
for ne in doc.ents:
    named_entity = str(ne)
    print("'"+named_entity+"'")
    count = named_entities.get(named_entity)
    if count:
        named_entities[named_entity] = count + 1
    else:
        named_entities[named_entity] = 1

for sent in doc.sents:
    scount=scount+1
    sent.
print("Token count: "+str(tcount))
print("Verb count: "+str(vcount))
# getting max frequency
print(named_entities)
res = max(named_entities, key=named_entities.get)
print("Most frequent named entity: ")
print(res)
