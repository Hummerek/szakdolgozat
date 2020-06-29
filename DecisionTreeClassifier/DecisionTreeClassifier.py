import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

import StringWeightCalculator as SWC

def classify(datarecordlist, param):
  Dictionary = SWC.StringWeightCalculatorClass()
  Dictionary.__process_calculation__(datarecordlist, param)
  Dictionary = Dictionary.WordDictionary
  print("[DecisionTree] - Done.")
  col_names = ["score","category"]