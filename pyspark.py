#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


sc = SparkContext.getOrCreate()
spark = SparkSession(sc)


# In[3]:


df = spark.read.csv("file:///C:/Users/gauth/OneDrive/Desktop/testset.csv", inferSchema = True, header = True)
df.show()


# In[4]:


from pyspark.sql.functions import mean


# In[5]:


mean_val = df.select(mean(df[' _pressurem'])).collect()
mean_val[0][0]
mean_fin = mean_val[0][0]
df.na.fill(mean_fin,[' _pressurem']).show()


# In[6]:


mean_val = df.select(mean(df[' _dewptm'])).collect()
mean_val[0][0]
mean_fin = mean_val[0][0]
df.na.fill(mean_fin,[' _dewptm']).show()


# In[7]:


mean_val = df.select(mean(df[' _tempm'])).collect()
mean_val[0][0]
mean_fin = mean_val[0][0]
df.na.fill(mean_fin,[' _tempm']).show()


# In[8]:


mean_val = df.select(mean(df[' _wdird'])).collect()
mean_val[0][0]
mean_fin = mean_val[0][0]
df.na.fill(mean_fin,[' _wdird']).show()


# In[9]:


df.na.drop(subset=[' _hum']).show()


# In[11]:


df.write.csv('/C:/Users/gauth/OneDrive/Desktop/cloud assignment/final.csv')


# In[ ]:




