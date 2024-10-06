from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from googletrans import Translator
import timeit

def printa_sentimento(sentenca):
    blob = TextBlob(sentenca, analyzer=NaiveBayesAnalyzer())
    polaridade = blob.sentiment


    print(f"Polaridade: {polaridade}")  


sentenca1 = "I absolutely loved the Bee Movie! The storyline was incredibly engaging and the animation was vibrant and colorful. It was incredibly entertaining, filled with humor and clever dialogues! I was thoroughly impressed and found myself laughing throughout the entire film!"
sentenca2 = "I enjoyed the Bee Movie! It was really fun!"

tradutor = Translator()
sentenca1_pt= tradutor.translate(sentenca1, src='en', dest='pt').text
sentenca2_pt = tradutor.translate(sentenca2, src='en', dest='pt').text

print(sentenca1_pt)
print(sentenca2_pt)


tempo_antes = timeit.default_timer()
printa_sentimento(sentenca1)
tempo_depois = timeit.default_timer() - tempo_antes
print(f'Executado em {tempo_depois} segundos.\n------------------------')


tempo_antes = timeit.default_timer()
printa_sentimento(sentenca2)
tempo_depois = timeit.default_timer() - tempo_antes
print(f'Executado em {tempo_depois} segundos.')