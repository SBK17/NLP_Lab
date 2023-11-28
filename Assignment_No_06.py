"""
Assignment No 6
Name - Shubham Kamandar
Batch - B2
Roll No - 31
Assignment Title : Implement and visualize Dependency Parsing of Textual Input using Standford CoreNLP and Spacy library

"""

import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

multiline_text = """
Shubham is a Spark Developer 
Working in Multi National Compony
"""

multiline_doc = nlp(multiline_text)

for token in multiline_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )

displacy.serve(multiline_doc, style="dep")

'''
TOKEN: 

=====
token.tag_ = '_SP'
token.head.text = 'Shubham'
token.dep_ = 'dep'

TOKEN: Shubham
=====
token.tag_ = 'NNP'
token.head.text = 'is'
token.dep_ = 'nsubj'

TOKEN: is
=====
token.tag_ = 'VBZ'
token.head.text = 'is'
token.dep_ = 'ROOT'

TOKEN: a
=====
token.tag_ = 'DT'
token.head.text = 'Working'
token.dep_ = 'det'

TOKEN: Spark
=====
token.tag_ = 'NNP'
token.head.text = 'Developer'
token.dep_ = 'compound'

TOKEN: Developer
=====
token.tag_ = 'NNP'
token.head.text = 'Working'
token.dep_ = 'compound'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = 'Developer'
token.dep_ = 'dep'

TOKEN: Working
=====
token.tag_ = 'NNP'
token.head.text = 'is'
token.dep_ = 'attr'

TOKEN: in
=====
token.tag_ = 'IN'
token.head.text = 'Working'
token.dep_ = 'prep'

TOKEN: Multi
=====
token.tag_ = 'NNP'
token.head.text = 'Compony'
token.dep_ = 'compound'

TOKEN: National
=====
token.tag_ = 'NNP'
token.head.text = 'Compony'
token.dep_ = 'compound'

TOKEN: Compony
=====
token.tag_ = 'NNP'
token.head.text = 'in'
token.dep_ = 'pobj'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = 'Compony'
token.dep_ = 'dep'

Using the 'dep' visualizer
Serving on http://0.0.0.0:5000 ...

'''