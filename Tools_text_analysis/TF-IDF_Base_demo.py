
"""
    词频-逆向文件频率
    特征向量化方法，体现一个文档中词语在语料库中的重要程度
    首先使用分解器Tokenizer把句子划分为单个词语。
    对每一个句子（词袋），我们使用HashingTF将句子转换为特征向量，最后使用IDF重新调整特征向量。
    这种转换通常可以提高使用文本特征的性能。
"""
from pyspark.ml.feature import HashingTF,IDF,Tokenizer
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local").appName("Word Count").getOrCreate()

# 创建简单的DataFrame，每个句子代表一个文档
sentenceData = spark.createDataFrame(
    [(0, "I heard about Spark and I love Spark"),
     (1, "I wish Java could use case classes"),
     (2, "Logistic regression models are neat")]).toDF("label", "sentence")

# 使用tokenizer对句子进行分词
tokenizer = Tokenizer(inputCol="sentence", outputCol="words")
wordsData = tokenizer.transform(sentenceData)

# 把句子哈希成特征向量,最多容纳单词的个数为numFeatures
hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=20)

featurizedData = hashingTF.transform(wordsData)

# 使用IDF对单纯的词频特征向量进行修正，使其更能体现不同词汇对文本的区别能力
idf = IDF(inputCol="rawFeatures", outputCol="features")
idfModel = idf.fit(featurizedData)

# idfModel是一个transformer，调用transform()方法，得到每个单词对应的TF-IDF度量值
rescaledData = idfModel.transform(featurizedData)
rescaledData.show()

