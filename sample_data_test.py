"""This is a test program with sample data"""

import spacy

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
first_word_in_3rd_sentence = ''
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
    if(len(sent)>4):
        big_sentences.append(sent)
    if scount == 3:
        for word in sent:
            first_word_in_3rd_sentence = word
            break        


print("Token count: "+str(tcount))
print("Verb count: "+str(vcount))
print("Sentence count: "+str(scount))
print("")
print("These are the big sentences in sample data")
print(big_sentences)
for big_sentence in big_sentences:
    getsimilarity(big_sentence, big_sentences)
print("")
print("These are similarities for each big sentence")
print(simi_dict)
res0 = max(simi_dict, key=simi_dict.get)
print("")
print("Most similar sentence is: ")
print(res0)
print("Similarity: "+str(simi_dict[res0]))
simi_dict1 = {key:val for key, val in simi_dict.items() if val != simi_dict[res0]}
res1 = max(simi_dict1, key=simi_dict1.get)
print("2nd Most similar sentence is: ")
print(res1)
print("Similarity: "+str(simi_dict1[res1]))


# getting max frequency
print("")
print("These are the names entites:")
print(named_entities)
res = max(named_entities, key=named_entities.get)
print("Most frequent named entity is: ")
print(res)


print("")
print("first_word_in_3rd_sentence is: ")
print(str(first_word_in_3rd_sentence))
print("Vector for first_word_in_3rd_sentence:")
print(first_word_in_3rd_sentence.vector_norm)

"""
Sample data test output:

Token count: 31
Verb count: 3
Sentence count: 6

These are the big sentences in sample data
[The carriage stopped at the Rectory., She got out to Katty., John is O.K. too., Jim is OK too.]
The carriage stopped at the Rectory.
The carriage stopped at the Rectory.
1.0
The carriage stopped at the Rectory.
She got out to Katty.
0.38816627860069275
The carriage stopped at the Rectory.
John is O.K. too.
0.3134959638118744
The carriage stopped at the Rectory.
Jim is OK too.
0.18550023436546326
She got out to Katty.
The carriage stopped at the Rectory.
0.38816627860069275
She got out to Katty.
She got out to Katty.
1.0
She got out to Katty.
John is O.K. too.
0.3262345790863037
She got out to Katty.
Jim is OK too.
0.33379584550857544
John is O.K. too.
The carriage stopped at the Rectory.
0.3134959638118744
John is O.K. too.
She got out to Katty.
0.3262345790863037
John is O.K. too.
John is O.K. too.
1.0
John is O.K. too.
Jim is OK too.
0.8613601326942444
Jim is OK too.
The carriage stopped at the Rectory.
0.18550023436546326
Jim is OK too.
She got out to Katty.
0.33379584550857544
Jim is OK too.
John is O.K. too.
0.8613601326942444
Jim is OK too.
Jim is OK too.
1.0

These are similarities for each big sentence
{'The carriage stopped at the Rectory. <-> She got out to Katty.': 0.38816627860069275, 'The carriage stopped at the Rectory. <-> John is O.K. too.': 0.3134959638118744, 'The carriage stopped at the Rectory. <-> Jim is OK too.': 0.18550023436546326, 'She got out to Katty. <-> The carriage stopped at the Rectory.': 0.38816627860069275, 'She got out to Katty. <-> John is O.K. too.': 0.3262345790863037, 'She got out to Katty. <-> Jim is OK too.': 0.33379584550857544, 'John is O.K. too. <-> The carriage stopped at the Rectory.': 0.3134959638118744, 'John is O.K. too. <-> She got out to Katty.': 0.3262345790863037, 'John is O.K. too. <-> Jim is OK too.': 0.8613601326942444, 'Jim is OK too. <-> The carriage stopped at the Rectory.': 0.18550023436546326, 'Jim is OK too. <-> She got out to Katty.': 0.33379584550857544, 'Jim is OK too. <-> John is O.K. too.': 0.8613601326942444}

Most similar sentence is: 
John is O.K. too. <-> Jim is OK too.
Similarity: 0.8613601326942444
2nd Most similar sentence is: 
The carriage stopped at the Rectory. <-> She got out to Katty.
Similarity: 0.38816627860069275

These are the names entites:
{'Jim': 2, 'John': 2, 'O.K.': 1}
Most frequent named entity is: 
Jim

first_word_in_3rd_sentence is: 
The
Vector for first_word_in_3rd_sentence:
76.91735
"""