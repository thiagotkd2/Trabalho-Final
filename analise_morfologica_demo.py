import spacy


def remove_stopwords(sentenca):
    nlp = spacy.load("pt_core_news_sm")
    doc = nlp(sentenca)
    print(doc)
    saida = ""

    stop_words = ["AUX", "ADP", "PUNCT", "PRON"]

    for token in doc:
        if token.pos_ not in stop_words:
            saida+=token.text + ' '
        print(token.text, token.pos_)

    print(saida)
    return saida


sentenca = "Ontem fui ao supermercado da cidade. Achei que os preços estavam muito altos. Fui embora de imediato"

remove_stopwords(sentenca)
