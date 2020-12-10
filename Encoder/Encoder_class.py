from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot
import numpy as np
import pandas as pd
from scipy import spatial
from sklearn.manifold import TSNE
from Progressbar import Progressbar_class as pbc
from time import sleep

class Encoder_class:
  errorcount = 0

  config = []
  configfile = ""
  input_data = []
  tfidf_data = []
  tfidf_feature_names = []
  transformed_input_data = []
  transformed_without_POS = []
  gensim_embedded = []
  gensim_vocab = []
  glove_database = {}
  glove_embedded = []
  guiobject = []

  def __init__(self, configfile, inputdata):
    self.errorcount = 0
    self.config = []
    self.configfile = configfile
    self.input_data = inputdata
    self.tfidf_data = []
    self.tfidf_feature_names = []
    self.transformed_input_data = []
    self.transformed_without_POS = []
    self.gensim_embedded = []
    self.gensim_vocab = []
    self.glove_database = {}
    self.glove_embedded = []
    self.guiobject = []
	
  def __process__(self, guiobject):
    self.__parse_configuration__()
    self.guiobject = guiobject
    self.guiobject.tfidfstatusstringvar.set("Pending")
    self.guiobject.tfidfstatus.config(fg='white', bg='blue', text="" + str(self.guiobject.tfidfstatusstringvar.get()))
    self.guiobject.transformstatusstringvar.set("Pending")
    self.guiobject.transformstatus.config(fg='white', bg='blue', text="" + str(self.guiobject.transformstatusstringvar.get()))
    self.guiobject.gensimstatusstringvar.set("Pending")
    self.guiobject.gensimstatus.config(fg='white', bg='blue', text="" + str(self.guiobject.gensimstatusstringvar.get()))
    self.guiobject.glovestatusstringvar.set("Pending")
    self.guiobject.glovestatus.config(fg='white', bg='blue', text="" + str(self.guiobject.glovestatusstringvar.get()))
    self.guiobject.glovegenstatusstringvar.set("Pending")
    self.guiobject.glovegenstatus.config(fg='white', bg='blue', text="" + str(self.guiobject.glovegenstatusstringvar.get()))
    sleep(0.001)
    self.guiobject.window.update()
    self.__process_tf_idf_vectorization__()
    self.__transform_input_data__()
    self.__load_gensim_model__()
    self.__load_glove_model__()
    self.__create_embed_model_using_glove__()
	
  def __parse_configuration__(self):
    print("[ENC]: Parsing configuration file.")
    try:
      self.config = json.load(open(self.configfile))
    except:
      print("[ENC-0001]: Configuration file is not in JSON format!")

  def __process_tf_idf_vectorization__(self):
    vectorizer = TfidfVectorizer()
    progressbar_object = pbc.Progressbar_class("[ENC]: TF-IDF vectorizing:", 139, len(self.input_data), 2,"", self.guiobject, self.guiobject.tfidfstatusstringvar, self.guiobject.progress, self.guiobject.progressstringvar, 65, 607)
    temp = []
    self.guiobject.tfidfstatusstringvar.set("In Progress")
    self.guiobject.tfidfstatus.config(fg='black', bg='yellow', text="" + str(self.guiobject.tfidfstatusstringvar.get()))
    sleep(0.001)
    self.guiobject.window.update()
    for element in self.input_data:
      temp.append(self.__build_string__(element[0]) + " CATEGORY" + str(element[1]))
      progressbar_object.__update__()
    progressbar_object.__finalize__()
    self.guiobject.tfidfstatusstringvar.set("Done.")
    self.guiobject.tfidfstatus.config(fg='white', bg='green', text="" + str(self.guiobject.tfidfstatusstringvar.get()))
    sleep(0.001)
    self.guiobject.window.update()
    self.tfidf_data = vectorizer.fit_transform(temp)
    self.tfidf_feature_names = vectorizer.get_feature_names()
    tempdata = []
    for i in range(len(self.input_data)):
      tempdata.append(""+str(i+1)+".req")
    self.tfidf_data = pd.DataFrame(self.tfidf_data.todense(), index=tempdata, columns=self.tfidf_feature_names)
    #this should be configurable
    #self.tfidf_data.to_excel("kimenet.xlsx")
	
  def __build_string__(self, list):
    result = ""
    for element in list:
      result += str(element[0])+str(element[1])
      result += " "
    return result[:-1]
	
  def __transform_input_data__(self):
    self.guiobject.transformstatusstringvar.set("In Progress")
    self.guiobject.transformstatus.config(fg='black', bg='yellow', text="" + str(self.guiobject.transformstatusstringvar.get()))
    sleep(0.001)
    self.guiobject.window.update()
    progressbar_object = pbc.Progressbar_class("[ENC]: Transforming data:", 139, len(self.input_data), 2,"", self.guiobject, self.guiobject.transformstatusstringvar, self.guiobject.progress, self.guiobject.progressstringvar, 65, 607)
    for line in self.input_data:
      convertedline = []
      converted_without_POS = []
      element = line[0]
      for pair in element:
        convertedline.append("" + pair[0] + pair[1])
        converted_without_POS.append(""+pair[0])
      self.transformed_input_data.append(convertedline)
      self.transformed_without_POS.append(converted_without_POS)
      progressbar_object.__update__()
    progressbar_object.__finalize__()
    self.guiobject.transformstatusstringvar.set("Done.")
    self.guiobject.transformstatus.config(fg='white', bg='green', text="" + str(self.guiobject.transformstatusstringvar.get()))
    sleep(0.001)
    self.guiobject.window.update()
	  
  def __load_gensim_model__(self):
    self.guiobject.gensimstatusstringvar.set("In Progress")
    self.guiobject.gensimstatus.config(fg='black', bg='yellow', text="" + str(self.guiobject.gensimstatusstringvar.get()))
    sleep(0.001)
    self.guiobject.window.update()
    print("[ENC]: Loading gensim model.")
    self.gensim_embedded = Word2Vec.load('embedded_model.chb')
    self.gensim_vocab = list(self.gensim_embedded.wv.vocab)
    self.guiobject.gensimstatusstringvar.set("Done.")
    self.guiobject.gensimstatus.config(fg='white', bg='green', text="" + str(self.guiobject.gensimstatusstringvar.get()))
    sleep(0.001)
    self.guiobject.window.update()
	
  def __create_embed_model_using_gensim__(self):
    print("[ENC]: Creating embed model using gensim.")
    self.gensim_embedded = Word2Vec(self.transformed_input_data, min_count=1)
    self.gensim_vocab = list(self.gensim_embedded.wv.vocab)
    self.gensim_embedded.save('embedded_model.chb')
	  
  def __display_gensim_embed__(self): #THIS IS NOT USED NOW, POSSIBLY DEAD CODE
    matrix = self.gensim_embedded[self.gensim_vocab]
    pca = PCA(n_components=2)
    fillup = pca.fit_transform(matrix)
    pyplot.scatter(fillup[:,0],fillup[:,1])
    for i, word in enumerate(self.gensim_vocab):
      pyplot.annotate(word, xy=(fillup[i, 0], fillup[i, 1]))
    #pyplot.show()
	
  def __load_glove_model__(self):
    self.guiobject.glovestatusstringvar.set("In Progress")
    self.guiobject.glovestatus.config(fg='black', bg='yellow', text="" + str(self.guiobject.glovestatusstringvar.get()))
    sleep(0.001)
    self.guiobject.window.update()
    progressbar_object = pbc.Progressbar_class("[ENC]: Loading GloVe vectors:", 139, self.__count_glove_model_size__(), 1,"", self.guiobject, self.guiobject.glovestatusstringvar, self.guiobject.progress, self.guiobject.progressstringvar, 65, 607)
    with open("glove.6B.50d.txt", 'r', encoding="utf-8") as f:
      for line in f:
        values = line.split(" ")
        word = values[0]
        vector = np.asarray(values[1:], "float32")
        self.glove_database[word] = vector
        progressbar_object.__update__()
    progressbar_object.__finalize__()
    self.guiobject.glovestatusstringvar.set("Done.")
    self.guiobject.glovestatus.config(fg='white', bg='green', text="" + str(self.guiobject.glovestatusstringvar.get()))
    sleep(0.001)
    self.guiobject.window.update()
			
  def __count_glove_model_size__(self):
    print("[ENC]: Initializing.")
    count = 0
    count = len(open("glove.6B.50d.txt", encoding="utf8").readlines())
    return count
	
  def __create_embed_model_using_glove__(self):
    self.guiobject.glovegenstatusstringvar.set("In Progress")
    self.guiobject.glovegenstatus.config(fg='black', bg='yellow', text="" + str(self.guiobject.glovegenstatusstringvar.get()))
    sleep(0.001)
    self.guiobject.window.update()
    progressbar_object = pbc.Progressbar_class("[ENC]: Creating GloVe model:", 139, len(self.transformed_without_POS), 2,"", self.guiobject, self.guiobject.glovegenstatusstringvar, self.guiobject.progress, self.guiobject.progressstringvar, 65, 607)
    for line in self.transformed_without_POS:
      linedata = []
      for word in line:
        worddata="nodata"
        for key in self.glove_database:
          if(key==word):
            worddata=self.glove_database[key]
        linedata.append(worddata)
      self.glove_embedded.append(linedata)
      progressbar_object.__update__()
    progressbar_object.__finalize__()
    self.guiobject.glovegenstatusstringvar.set("Done.")
    self.guiobject.glovegenstatus.config(fg='white', bg='green', text="" + str(self.guiobject.glovegenstatusstringvar.get()))
    sleep(0.001)
    self.guiobject.window.update()

  def __get_tfidf_data__(self):
    if(len(self.tfidf_data) != 0):
      return self.tfidf_data
    else:
      self.__encoder_error__("[ENC]: TF-IDF data and/or feature name list seems to be empty. Did you run __process__()?")
	  
  def __get_gensim_data__(self):
    if(self.gensim_embedded != []):
      return self.gensim_embedded, self.gensim_vocab
    else:
      self.__encoder_error__("[ENC]: Gensim data seems to be empty. Did you run __process__()?")
 
  def __get_glove_data__(self):
    if(self.glove_embedded != []):
      return self.glove_embedded
    else:
      self.__encoder_error__("[ENC]: GloVe data seems to be empty. Did you run __process__()?")

  def __encoder_error__(self, message):
    print(message)
    exit()