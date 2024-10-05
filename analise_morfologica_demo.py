import spacy


nlp = spacy.load("pt_core_news_sm")


sentence = "Hoje fui ao supermercado da minha cidade. Os preços estavam muito altos."
doc = nlp(sentence)

for token in doc:
    print(token.text, token.pos_)
