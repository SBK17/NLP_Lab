import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
piano_text = "My Name is Shubham"
piano_doc = nlp(piano_text)
for token in piano_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )

displacy.serve(piano_doc, style="dep")