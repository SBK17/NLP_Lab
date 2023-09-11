#Assignment no : 1
#Name : Shubham Bappasaheb Kamandar
#Batch : B2
#Roll no : 31
#Title : Assignment based on text preprocessing using NLP operations like tokenization,stop words,lemmatization,part of speech

#########Tokens in spaCy



import spacy                                #Import Library
nlp = spacy.load("en_core_web_sm")
about_text = (
    "Johny Johny Yes Papa"                  #Input
    "Eating sugar No, papa"
    "Telling lies No, papa"
    "Open your mouth Ah, ah, ah!"
)
about_doc = nlp(about_text)

for token in about_doc:
    print (token, token.idx)                #Print Output
    
    
    
                                            #Output  
    
# Johny 0
# Johny 6
# Yes 12
# PapaEating 16
# sugar 27
# No 33
# , 35
# papaTelling 37
# lies 49
# No 54
# , 56
# papaOpen 58
# your 67
# mouth 72
# Ah 78
# , 80
# ah 82
# , 84
# ah 86
# ! 88

########            Stop Word


spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)

for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)
    
    
#                                           OUTPUT
 
# whether
# many
# get
# may
# again
# hers
# keep
# itself
# will
# here   


#########             Lemmatization
    
nlp = spacy.load("en_core_web_sm")
conference_help_text = (
    "Johny Johny Yes Papa"
    "Eating sugar No, papa"
    "Telling lies No, papa"
    "Open your mouth Ah, ah, ah!"
)
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")
        
        
#                                          OUTPUT

#                   No : no
#          papaTelling : papatelling
#                 lies : lie
#                   No : no
#             papaOpen : papaopen
#                   Ah : ah
     
##########                                              Part-of-Speech Tagging

about_doc = nlp(about_text)
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )
#                                       OUTPUT

#                Ah : ah

# TOKEN: Johny
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: Johny
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: Yes
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: PapaEating
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: sugar
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: No
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: ,
# =====
# TAG: ,          POS: PUNCT
# EXPLANATION: punctuation mark, comma

# TOKEN: papaTelling
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: lies
# =====
# TAG: VBZ        POS: VERB
# EXPLANATION: verb, 3rd person singular present

# TOKEN: No
# =====
# TAG: RB         POS: ADV
# EXPLANATION: adverb

# TOKEN: ,
# =====
# TAG: ,          POS: PUNCT
# EXPLANATION: punctuation mark, comma

# TOKEN: papaOpen
# =====
# TAG: VB         POS: VERB
# EXPLANATION: verb, base form

# TOKEN: your
# =====
# TAG: PRP$       POS: PRON
# EXPLANATION: pronoun, possessive

# TOKEN: mouth
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: Ah
# =====
# TAG: UH         POS: INTJ
# EXPLANATION: interjection

# TOKEN: ,
# =====
# TAG: ,          POS: PUNCT
# EXPLANATION: punctuation mark, comma

# TOKEN: ah
# =====
# TAG: UH         POS: INTJ
# EXPLANATION: interjection

# TOKEN: ,
# =====
# TAG: ,          POS: PUNCT
# EXPLANATION: punctuation mark, comma

# TOKEN: ah
# =====
# TAG: UH         POS: INTJ
# EXPLANATION: interjection

# TOKEN: !
# =====
# TAG: .          POS: PUNCT