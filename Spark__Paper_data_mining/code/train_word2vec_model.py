"""
训练word2vec模型
"""

# from gensim.models import word2vec
import gensim
import logging

# 训练模型，生成词向量
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# 加载语料
sentences = gensim.models.word2vec.Text8Corpus('./corpus/1/fenci.txt')
print(sentences)
# 训练模型
model = gensim.models.Word2Vec(sentences, size = 200)
# 保存模型

model.save('./models/word2vec_model.model')
model.wv.save_word2vec_format("./models/word2vec_model.bin", binary=True)
