import spacy
from textblob import TextBlob
from googletrans import Translator

def printa_sentimento(sentenca):
    blob = TextBlob(sentenca)
    polaridade = blob.sentiment.polarity
    subjetividade = blob.sentiment.subjectivity

    print(f"Polaridade: {polaridade}")  
    print(f"Subjetividade: {subjetividade}") 

nlp = spacy.load("en_core_web_lg")

sentenca1 = "I dont believe on what happend last night! The team was playing very good. Veron was on fire!"
sentenca2 = "I dont believe on what happend last night! Veron was on fire!"

tradutor = Translator()
sentenca1_pt= tradutor.translate(sentenca1, src='en', dest='pt').text
sentenca2_pt = tradutor.translate(sentenca2, src='en', dest='pt').text

print(sentenca1_pt)
print(sentenca2_pt)

printa_sentimento(sentenca1)
printa_sentimento(sentenca2)