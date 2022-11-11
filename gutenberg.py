"""This code scrapes one of the top scored book from gutenberg and uses spacy to analyse the book text corpus"""

from curses.ascii import isdigit
from typing import Counter
from urllib import response
import spacy
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

#utiliity function for storing similarities
simi_dict = {}
def getsimilarity(big_sentence, big_sentences):
    s1 = str(big_sentence)
    for sentence in big_sentences:
        s2 = str(sentence)
        sim = big_sentence.similarity(sentence)
        if float(sim) < 0.98:
            simi_dict[s1+" <-> "+s2] = float(sim)


#Scrape the book data
base_url = "https://www.gutenberg.org/"
url = base_url + "/browse/scores/top"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
links = soup.find_all("a")
for link in links:
    href = link.get("href")
    parsed = urlparse(href)
    if parsed.path.startswith("/ebooks") and not parsed.path.endswith("/"):
        tokens = parsed.path.split("/")
        if len(tokens) == 3:
            if tokens[2].isdigit():
                book_url = base_url+parsed.path+".txt.utf-8"
                break
print(book_url)
response = requests.get(book_url)

#Use Spacy for NLP
nlp = spacy.load("en_core_web_lg")
doc = nlp(response.text)
big_sentences = []
first_word_in_15th_sentence = ''
tcount=0
vcount=0
scount=0
named_entities = {}

#Get verb and token count
for token in doc:
    tcount=tcount+1
    if token.pos_ == "VERB":
        vcount = vcount+1

#Get named entitiies
for ne in doc.ents:
    named_entity = str(ne)
    count = named_entities.get(named_entity)
    if count:
        named_entities[named_entity] = count + 1
    else:
        named_entities[named_entity] = 1

#Get Sentences
for sent in doc.sents:
    scount=scount+1
    if(len(sent)>10):
        big_sentences.append(sent)
    if scount == 15:
        for word in sent:
            first_word_in_15th_sentence = word
            break       

#Print results
print("Token count: "+str(tcount))
print("Verb count: "+str(vcount))
print("Sentence count: "+str(scount))
for big_sentence in big_sentences:
    getsimilarity(big_sentence, big_sentences)
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
res = max(named_entities, key=named_entities.get)
print("Most frequent named entity: ")
print(res)

print("first_word_in_15th_sentence is: ")
print(str(first_word_in_15th_sentence))
print("Vector for first_word_in_15th_sentence:")
print(first_word_in_15th_sentence.vector_norm)

"""
(.venv) (base) BhajanpreetsMBP:analyzing_corpus_with_spacy bhajanpreetsingh$ /Users/bhajanpreetsingh/dev/analyzing_corpus_with_spacy/.venv/bin/python /Users/bhajanpreetsingh/dev/analyzing_corpus_with_spacy/gutenberg.py
https://www.gutenberg.org//ebooks/2641.txt.utf-8
Token count: 95392
Verb count: 10588
Sentence count: 5751


Most similar sentence: 
Surely it was better not to speak until I felt
certain.” <-> I
was not meant to understand it.”


Similarity: 0.9796569347381592
2nd Most similar sentence: 
“I said: ‘Dear Mrs. Vyse, Cecil has just asked my permission about it,
and I should be delighted, if Lucy wishes it. <-> “Then the whole thing runs: ‘Dear Mrs. Vyse.—Cecil has just asked my
permission about it, and I should be delighted if Lucy wishes it, and I
have told Lucy so.
Similarity: 0.9793974757194519
Most frequent named entity: 
Lucy
first_word_in_15th_sentence is: 
Fourth
Vector for first_word_in_15th_sentence:
37.999928
"""