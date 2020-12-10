from Progressbar import Progressbar_class as pbc
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from time import sleep

class Classifier_class:

  tf_idf_database = []
  tf_idf_loaded = False
  gensim_embed_database = []
  gensim_loaded = False
  glove_embed_database = []
  glove_loaded = False
  guiobject = []

  def __init__(self):
    self.tf_idf_database = []
    self.tf_idf_loaded = False
    self.gensim_embed_database = []
    self.gensim_loaded = False
    self.glove_embed_database = []
    self.glove_loaded = False
    self.guiobject = []
    
  def __perform__(self, guiobject):
    self.__parse_configuration__()
    self.guiobject = guiobject
    self.guiobject.randomforeststatusstringvar.set("Pending")
    self.guiobject.randomforeststatus.config(fg='white', bg='blue', text="" + str(self.guiobject.randomforeststatusstringvar.get()))
    self.guiobject.svmlinstatusstringvar.set("Pending")
    self.guiobject.svmlinstatus.config(fg='white', bg='blue', text="" + str(self.guiobject.svmlinstatusstringvar.get()))
    self.guiobject.svmpolystatusstringvar.set("Pending")
    self.guiobject.svmpolystatus.config(fg='white', bg='blue', text="" + str(self.guiobject.svmpolystatusstringvar.get()))
    self.guiobject.svmrbfstatusstringvar.set("Pending")
    self.guiobject.svmrbfstatus.config(fg='white', bg='blue', text="" + str(self.guiobject.svmrbfstatusstringvar.get()))
    self.guiobject.svmsigmstatusstringvar.set("Pending")
    self.guiobject.svmsigmstatus.config(fg='white', bg='blue', text="" + str(self.guiobject.svmsigmstatusstringvar.get()))
    self.guiobject.decisiontreestatusstringvar.set("Pending")
    self.guiobject.decisiontreestatus.config(fg='white', bg='blue', text="" + str(self.guiobject.decisiontreestatusstringvar.get()))
    self.guiobject.knnstatusstringvar.set("Pending")
    self.guiobject.knnstatus.config(fg='white', bg='blue', text="" + str(self.guiobject.knnstatusstringvar.get()))
    self.guiobject.bayesstatusstringvar.set("Pending")
    self.guiobject.bayesstatus.config(fg='white', bg='blue', text="" + str(self.guiobject.bayesstatusstringvar.get()))
    self.guiobject.ldastatusstringvar.set("Pending")
    self.guiobject.ldastatus.config(fg='white', bg='blue', text="" + str(self.guiobject.ldastatusstringvar.get()))
    self.guiobject.randomforestaccstringvar.set("Pending")
    self.guiobject.randomforestacc.config(fg='white', bg='blue', text="" + str(self.guiobject.randomforestaccstringvar.get()))
    self.guiobject.svmlinaccstringvar.set("Pending")
    self.guiobject.svmlinacc.config(fg='white', bg='blue', text="" + str(self.guiobject.svmlinaccstringvar.get()))
    self.guiobject.svmpolyaccstringvar.set("Pending")
    self.guiobject.svmpolyacc.config(fg='white', bg='blue', text="" + str(self.guiobject.svmpolyaccstringvar.get()))
    self.guiobject.svmrbfaccstringvar.set("Pending")
    self.guiobject.svmrbfacc.config(fg='white', bg='blue', text="" + str(self.guiobject.svmrbfaccstringvar.get()))
    self.guiobject.svmsigmoidaccstringvar.set("Pending")
    self.guiobject.svmsigmoidacc.config(fg='white', bg='blue', text="" + str(self.guiobject.svmsigmoidaccstringvar.get()))
    self.guiobject.dectreeaccstringvar.set("Pending")
    self.guiobject.dectreeacc.config(fg='white', bg='blue', text="" + str(self.guiobject.dectreeaccstringvar.get()))
    self.guiobject.knnaccstringvar.set("Pending")
    self.guiobject.knnacc.config(fg='white', bg='blue', text="" + str(self.guiobject.knnaccstringvar.get()))
    self.guiobject.bayesaccstringvar.set("Pending")
    self.guiobject.bayesacc.config(fg='white', bg='blue', text="" + str(self.guiobject.bayesaccstringvar.get()))
    self.guiobject.ldaaccstringvar.set("Pending")
    self.guiobject.ldaacc.config(fg='white', bg='blue', text="" + str(self.guiobject.ldaaccstringvar.get()))
    sleep(0.001)
    self.guiobject.window.update()
    self.__perform_classification__("RFC","Random Forest")
    self.__perform_classification__("SVMlinear", "SVM linear")
    self.__perform_classification__("SVMpoly", "SVM poly")
    self.__perform_classification__("SVMrbf", "SVM rbf")
    self.__perform_classification__("SVMsigmoid", "SVM sigmoid")
    self.__perform_classification__("DTC", "Decision Tree")
    self.__perform_classification__("KNN", "KNN")
    self.__perform_classification__("NBS", "Naive Bayes")
    self.__perform_classification__("LDA", "LDA")
 
  def __parse_configuration__(self):
    print("[CLA]: Parsing configuration file.")
    try:
      self.config = json.load(open(self.configfile))
    except:
      print("[CLA-0001]: Configuration file is not in JSON format!")
 
  def __set_tfidf_database__(self, database):
    self.tf_idf_database = database
    self.tf_idf_loaded = True

  def __set_gensim_database__(self, database):
    self.gensim_embed_database = database
    self.gensim_loaded = True

  def __set_glove_database__(self, database):
    self.glove_embed_database = database
    self.glove_loaded = True

  def __perform_classification__(self, algo, name):
    data = []
    status = []
    acc = []
    acclab = []
    if(algo=="RFC"):
      data = self.guiobject.randomforeststatusstringvar
      status = self.guiobject.randomforeststatus
      acc = self.guiobject.randomforestaccstringvar
      acclab = self.guiobject.randomforestacc
    if(algo=="SVMlinear"):
      data = self.guiobject.svmlinstatusstringvar
      status = self.guiobject.svmlinstatus
      acc = self.guiobject.svmlinaccstringvar
      acclab = self.guiobject.svmlinacc
    if(algo=="SVMpoly"):
      data = self.guiobject.svmpolystatusstringvar
      status = self.guiobject.svmpolystatus
      acc = self.guiobject.svmpolyaccstringvar
      acclab = self.guiobject.svmpolyacc
    if(algo=="SVMrbf"):
      data = self.guiobject.svmrbfstatusstringvar
      status = self.guiobject.svmrbfstatus
      acc = self.guiobject.svmrbfaccstringvar
      acclab = self.guiobject.svmrbfacc
    if(algo=="SVMsigmoid"):
      data = self.guiobject.svmsigmstatusstringvar
      status = self.guiobject.svmsigmstatus
      acc = self.guiobject.svmsigmoidaccstringvar
      acclab = self.guiobject.svmsigmoidacc
    if(algo=="DTC"):
      data = self.guiobject.decisiontreestatusstringvar
      status = self.guiobject.decisiontreestatus
      acc = self.guiobject.dectreeaccstringvar
      acclab = self.guiobject.dectreeacc
    if(algo=="KNN"):
      data = self.guiobject.knnstatusstringvar
      status = self.guiobject.knnstatus
      acc = self.guiobject.knnaccstringvar
      acclab = self.guiobject.knnacc
    if(algo=="NBS"):
      data = self.guiobject.bayesstatusstringvar
      status = self.guiobject.bayesstatus
      acc = self.guiobject.bayesaccstringvar
      acclab = self.guiobject.bayesacc
    if(algo=="LDA"):
      data = self.guiobject.ldastatusstringvar
      status = self.guiobject.ldastatus
      acc = self.guiobject.ldaaccstringvar
      acclab = self.guiobject.ldaacc
    data.set("In Progress")
    status.config(fg='black', bg='yellow', text="" + str(data.get()))
    acc.set("Calculating")
    acclab.config(fg='black', bg='yellow', text="" + str(acc.get()))
    sleep(0.001)
    self.guiobject.window.update()
    category_list = ["f", "a", "l", "lf", "mn", "o", "pe", "sc", "se", "us", "ft", "po"]
    average_accuracy = 0
    category_counter = len(category_list)

    progressbar_object = pbc.Progressbar_class("[CLA]: " + name + " classifying:", 139, category_counter*9, 2,"",  self.guiobject, data, self.guiobject.progress, self.guiobject.progressstringvar, 65, 607)
    for element in category_list:
      labels = np.array(self.tf_idf_database["category"+element])
      progressbar_object.__update__()
      labels = self.__normalize_labels__(labels)
      progressbar_object.__update__()
      tempdatabase = self.tf_idf_database.drop("category"+element, axis=1)
      progressbar_object.__update__()
      train_features, test_features, train_labels, test_labels = train_test_split(tempdatabase, labels, test_size=0.2)
      progressbar_object.__update__()
      model = self.__create_moedel__(algo)
      progressbar_object.__update__()
      model=self.__fit_data__(model, train_features, train_labels, algo)
      progressbar_object.__update__()
      predictions = model.predict(test_features)
      progressbar_object.__update__()
      accuracy = self.__calculate_accuracy__(test_labels, predictions)
      progressbar_object.__update__()
      average_accuracy += round(accuracy,4)
      progressbar_object.__update__()
    progressbar_object.__update_final_message__("Average accuracy is " + str(round(average_accuracy/category_counter, 4)) + "%.")
    progressbar_object.__finalize__()
    data.set("Done.")
    status.config(fg='white', bg='green', text="" + str(data.get()))
    acc.set(str(round(average_accuracy/category_counter, 4)) + "%.")
    acclab.config(fg='white', bg='green', text="" + str(acc.get()))
    sleep(0.001)
    self.guiobject.window.update()
	
  def __create_moedel__(self, algo):
    if(algo=="RFC"):
      return RandomForestClassifier(n_estimators = 1500)
    if(algo=="LDA"):
      return LDA(n_components=1)
    if(algo=="NBS"):
      return GaussianNB()
    if(algo=="KNN"):
      return KNeighborsClassifier()
    if(algo=="DTC"):
      return DecisionTreeClassifier()
    if(algo=="SVMlinear"):
      return SVC(kernel="linear")
    if(algo=="SVMpoly"):
      return SVC(kernel="poly")
    if(algo=="SVMrbf"):
      return SVC(kernel="rbf")
    if(algo=="SVMsigmoid"):
      return SVC(kernel="sigmoid")

  def __fit_data__(self, model, train_features, train_labels, algo):
    if(algo=="LDA"):
      model.fit_transform(train_features, train_labels)
    else:
      model.fit(train_features, train_labels)
    return model	
	
  def __normalize_labels__(self, labels):
    for i in range(len(labels)):
      if(labels[i] > 0):
        labels[i]=1
    return labels
	
  def __calculate_accuracy__(self, test_data, predicted_data):
    erroneous = 0
    total = 0
    for i in range(len(test_data)):
      if (test_data[i] != predicted_data[i]):
        erroneous += 1
      total += 1
    return 100 - (float(erroneous)/float(total)*100)
