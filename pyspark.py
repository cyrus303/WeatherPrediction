import findspark
findspark.init()
import pyspark
import random
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.conf import SparkConf
from pyspark import sql
from pyspark.sql import *
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

sc = SparkContext.getOrCreate()
spark = SparkSession(sc)

df = spark.read.csv("testset_raw.csv", inferSchema = True, header = True)
df.show()

from pyspark.sql.functions import mean

mean_val = df.select(mean(df[' _pressurem'])).collect()
mean_val[0][0]
mean_fin = mean_val[0][0]
df.na.fill(mean_fin,[' _pressurem']).show()

mean_val = df.select(mean(df[' _dewptm'])).collect()
mean_val[0][0]
mean_fin = mean_val[0][0]
df.na.fill(mean_fin,[' _dewptm']).show()

mean_val = df.select(mean(df[' _tempm'])).collect()
mean_val[0][0]
mean_fin = mean_val[0][0]
df.na.fill(mean_fin,[' _tempm']).show()

mean_val = df.select(mean(df[' _wdird'])).collect()
mean_val[0][0]
mean_fin = mean_val[0][0]
df.na.fill(mean_fin,[' _wdird']).show()

df.na.drop(subset=[' _hum']).show()

df.write.csv('/C:/Users/gauth/OneDrive/Desktop/cloud assignment/final.csv')



