项目框架

=====================================
------------
文件夹目录：
------------
./Datasets/origin_data     原始文档数据
./Datasets/ch_data         只用中文的稳定数据
./Dataset/key_words        只有关键词的文档

./corpus/1/fenci_1.txt      分词只有的预料库，用于word2vec的模型训练
./corpus/dict/dict.txt      所有关键词各占一行，用于jieba分词防止关键词分开

./model/                    保存word2vec模型

-----------------------
代码文件目录（省略后缀）：
-----------------------
get_ch_data                删除原文档中的英文不分
deal_data                  提取原始文档中的关键词
transform_docx_to_txt      得到jieba分词用的用户自定义字典，将文档转化成一个txt文件，将关键词按年转化成txt文件
segment_txt                分词
train_word2vec_model       训练Word2vec模型
get_vector                 测试word2vec模型
k-means_cluster            k-means聚类