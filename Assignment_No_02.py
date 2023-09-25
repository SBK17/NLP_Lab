'''
Name: Shubham Kamandar
Roll no: 031
Sub: NLP_LAB 
Assignment Name: Natural Language Processing (NLP) using Gensim 
Assignment NO 02
'''

import numpy as np
from gensim.utils import simple_preprocess
from gensim import corpora
from gensim import models



text2 = open('Sample.txt', encoding ='utf-8')
 
tokens2 =[]
for line in text2.read().split('.'):
  tokens2.append(simple_preprocess(line, deacc = True))

g_dict2 = corpora.Dictionary(tokens2)

print("The dictionary has: " +str(len(g_dict2)) + " tokens\n")
print(g_dict2.token2id)
g_bow =[g_dict2.doc2bow(token, allow_update = True) for token in tokens2]       #Using Bag-of-Words(BOW)
print("Bag of Words : ", g_bow)


#--------------------------------------OUTPUT---------------------------------------------

# The dictionary has: 12 tokens

#{'ah': 0, 'eating': 1, 'johny': 2, 'lies': 3, 'mouth': 4, 'no': 5, 'open': 6, 'papa': 7, 'sugar': 8, 'telling': 9, 'yes': 10, 'your': 11}
#Bag of Words :  [[(0, 3), (1, 1), (2, 2), (3, 1), (4, 1), (5, 2), (6, 1), (7, 3), (8, 1), (9, 1), (10, 1), (11, 1)]]










#---------------------------------------------CREATING TF-IDF---------------------------------------------

# text = ["Johny Johny Yes Papa",               
#         "Eating sugar No, papa",
#         "Telling lies No, papa",
#         "Open your mouth Ah, ah, ah!"]

# g_dict = corpora.Dictionary([simple_preprocess(line) for line in text])
# g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text]

# print("Dictionary : ")
# for item in g_bow:
#     print([[g_dict[id], freq] for id, freq in item])

# g_tfidf = models.TfidfModel(g_bow, smartirs='ntc')

# print("TF-IDF Vector:")
# for item in g_tfidf[g_bow]:
#     print([[g_dict[id], np.around(freq, decimals=2)] for id, freq in item])
    
    
    
    
#  --------------------------------------OUTPUT---------------------------------------------

# Dictionary : 
# [['johny', 2], ['papa', 1], ['yes', 1]]
# [['papa', 1], ['eating', 1], ['no', 1], ['sugar', 1]]
# [['papa', 1], ['no', 1], ['lies', 1], ['telling', 1]]
# [['ah', 3], ['mouth', 1], ['open', 1], ['your', 1]]
# TF-IDF Vector:
# [['johny', 0.89], ['papa', 0.14], ['yes', 0.44]]
# [['papa', 0.2], ['eating', 0.64], ['no', 0.37], ['sugar', 0.64]]
# [['papa', 0.2], ['no', 0.37], ['lies', 0.64], ['telling', 0.64]]
# [['ah', 0.87], ['mouth', 0.29], ['open', 0.29], ['your', 0.29]]