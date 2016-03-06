#!/usr/bin/env python

'''
Convenience script to prepare pyspark for sql usage.

1. Start pyspark with csv dependencies 
(https://github.com/databricks/spark-csv):
$ bin/pyspark --packages com.databricks:spark-csv_2.11:1.4.0

2. load script:
>>> execfile('sqlprepare.py')

'''


from __future__ import print_function
from pyspark.sql import SQLContext
from pyspark.sql.functions import *

sqlContext = SQLContext(sc)
print("---------------")
print("Preparing shell for SQL")
print("Added variable: sqlContext")
print("Imported pyspark.sql.functions.*")
print("Added function: df = load_csv('file')")

def load_csv(filename):
    print("sqlContext.read.format('com.databricks.spark.csv').option('header',''true').option('inferSchema','true').load('" + filename + "')")
    x = sqlContext.read \
        .format("com.databricks.spark.csv") \
        .option("header","true") \
        .option("inferSchema","true") \
        .load(filename)
    return x

