import nltk, re, pprint
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from Progressbar import Progressbar_class as pbc
import json
from time import sleep

class Preprocessor_class:
  errorcount = 0

  config = []
  configfile = ""
  raw_data = []
  datafile = ""
  tokens = []
  category = []
  normalized_tokens = []
  stop_words = []
  stopword_filtered = []
  punctuation_marks_to_remove = []
  punctuation_marks_to_convert = []
  punctuation_filtered = []
  indicator_list = []
  separator_list = []
  numeric_converted = []
  pos_tagged = []
  lemmatized = []
  preprocessed_structure = []
  guiobject = []

  def __init__(self, configfile, datafile):
    self.errorcount = 0
    self.config = []
    self.configfile = configfile
    self.raw_data = []
    self.datafile = datafile
    self.tokens = []
    self.category = []
    self.normalized_tokens = []
    self.stop_words = []
    self.stopword_filtered = []
    self.punctuation_marks_to_remove = [',', '.', '!', '?', ':', '(', ')', '@', '&', "$", "%", '#', '<', '>', "'", "•", "	", "-", "'", "'s", "s'"]
    self.punctuation_marks_to_convert = ["/"]
    self.punctuation_filtered = []
    self.indicator_list = ["am", "pm", "k", "mb", "kb", "gb", "min", "m", "h", "s", "day", "x", "way"]
    self.separator_list = ["x", ".", " ", ","]
    self.numeric_converted = []
    self.pos_tagged = []
    self.lemmatized = []
    self.preprocessed_structure = []
    self.guiobject = []
	
  def __process__(self, guiobject):
    self.__parse_configuration__()
    self.guiobject = guiobject
    self.guiobject.loadstopwordstatusstringvar.set("Pending")
    self.guiobject.loadstopwordstatus.config(fg='white', bg='blue', text="" + str(self.guiobject.loadstopwordstatusstringvar.get()))
    self.guiobject.tokenizestatusstringvar.set("Pending")
    self.guiobject.tokenizestatus.config(fg='white', bg='blue', text="" + str(self.guiobject.tokenizestatusstringvar.get()))
    self.guiobject.normalizestatusstringvar.set("Pending")
    self.guiobject.normalizestatus.config(fg='white', bg='blue', text="" + str(self.guiobject.normalizestatusstringvar.get()))
    self.guiobject.filterstopwordsstatusstringvar.set("Pending")
    self.guiobject.filterstopwordsstatus.config(fg='white', bg='blue', text="" + str(self.guiobject.filterstopwordsstatusstringvar.get()))
    self.guiobject.punctuationstatusstringvar.set("Pending")
    self.guiobject.punctuationstatus.config(fg='white', bg='blue', text="" + str(self.guiobject.punctuationstatusstringvar.get()))
    self.guiobject.mergenumericstatusstringvar.set("Pending")
    self.guiobject.mergenumericstatus.config(fg='white', bg='blue', text="" + str(self.guiobject.mergenumericstatusstringvar.get()))
    self.guiobject.postagstatusstringvar.set("Pending")
    self.guiobject.postagstatus.config(fg='white', bg='blue', text="" + str(self.guiobject.postagstatusstringvar.get()))
    self.guiobject.lemmatizestatusstringvar.set("Pending")
    self.guiobject.lemmatizestatus.config(fg='white', bg='blue', text="" + str(self.guiobject.lemmatizestatusstringvar.get()))
    self.guiobject.finalizestatusstringvar.set("Pending")
    self.guiobject.finalizestatus.config(fg='white', bg='blue', text="" + str(self.guiobject.finalizestatusstringvar.get()))
    sleep(0.001)
    self.guiobject.window.update()
    print("guiobject is now of type " + str(type(self.guiobject)))
    self.__generate_raw_data__()
    self.__load_stopword_list__()
    self.__tokenize__()
    self.__normalize_tokens__()
    self.__filter_stopwords__()
    self.__filter_punctuation_from_words__()
    self.__merge_numeric_tokens__()
    self.__POS_tag__()
    self.__lemmatize__()
    self.__finalize__()
	
  def __parse_configuration__(self):
    print("[PRE]: Parsing configuration file.")
    try:
      self.config = json.load(open(self.configfile))
    except:
      print("[PRE-0001]: Configuration file is not in JSON format!")
  
  def __generate_raw_data__(self):
  #  try:
    self.guiobject.rawdatastatusstringvar.set("In Progress")
    self.guiobject.rawdatastatus.config(fg='black', bg='yellow', text="" + str(self.guiobject.rawdatastatusstringvar.get()))
    sleep(0.001)
    self.guiobject.window.update()
    progressbar_object = pbc.Progressbar_class("[PRE]: Generating raw data:",139,self.__count_lines__(self.datafile),2,"", self.guiobject, self.guiobject.rawdatastatusstringvar, self.guiobject.progress, self.guiobject.progressstringvar, 65, 607)
    skipping_lines = True
    with open(self.datafile, 'r') as inputfile:
      for line in inputfile.readlines():
        if(skipping_lines == False):
          strippedline = line.strip()
          self.raw_data.append([strippedline])
        if(line.startswith("@DATA")):
          skipping_lines = False
        progressbar_object.__update__()
    progressbar_object.__finalize__()
    self.guiobject.rawdatastatusstringvar.set("Done.")
    self.guiobject.rawdatastatus.config(fg='white', bg='green', text="" + str(self.guiobject.rawdatastatusstringvar.get()))
    sleep(0.001)
    self.guiobject.window.update()
   # except:
    #  self.__preprocessor_error__("[PRE-0001]: Failed to read data file!")
  
  def __count_lines__(self, filename):
    with open(filename, 'r') as file:
      return len(file.readlines())
  
  def __load_stopword_list__(self):
    try:
      self.guiobject.loadstopwordstatusstringvar.set("In Progress")
      self.guiobject.loadstopwordstatus.config(fg='black', bg='yellow', text="" + str(self.guiobject.loadstopwordstatusstringvar.get()))
      sleep(0.001)
      self.guiobject.window.update()
      progressbar_object = pbc.Progressbar_class("[PRE]: Loading stopword list:", 139,len(stopwords.words('english')),2,"", self.guiobject, self.guiobject.loadstopwordstatusstringvar, self.guiobject.progress, self.guiobject.progressstringvar, 65, 607)
      for word in stopwords.words('english'):
        self.stop_words.append(word)
        progressbar_object.__update__()
      progressbar_object.__finalize__()
      self.guiobject.loadstopwordstatusstringvar.set("Done.")
      self.guiobject.loadstopwordstatus.config(fg='white', bg='green', text="" + str(self.guiobject.loadstopwordstatusstringvar.get()))
      sleep(0.001)
      self.guiobject.window.update()
    except LookupError:
      self.errorcount = self.errorcount + 1
      print("[PRE]: Looks like stopwords are not available. Automatically downloading some for you.")
      nltk.download('stopwords')
      print("[PRE]: All done. Retrying")
      if(self.errorcount >= 3):
        self.__preprocessor_error__("[PRE-0002]: Looks like that did not solve the problem, exiting.")
      else:
        self.stop_words = []
        self.__load_stopword_list__()
	  
  def __tokenize__(self):
    progressbar_object = pbc.Progressbar_class("[PRE]: Tokenizing:",139,len(self.raw_data),2,"", self.guiobject, self.guiobject.tokenizestatusstringvar, self.guiobject.progress, self.guiobject.progressstringvar, 65, 607)
    try:
      self.guiobject.tokenizestatusstringvar.set("In Progress")
      self.guiobject.tokenizestatus.config(fg='black', bg='yellow', text="" + str(self.guiobject.tokenizestatusstringvar.get()))
      sleep(0.001)
      self.guiobject.window.update()
      for entry in self.raw_data:
        record = []
        if entry[0]:
          partitioned = entry[0].split(',')
          entry = partitioned[1]
          self.category.append(partitioned[2])
          for element in entry.split(" "):
            word_tokenize(element)
            record.append(element)
        self.tokens.append(record)
        progressbar_object.__update__()
      progressbar_object.__finalize__()
      self.guiobject.tokenizestatusstringvar.set("Done.")
      self.guiobject.tokenizestatus.config(fg='white', bg='green', text="" + str(self.guiobject.tokenizestatusstringvar.get()))
      sleep(0.001)
      self.guiobject.window.update()
    except LookupError:
      self.errorcount = self.errorcount + 1
      print("[PRE]: Looks like punctuation data is not available. Automatically downloading some for you.")
      nltk.download('punkt')
      print("[PRE]: All done. Retrying")
      if(self.errorcount >= 3):
        self.__preprocessor_error__("[PRE-0003]: Looks like that did not solve the problem, exiting.")
      else:
        self.tokens = []
        self.__tokenize__()
    except:
      if(len(self.raw_data) == 0):
       self.__preprocessor_error__("[PRE-0004]: No raw data to tokenize!")
      else:
        self.__preprocessor_error__("[PRE-0005]: Unknown error during conversion of raw text to tokens!")

  def __normalize_tokens__(self):
    progressbar_object = pbc.Progressbar_class("[PRE]: Normalizing tokens:",139,len(self.tokens),2,"", self.guiobject, self.guiobject.normalizestatusstringvar, self.guiobject.progress, self.guiobject.progressstringvar, 65, 607)
    try: 
      self.guiobject.normalizestatusstringvar.set("In Progress")
      self.guiobject.normalizestatus.config(fg='black', bg='yellow', text="" + str(self.guiobject.normalizestatusstringvar.get()))
      sleep(0.001)
      self.guiobject.window.update()
      for element in self.tokens:
        buffer = []
        for word in element:
          buffer.append(word.lower())
        self.normalized_tokens.append(buffer)
        progressbar_object.__update__()
      progressbar_object.__finalize__()
      self.guiobject.normalizestatusstringvar.set("Done.")
      self.guiobject.normalizestatus.config(fg='white', bg='green', text="" + str(self.guiobject.normalizestatusstringvar.get()))
      sleep(0.001)
      self.guiobject.window.update()
    except:
      if(len(self.tokens) == 0):
        self.__preprocessor_error__("[PRE-0006]: No tokens to normalize!")
      else:
        self.__preprocessor_error__("[PRE-0007]: Unknown error during normalization of tokens!")

  def __filter_stopwords__(self):
    progressbar_object = pbc.Progressbar_class("[PRE]: Filtering stopwords:",139,len(self.normalized_tokens),2,"", self.guiobject, self.guiobject.filterstopwordsstatusstringvar, self.guiobject.progress, self.guiobject.progressstringvar, 65, 607)
    try:
      self.guiobject.filterstopwordsstatusstringvar.set("In Progress")
      self.guiobject.filterstopwordsstatus.config(fg='black', bg='yellow', text="" + str(self.guiobject.filterstopwordsstatusstringvar.get()))
      sleep(0.001)
      self.guiobject.window.update()
      for element in self.normalized_tokens:
        buffer = []
        for word in element:
          if(word not in self.stop_words):
            buffer.append(word)
        self.stopword_filtered.append(buffer)
        progressbar_object.__update__()
      progressbar_object.__finalize__()
      self.guiobject.filterstopwordsstatusstringvar.set("Done.")
      self.guiobject.filterstopwordsstatus.config(fg='white', bg='green', text="" + str(self.guiobject.filterstopwordsstatusstringvar.get()))
      sleep(0.001)
      self.guiobject.window.update()
    except:
      if(len(self.normalized_tokens) == 0):
        self.__preprocessor_error__("[PRE-0008]: Cannot filter stopwords, no words to filter!")
      if(len(self.stop_words) == 0):
        self.__preprocessor_error__("[PRE-0009]: Cannot filter stopwords, no stopwords recorded!")
      else:
        self.__preprocessor_error__("[PRE-0010]: Unknown error during filtering stopwords!")
		
  def __filter_punctuation_from_words__(self):
    progressbar_object = pbc.Progressbar_class("[PRE]: Filtering punctuation:",139,len(self.stopword_filtered),2,"", self.guiobject, self.guiobject.punctuationstatusstringvar, self.guiobject.progress, self.guiobject.progressstringvar, 65, 607)
    try:
      self.guiobject.punctuationstatusstringvar.set("In Progress")
      self.guiobject.punctuationstatus.config(fg='black', bg='yellow', text="" + str(self.guiobject.punctuationstatusstringvar.get()))
      sleep(0.001)
      self.guiobject.window.update()
      for element in self.stopword_filtered:
        filtered = self.__filter_word__(element)
        self.punctuation_filtered.append(filtered)
        progressbar_object.__update__()
      progressbar_object.__finalize__()
      self.guiobject.punctuationstatusstringvar.set("Done.")
      self.guiobject.punctuationstatus.config(fg='white', bg='green', text="" + str(self.guiobject.punctuationstatusstringvar.get()))
      sleep(0.001)
      self.guiobject.window.update()
    except:
      if(len(self.stopword_filtered) == 0):
        self.__preprocessor_error__("[PRE-0011]: No data to filter punctuation on!")
      else:
        self.__preprocessor_error__("[PRE-0012]: Unknown error during filtering of punctuation!")

  def __filter_word__(self, entry):
    filtered_entry = []
    for word in entry:
      for filter in self.punctuation_marks_to_remove:
        word = word.replace(filter,'')
      for filter in self.punctuation_marks_to_convert:
        word = word.replace(filter,' ')
      word = word.strip()
      filtered_entry.append(word)
    return filtered_entry
	
  def __merge_numeric_tokens__(self):
    progressbar_object = pbc.Progressbar_class("[PRE]: Merging numeric tokens:",139,len(self.punctuation_filtered),2,"", self.guiobject, self.guiobject.mergenumericstatusstringvar, self.guiobject.progress, self.guiobject.progressstringvar, 65, 607)
    try:
      self.guiobject.mergenumericstatusstringvar.set("In Progress")
      self.guiobject.mergenumericstatus.config(fg='black', bg='yellow', text="" + str(self.guiobject.mergenumericstatusstringvar.get()))
      sleep(0.001)
      self.guiobject.window.update()
      for element in self.punctuation_filtered:
        buffer = []
        for word in element:
          word = self.__remove_indicator__(word)
          if(word.isnumeric() or self.__separable_number__(word)):
            buffer.append("QNUM")
          else:
            buffer.append(word)
        self.numeric_converted.append(buffer)
        progressbar_object.__update__()
      progressbar_object.__finalize__()
      self.guiobject.mergenumericstatusstringvar.set("Done.")
      self.guiobject.mergenumericstatus.config(fg='white', bg='green', text="" + str(self.guiobject.mergenumericstatusstringvar.get()))
      sleep(0.001)
      self.guiobject.window.update()
    except:
      if(len(self.punctuation_filtered) == 0):
        self.__preprocessor_error__("[PRE-0013]: Cannot merge numeric tokens, no tokens to work on!")
      else:
        self.__preprocessor_error__("[PRE-0014]: Unknown error during merger of numeric tokens!")

  def __remove_indicator__(self, word):
    for indicator in self.indicator_list:
      if(indicator in word and word.replace(indicator,'').isnumeric()):
        word = word.replace(indicator,'')
    return word

  def __separable_number__(self, word):
    result = True
    for separator in self.separator_list:
      result = True
      separated = word.split(separator)
      if(len(separated) > 1):
        for element in separated:
          if(not element.isnumeric() and not self.__separable_number__(element) and not self.__remove_indicator__(element).isnumeric()):
            result = False
      if(len(separated) == 1):
        result = False
      if(result==True):
        return result
    return result
 		
  def __POS_tag__(self):
    progressbar_object = pbc.Progressbar_class("[PRE]: POS-tagging:",139,len(self.numeric_converted),2,"", self.guiobject, self.guiobject.postagstatusstringvar, self.guiobject.progress, self.guiobject.progressstringvar, 65, 607)
    try:
      self.guiobject.postagstatusstringvar.set("In Progress")
      self.guiobject.postagstatus.config(fg='black', bg='yellow', text="" + str(self.guiobject.postagstatusstringvar.get()))
      sleep(0.001)
      self.guiobject.window.update()
      for element in self.numeric_converted:
        pos_tagged_temp = nltk.pos_tag(self.__filter_empty_elements__(element))
        if(pos_tagged_temp != []):
          self.pos_tagged.append(pos_tagged_temp)
        progressbar_object.__update__()
      progressbar_object.__finalize__()
      self.guiobject.postagstatusstringvar.set("Done.")
      self.guiobject.postagstatus.config(fg='white', bg='green', text="" + str(self.guiobject.postagstatusstringvar.get()))
      sleep(0.001)
      self.guiobject.window.update()
    except LookupError:
      self.errorcount = self.errorcount + 1
      print("[PRE]: Looks like POS-tagging data is not available. Automatically downloading some for you.")
      nltk.download('averaged_perceptron_tagger')
      print("[PRE]: All done. Retrying")
      if(self.errorcount >= 3):
        self.__preprocessor_error__("[PRE-0015]: Looks like that did not solve the problem, exiting.")
      else:
        self.pos_tagged = []
        self.__POS_tag__()
    except:
      if(len(self.numeric_converted) == 0):
        self.__preprocessor_error__("[PRE-0016]: No data to POS tag!")
      else:
        self.__preprocessor_error__("[PRE-0017]: Unknown error during POS-tagging!")

  def __filter_empty_elements__(self, text):
    result = []
    for element in text:
      if(element != ''):
        result.append(element)
    return result
	
  def __lemmatize__(self):
    count = 0
    for entry in self.pos_tagged:
      count += len(entry)
    progressbar_object = pbc.Progressbar_class("[PRE]: Lemmatizing:",139,count+len(self.pos_tagged),2,"", self.guiobject, self.guiobject.lemmatizestatusstringvar, self.guiobject.progress, self.guiobject.progressstringvar, 65, 607)
    try:
      self.guiobject.lemmatizestatusstringvar.set("In Progress")
      self.guiobject.lemmatizestatus.config(fg='black', bg='yellow', text="" + str(self.guiobject.lemmatizestatusstringvar.get()))
      sleep(0.001)
      self.guiobject.window.update()
      lemmatizer = WordNetLemmatizer()
      for entry in self.pos_tagged:
        buffer = []
        for element in entry:
          progressbar_object.__update__()
          elementbuffer = (lemmatizer.lemmatize(element[0]), element[1])
          buffer.append(elementbuffer)
        self.lemmatized.append(buffer)
        progressbar_object.__update__()
      progressbar_object.__finalize__()
      self.guiobject.lemmatizestatusstringvar.set("Done.")
      self.guiobject.lemmatizestatus.config(fg='white', bg='green', text="" + str(self.guiobject.lemmatizestatusstringvar.get()))
      sleep(0.001)
      self.guiobject.window.update()
    except LookupError:
      self.errorcount = self.errorcount + 1
      print("[PRE]: Looks like WordNetLemmatizer data is not available. Automatically downloading some for you.")
      nltk.download('wordnet')
      print("[PRE]: All done. Retrying")
      if(self.errorcount >= 3):
        self.__preprocessor_error__("[PRE-00018]: Looks like that did not solve the problem, exiting.")
      else:
        self.lemmatized = []
        self.__lemmatize__()
    except:
      if(len(self.pos_tagged) == 0):
        self.__preprocessor_error__("[PRE-0019]: No data to lemmatize!")
      else:
        self.__preprocessor_error__("[PRE-0020]: Unknown error during lemmatizing!")
	
  def __finalize__(self):
    progressbar_object = pbc.Progressbar_class("[PRE]: Finalizing:",139,len(self.lemmatized),2,"", self.guiobject, self.guiobject.finalizestatusstringvar, self.guiobject.progress, self.guiobject.progressstringvar, 65, 607)
    try:
      self.guiobject.finalizestatusstringvar.set("In Progress")
      self.guiobject.finalizestatus.config(fg='black', bg='yellow', text="" + str(self.guiobject.finalizestatusstringvar.get()))
      sleep(0.001)
      self.guiobject.window.update()
      for i in range(len(self.lemmatized)):
        self.preprocessed_structure.append([self.lemmatized[i],self.category[i]])
        progressbar_object.__update__()
      progressbar_object.__finalize__()
      self.guiobject.finalizestatusstringvar.set("Done.")
      self.guiobject.finalizestatus.config(fg='white', bg='green', text="" + str(self.guiobject.finalizestatusstringvar.get()))
      sleep(0.001)
      self.guiobject.window.update()
    except:
      if(len(self.lemmatized) == 0):
        self.__preprocessor_error__("[PRE-0021]: No data to finalize!")
      else:
        self.__preprocessor_error__("[PRE-0022]: Unknown error during finalizing!")
	
  def __preprocessor_error__(self, message):
    print(message)
    exit()
	
  def __get_preprocessed_data__(self):
    if(self.preprocessed_structure!=[]):
      return self.preprocessed_structure
    else:
      print("Result seems to be empty. Did you run __process__()?")
      exit()