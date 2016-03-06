#!/usr/bin/env python

'''
Convenience script to prepare pyspark for ml usage.

1. Start pyspark
$ bin/pyspark

2. load script:
>>> execfile('mlprepare.py')
'''

from __future__ import print_function
from pyspark.ml import Pipeline
from pyspark.ml.feature import *

print("---------------")
print("Preparing shell for ML")
print("Imported pyspark.ml.Pipeline")
print("Imported pyspark.ml.feature.*")
