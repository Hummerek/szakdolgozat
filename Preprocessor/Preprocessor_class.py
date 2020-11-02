import nltk, re, pprint
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import json

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
    self.punctuation_marks_to_remove = [',', '.', '!', '?', ':', '(', ')', '@', '&', "$", "%", '#', '<', '>', "'", "•", "	", "-"]
    self.punctuation_marks_to_convert = ["/"]
    self.punctuation_filtered = []
    self.indicator_list = ["am", "pm", "k", "mb", "kb", "gb", "min", "m", "h", "s"]
    self.separator_list = ["x", ".", " ", ","]
    self.numeric_converted = []
    self.pos_tagged = []
    self.lemmatized = []
    self.preprocessed_structure = []
	
  def __process__(self):
    self.__parse_configuration__()
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
    print("[PRE]: Generating raw data.")
    skipping_lines = True
    try:
      with open(self.datafile, 'r') as inputfile:
        for line in inputfile.readlines():
          if(skipping_lines == False):
            strippedline = line.strip()
            self.raw_data.append([strippedline])
          if(line.startswith("@DATA")):
            skipping_lines = False
    except:
      self.__preprocessor_error__("[PRE-0001]: Failed to read data file!")
  
  def __load_stopword_list__(self):
    print("[PRE]: Loading stopword list.")
    try:
      self.stop_words = set(stopwords.words('english'))
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
    print("[PRE]: Tokenizing.")
    i = 1
    try:
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
        i += 1
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
    print("[PRE]: Normalizing tokens.")
    try:
      for element in self.tokens:
        buffer = []
        for word in element:
          buffer.append(word.lower())
        self.normalized_tokens.append(buffer)
    except:
      if(len(self.tokens) == 0):
        self.__preprocessor_error__("[PRE-0006]: No tokens to normalize!")
      else:
        self.__preprocessor_error__("[PRE-0007]: Unknown error during normalization of tokens!")

  def __filter_stopwords__(self):
    print("[PRE]: Filtering stopwords.")
    try:
      for element in self.normalized_tokens:
        buffer = []
        for word in element:
          if(word not in self.stop_words):
            buffer.append(word)
        self.stopword_filtered.append(buffer)
    except:
      if(len(self.normalized_tokens) == 0):
        self.__preprocessor_error__("[PRE-0008]: Cannot filter stopwords, no words to filter!")
      if(len(self.stop_words) == 0):
        self.__preprocessor_error__("[PRE-0009]: Cannot filter stopwords, no stopwords recorded!")
      else:
        self.__preprocessor_error__("[PRE-0010]: Unknown error during filtering stopwords!")
		
  def __filter_punctuation_from_words__(self):
    print("[PRE]: Filtering punctuation.")
    try:
      for element in self.stopword_filtered:
        filtered = self.__filter_word__(element)
        self.punctuation_filtered.append(filtered)
    except:
      if(len(self.stopword_filtered) == 0):
        self.__preprocessor_error__("[PRE-0011]: No data to filter punctuation on!")
      else:
        self.__preprocessor_error__("[PRE-0012]: Unknown error during filtering of punctuation!")

  def __filter_word__(self, entry):
    filtered_entry = []
    for word in entry:
      for filter in self.punctuation_marks_to_remove:
        word = word.replace(filter,' ')
      for filter in self.punctuation_marks_to_convert:
        word = word.replace(filter,' ')
      word = word.strip()
      filtered_entry.append(word)
    return filtered_entry
	
  def __merge_numeric_tokens__(self):
    print("[PRE]: Merging numeric tokens.")
    try:
      for element in self.punctuation_filtered:
        buffer = []
        for word in element:
          word = self.__remove_indicator__(word)
          if(word.isnumeric() or self.__separable_number__(word)):
            buffer.append("QNUM")
          else:
            buffer.append(word)
        self.numeric_converted.append(buffer)
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
    print("[PRE]: POS-tagging.")
    try:
      for element in self.numeric_converted:
        pos_tagged_temp = nltk.pos_tag(self.__filter_empty_elements__(element))
        if(pos_tagged_temp != []):
          self.pos_tagged.append(pos_tagged_temp)
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
    print("[PRE]: Lemmatizing.")
    try:
      lemmatizer = WordNetLemmatizer()
      for entry in self.pos_tagged:
        buffer = []
        for element in entry:
          elementbuffer = (lemmatizer.lemmatize(element[0]), element[1])
          buffer.append(elementbuffer)
        self.lemmatized.append(buffer)
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
    print("[PRE]: Finalizing.")
    try:
      for i in range(len(self.lemmatized)):
        self.preprocessed_structure.append([self.lemmatized[i],self.category[i]])
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
      print("[PRE]: Loaded preprocessed data.")
      return self.preprocessed_structure
    else:
      print("Result seems to be empty. Did you run __process__()?")
      exit()