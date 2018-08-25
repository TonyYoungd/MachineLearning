"""
	对每年的关键词使用K-means聚类
"""
import gensim
import numpy as np
from sklearn.cluster import KMeans
import docx
from docx import Document
from gensim.models import word2vec
import os
"""加载模型"""
# 文件地址
def get_information(years):
    save_model_name = './models/word2vec_model.model'
    model = word2vec.Word2Vec.load(save_model_name)
    """dfasfasfasfaf"""
    DIR = "./Datasets/key_words_txt/"+years+".txt"
    """数据加载和转化"""
    #print(DIR)
    # 加载数据
    year = []
    file = open(DIR)
    for _ in file:
        line = file.readline()
        year.append(line.split())

    # 将文字转化成特征向量并保存在vector列表中
    vector = []
    for line in year:
        for word in line:
            if word in model:
                vector.append(model[word])
            else:
                pass
    # 构造聚类数为三类的聚类器
    estimator = KMeans(n_clusters=4, max_iter = 1000000)# 构造聚类器
    estimator.fit(vector)  # 导入数据进行聚类
    label_pred = estimator.labels_ # 获取聚类标签

    print("==========聚类标签==============")
    print(label_pred)
    centroids = estimator.cluster_centers_ #获取聚类中心

    # print("==============聚类中心================")
    #print(centroids)

    print('==========中心词===========')

    # 通过对比离中心最近的向量获取中心点的文字表示
    center_topic = []
    for _ in centroids:
        center = 1000000
        temp = []
        for b in vector:
            if abs(np.linalg.norm(b- _)) < center:
                center = abs(np.linalg.norm(b-_))
                temp = b

        for line in year:
            for word in line:
                if word in model:
                    if (model[word] == temp).all():
                        if word not in center_topic:
                            center_topic.append(word)
                else:
                    pass
    print(center_topic)

    # 将需要的信息存储在txt文件中
    information = []
    information.append(years)
    information.append(label_pred)
    information.append(center_topic)
    # print(information)
    center_topic.append(years)
    with open("./result/topic_centers_4.txt", 'a+') as fw:
        fw.write(str(center_topic) + '\n')


if __name__ == '__main__':
    files = os.listdir('./Datasets/key_words_txt/')
    for file in files:
        print(file[:4])
        get_information(str(file[:4]))
