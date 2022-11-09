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

simi_dict = {}
def getsimilarity(big_sentence, big_sentences):
    s1 = str(big_sentence)
    for sentence in big_sentences:
        s2 = str(sentence)
        print(s1)
        print(s2)
        sim = big_sentence.similarity(sentence)
        print(sim)
        if int(sim) < 1:
            simi_dict[s1+" <-> "+s2] = float(sim)


nlp = spacy.load("en_core_web_lg")
#doc = nlp(response.text)
doc = nlp("Jim is there. John sank back. The carriage stopped at the Rectory. She got out to Katty. John is O.K. too. Jim is OK too.")
big_sentences = []
first_word_in_15th_sentence = ''
first_word_in_3rd_sentence = ''
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
    if(len(sent)>4):
        big_sentences.append(sent)
    if scount == 15:
        for word in sent:
            first_word_in_15th_sentence = word
            break
    if scount == 3:
        for word in sent:
            first_word_in_3rd_sentence = word
            break        

print("Token count: "+str(tcount))
print("Verb count: "+str(vcount))
print("Sentence count: "+str(scount))
print(big_sentences)
for big_sentence in big_sentences:
    getsimilarity(big_sentence, big_sentences)
print(simi_dict)
res0 = max(simi_dict, key=simi_dict.get)
print("Most similar sentence: ")
print(res0)
print("Similarity: "+str(simi_dict[res0]))
simi_dict1 = {key:val for key, val in simi_dict.items() if val != simi_dict[res0]}
res1 = max(simi_dict1, key=simi_dict1.get)
print("2nd Most similar sentence: ")
print(res1)
print("Similarity: "+str(simi_dict1[res1]))


# getting max frequency
print(named_entities)
res = max(named_entities, key=named_entities.get)
print("Most frequent named entity: ")
print(res)


print("first_word_in_3rd_sentence is: ")
print(str(first_word_in_3rd_sentence))
print("Vector for first_word_in_3rd_sentence:")
print(first_word_in_3rd_sentence.vector_norm)

print("first_word_in_15th_sentence is: ")
print(str(first_word_in_15th_sentence))
print("Vector for first_word_in_15th_sentence:")
print(first_word_in_15th_sentence.vector_norm)
