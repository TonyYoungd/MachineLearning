"""

    分词

"""

from pyspark.ml.feature import Tokenizer, RegexTokenizer
from pyspark.sql.functions import col, udf
from pyspark.sql.types import IntegerType
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local").appName("Word Count").getOrCreate()


sentenceDataFrame = spark.createDataFrame([
    (0, "Hi I heard about Spark"),
    (1, "I wish Java could use case classes"),
    (2, "Logistic,regression,models,are,neat")
], ["id", "sentence"])

"""
tokenizer = Tokenizer(inputCol="sentence", outputCol="words")

regexTokenizer = RegexTokenizer(inputCol="sentence", outputCol="words", pattern="\\W")
"""

# regexTokenizer.write().save('file:///home/hadoop/Desktop/to2')
tokenizer = Tokenizer().read().load("file:///home/hadoop/Desktop/to")
regexTokenizer = Tokenizer().read().load("file:///home/hadoop/Desktop/to2")


countTokens = udf(lambda words: len(words), IntegerType())

tokenized = tokenizer.transform(sentenceDataFrame)
tokenized.select("words")\
    .withColumn("tokens", countTokens(col("words"))).show(truncate=False)
regexTokenized = regexTokenizer.transform(sentenceDataFrame)
regexTokenized.select("words") \
    .withColumn("tokens", countTokens(col("words"))).show(truncate=False)