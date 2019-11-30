from gensim.models import word2vec
import json
import pandas as pd
import os

# Load training text
with open('data/guru99.txt') as fp:
    text_list = fp.readlines()
    
text = ' '.join(text_list)

sentences = word2vec.LineSentence(text)
model = word2vec.Word2Vec(sentences, size = 300)

print(model)