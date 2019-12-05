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
from pyspark.sql.functions import mean
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import DoubleType, IntegerType, StringType

sc = SparkContext.getOrCreate()
spark = SparkSession(sc)

data_schema = StructType([
	StructField('datetime_utc', IntegerType()),
	StructField('Time', StringType()),
	StructField(' _conds', StringType()),
	StructField(' _dewptm', IntegerType()),
	StructField(' _fog', IntegerType()),
	StructField(' _hail', IntegerType()),
	StructField(' _heatindexm', IntegerType()),
	StructField(' _hum', IntegerType()),
	StructField(' _precipm', IntegerType()),
	StructField(' _pressurem', IntegerType()),
	StructField(' _rain', IntegerType()),
	StructField(' _snow', IntegerType()),
	StructField(' _tempm', IntegerType()),
	StructField(' _thunder', IntegerType()),
	StructField(' _tornado', IntegerType()),
	StructField(' _vism', DoubleType()),
	StructField(' _wdird', IntegerType()),
	StructField(' _wdire', StringType()),
	StructField(' _wgustm', DoubleType()),
	StructField(' _windchillm', DoubleType()),
	StructField(' _wspdm', DoubleType())
])

df = spark.read.schema(data_schema).options(header='True').csv("file:///C:/Users/gauth/OneDrive/Desktop/testset_raw.csv")
df.show()


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

df.write.csv('/C:/Users/gauth/OneDrive/Desktop/cloud assignment/final.csv')





