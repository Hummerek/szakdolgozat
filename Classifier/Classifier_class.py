import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from Progressbar import Progressbar_class as pbc

class Classifier_class:

  tf_idf_database = []
  tf_idf_loaded = False
  gensim_embed_database = []
  gensim_loaded = False
  glove_embed_database = []
  glove_loaded = False
  random_forest_prepared = [[],[],[],[]]

  def __init__(self):
    self.tf_idf_database = []
    self.tf_idf_loaded = False
    self.gensim_embed_database = []
    self.gensim_loaded = False
    self.glove_embed_database = []
    self.glove_loaded = False
    self.random_forest_prepared = [[],[],[],[]]
    
  def __perform__(self):
    #self.__perform_random_forest_classification__()
    self.__perform_svm_classification__()
    self.__perform_decision_tree_classification__()
    self.__perform_knn_classification__()
    self.__perform_naive_bayes_classification__()
    self.__perform_lda_classification__()
  
  def __set_tfidf_database__(self, database):
    self.tf_idf_database = database
    self.tf_idf_loaded = True

  def __set_gensim_database__(self, database):
    self.gensim_embed_database = database
    self.gensim_loaded = True

  def __set_glove_database__(self, database):
    self.glove_embed_database = database
    self.glove_loaded = True

  def __perform_random_forest_classification__(self):
    category_list = ["f", "a", "l", "lf", "mn", "o", "pe", "sc", "se", "us", "ft", "po"]
    average_accuracy = 0
    category_counter = len(category_list)
    progressbar_object = pbc.Progressbar_class("[CLA]: Random Forest classifying:", 40, category_counter*11, 2,"")
    #todo: dont specify these, but read out of the arff file
    for element in category_list:
      labels = np.array(self.tf_idf_database["category"+element])
      progressbar_object.__update__()
      labels = self.__normalize_labels__(labels)
      progressbar_object.__update__()
      tempdatabase = self.tf_idf_database.drop("category"+element, axis=1)
      progressbar_object.__update__()
      featurelist = list(tempdatabase.columns)
      progressbar_object.__update__()
      tempdatabase = np.array(tempdatabase)
      progressbar_object.__update__()
      train_features, test_features, train_labels, test_labels = train_test_split(tempdatabase, labels, test_size=0.2)
      progressbar_object.__update__()
      model = RandomForestClassifier(n_estimators = 10000)
      progressbar_object.__update__()
      model.fit(train_features, train_labels)
      progressbar_object.__update__()
      predictions = model.predict(test_features)
      progressbar_object.__update__()
      accuracy = self.__calculate_accuracy__(test_labels, predictions)
      progressbar_object.__update__()
      average_accuracy += round(accuracy,4)
      progressbar_object.__update__()
    progressbar_object.__update_final_message__("Average accuracy is " + str(round(average_accuracy/category_counter, 4)) + "%.")
    progressbar_object.__finalize__()

  def __calculate_accuracy__(self, test_data, predicted_data):
    erroneous = 0
    total = 0
    for i in range(len(test_data)):
      if (test_data[i] != predicted_data[i]):
        erroneous += 1
      total += 1
    return 100 - (float(erroneous)/float(total)*100)
	
  def __normalize_labels__(self, labels):
    for i in range(len(labels)):
      if(labels[i] > 0):
        labels[i]=1
    return labels

  def __perform_svm_classification__(self):
    type_list = ["linear", "poly", "rbf", "sigmoid"]
    for type in type_list:
      self.__perform_typic_svm_classification__(type)

  def __perform_typic_svm_classification__(self, type):
    category_list = ["f", "a", "l", "lf", "mn", "o", "pe", "sc", "se", "us", "ft", "po"]
    average_accuracy = 0
    category_counter = len(category_list)
    progressbar_object = pbc.Progressbar_class("[CLA]: SVM " + type + " classifying:", 40, category_counter*18, 2,"")
    for element in category_list:
      labels = np.array(self.tf_idf_database["category"+element])
      progressbar_object.__update__()
      progressbar_object.__update__()
      labels = self.__normalize_labels__(labels)
      progressbar_object.__update__()
      progressbar_object.__update__()
      tempdatabase = self.tf_idf_database.drop("category"+element, axis=1)
      progressbar_object.__update__()
      progressbar_object.__update__()
      train_features, test_features, train_labels, test_labels = train_test_split(tempdatabase, labels, test_size=0.2)
      progressbar_object.__update__()
      progressbar_object.__update__()
      model = SVC(kernel=type)
      progressbar_object.__update__()
      progressbar_object.__update__()
      model.fit(train_features, train_labels)
      progressbar_object.__update__()
      progressbar_object.__update__()
      predictions = model.predict(test_features)
      progressbar_object.__update__()
      progressbar_object.__update__()
      accuracy = self.__calculate_accuracy__(test_labels, predictions)
      progressbar_object.__update__()
      progressbar_object.__update__()
      average_accuracy += round(accuracy,4)
      progressbar_object.__update__()
      progressbar_object.__update__()
    progressbar_object.__update_final_message__("Average accuracy is " + str(round(average_accuracy/category_counter, 4)) + "%.")
    progressbar_object.__finalize__()

  def __perform_decision_tree_classification__(self):
    category_list = ["f", "a", "l", "lf", "mn", "o", "pe", "sc", "se", "us", "ft", "po"]
    average_accuracy = 0
    category_counter = len(category_list)
    progressbar_object = pbc.Progressbar_class("[CLA]: Decision tree classifying:", 40, category_counter*18, 2,"")
    for element in category_list:
      labels = np.array(self.tf_idf_database["category"+element])
      progressbar_object.__update__()
      progressbar_object.__update__()
      labels = self.__normalize_labels__(labels)
      progressbar_object.__update__()
      progressbar_object.__update__()
      tempdatabase = self.tf_idf_database.drop("category"+element, axis=1)
      progressbar_object.__update__()
      progressbar_object.__update__()
      train_features, test_features, train_labels, test_labels = train_test_split(tempdatabase, labels, test_size=0.2)
      progressbar_object.__update__()
      progressbar_object.__update__()
      model = DecisionTreeClassifier()
      progressbar_object.__update__()
      progressbar_object.__update__()
      model.fit(train_features, train_labels)
      progressbar_object.__update__()
      progressbar_object.__update__()
      predictions = model.predict(test_features)
      progressbar_object.__update__()
      progressbar_object.__update__()
      accuracy = self.__calculate_accuracy__(test_labels, predictions)
      progressbar_object.__update__()
      progressbar_object.__update__()
      average_accuracy += round(accuracy,4)
      progressbar_object.__update__()
      progressbar_object.__update__()
    progressbar_object.__update_final_message__("Average accuracy is " + str(round(average_accuracy/category_counter, 4)) + "%.")
    progressbar_object.__finalize__()
	
  def __perform_knn_classification__(self):
    category_list = ["f", "a", "l", "lf", "mn", "o", "pe", "sc", "se", "us", "ft", "po"]
    average_accuracy = 0
    category_counter = len(category_list)
    progressbar_object = pbc.Progressbar_class("[CLA]: KNN classifying:", 40, category_counter*18, 2,"")
    for element in category_list:
      labels = np.array(self.tf_idf_database["category"+element])
      progressbar_object.__update__()
      progressbar_object.__update__()
      labels = self.__normalize_labels__(labels)
      progressbar_object.__update__()
      progressbar_object.__update__()
      tempdatabase = self.tf_idf_database.drop("category"+element, axis=1)
      progressbar_object.__update__()
      progressbar_object.__update__()
      train_features, test_features, train_labels, test_labels = train_test_split(tempdatabase, labels, test_size=0.2)
      progressbar_object.__update__()
      progressbar_object.__update__()
      model = KNeighborsClassifier()
      progressbar_object.__update__()
      progressbar_object.__update__()
      model.fit(train_features, train_labels)
      progressbar_object.__update__()
      progressbar_object.__update__()
      predictions = model.predict(test_features)
      progressbar_object.__update__()
      progressbar_object.__update__()
      accuracy = self.__calculate_accuracy__(test_labels, predictions)
      progressbar_object.__update__()
      progressbar_object.__update__()
      average_accuracy += round(accuracy,4)
      progressbar_object.__update__()
      progressbar_object.__update__()
    progressbar_object.__update_final_message__("Average accuracy is " + str(round(average_accuracy/category_counter, 4)) + "%.")
    progressbar_object.__finalize__()
		
  def __perform_naive_bayes_classification__(self):
    category_list = ["f", "a", "l", "lf", "mn", "o", "pe", "sc", "se", "us", "ft", "po"]
    average_accuracy = 0
    category_counter = len(category_list)
    progressbar_object = pbc.Progressbar_class("[CLA]: Naive Bayes classifying:", 40, category_counter*18, 2,"")
    for element in category_list:
      labels = np.array(self.tf_idf_database["category"+element])
      progressbar_object.__update__()
      progressbar_object.__update__()
      labels = self.__normalize_labels__(labels)
      progressbar_object.__update__()
      progressbar_object.__update__()
      tempdatabase = self.tf_idf_database.drop("category"+element, axis=1)
      progressbar_object.__update__()
      progressbar_object.__update__()
      train_features, test_features, train_labels, test_labels = train_test_split(tempdatabase, labels, test_size=0.2)
      progressbar_object.__update__()
      progressbar_object.__update__()
      model = GaussianNB()
      progressbar_object.__update__()
      progressbar_object.__update__()
      model.fit(train_features, train_labels)
      progressbar_object.__update__()
      progressbar_object.__update__()
      predictions = model.predict(test_features)
      progressbar_object.__update__()
      progressbar_object.__update__()
      accuracy = self.__calculate_accuracy__(test_labels, predictions)
      progressbar_object.__update__()
      progressbar_object.__update__()
      average_accuracy += round(accuracy,4)
      progressbar_object.__update__()
      progressbar_object.__update__()
    progressbar_object.__update_final_message__("Average accuracy is " + str(round(average_accuracy/category_counter, 4)) + "%.")
    progressbar_object.__finalize__()
	
  def __perform_lda_classification__(self):
    category_list = ["f", "a", "l", "lf", "mn", "o", "pe", "sc", "se", "us", "ft", "po"]
    average_accuracy = 0
    category_counter = len(category_list)
    progressbar_object = pbc.Progressbar_class("[CLA]: LDA classifying:", 40, category_counter*18, 2,"")
    for element in category_list:
      labels = np.array(self.tf_idf_database["category"+element])
      progressbar_object.__update__()
      progressbar_object.__update__()
      labels = self.__normalize_labels__(labels)
      progressbar_object.__update__()
      progressbar_object.__update__()
      tempdatabase = self.tf_idf_database.drop("category"+element, axis=1)
      progressbar_object.__update__()
      progressbar_object.__update__()
      train_features, test_features, train_labels, test_labels = train_test_split(tempdatabase, labels, test_size=0.2)
      progressbar_object.__update__()
      progressbar_object.__update__()
      model = LDA(n_components=1)
      progressbar_object.__update__()
      progressbar_object.__update__()
      model.fit_transform(train_features, train_labels)
      progressbar_object.__update__()
      progressbar_object.__update__()
      predictions = model.predict(test_features)
      progressbar_object.__update__()
      progressbar_object.__update__()
      accuracy = self.__calculate_accuracy__(test_labels, predictions)
      progressbar_object.__update__()
      progressbar_object.__update__()
      average_accuracy += round(accuracy,4)
      progressbar_object.__update__()
      progressbar_object.__update__()
    progressbar_object.__update_final_message__("Average accuracy is " + str(round(average_accuracy/category_counter, 4)) + "%.")
    progressbar_object.__finalize__()