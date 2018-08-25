"""
    调用模型获得词的向量
"""

from gensim.models import word2vec 

save_model_name = './models/word2vec_model.model'
model_1 = word2vec.Word2Vec.load(save_model_name)

# 计算两个词的相似度/相关程度
y1 = model_1.similarity("褐煤", "烟煤")
print(u"褐煤和烟煤的相似性：", y1)
print("-------------------------------\n")
y1_1 = model_1.similarity("褐煤", "时间")
print(u"褐煤和时间的相似性：", y1_1) 
print("-------------------------------\n")

# 计算某个词的相关词列表
y2 = model_1.most_similar("煤", topn=5)  # 5个最相关的
print(u"和煤最相关的词有：\n")
for item in y2:
    print(item[0], item[1])
print("-------------------------------\n")
print("煤的特征向量为:")
print(model_1['煤'])







