from gensim.models import word2vec

with open('data/guru99.txt') as fp:
	sentences = word2vec.LineSentence(fp)

	model = word2vec.Word2Vec(sentences, size = 300)
	model.save('models/model_1')