from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import HashingTF, Tokenizer
from pyspark.ml.clustering import LDA


DATA_SETS = './sample_lda_libsvm_data.txt'


spark = SparkSession.builder.master("local").appName("Word Count").getOrCreate()
dataset = spark.read.format("libsvm").load("file:///usr/local/spark-2.3.0/data/mllib/sample_lda_libsvm_data.txt")

lda = LDA(k=10, maxIter=10)
model = lda.fit(dataset)

ll = model.logLikelihood(dataset)
lp = model.logPerplexity(dataset)

print("The lower bound on the log likelihood of the entire corpus: " + str(ll))
print("The upper bound on perplexity: " + str(lp))
print('===========')


topics = model.describeTopics(3)
print(topics)
print('------')
topics.show(truncate=False)
print('========')
transformed = model.transform(dataset)
transformed.show(truncate=False)
print('=======')

print(dataset)