from sklearn.feature_extraction.text import TfidfVectorizer

class Encoder_class:
  errorcount = 0

  config = []
  configfile = ""
  input_data = []
  tfidf_data = []

  def __init__(self, configfile, inputdata):
    self.errorcount = 0
    self.config = []
    self.configfile = configfile
    self.input_data = inputdata
    self.tfidf_data = []
	
  def __process__(self):
    self.__parse_configuration__()
    self.__process_tf_idf_vectorization__()
		
  def __parse_configuration__(self):
    print("[ENC]: Parsing configuration file.")
    try:
      self.config = json.load(open(self.configfile))
    except:
      print("[ENC-0001]: Configuration file is not in JSON format!")

  def __process_tf_idf_vectorization__(self):
    vectorizer = TfidfVectorizer()
    temp = []
    for element in self.input_data:
      temp.append(self.__build_string__(element[0]))
    self.tfidf_data = vectorizer.fit_transform(temp)
    feature_names = vectorizer.get_feature_names()
    import pandas as pd
    df = pd.DataFrame(self.tfidf_data.T.todense(), index=feature_names)
    df.to_excel("kimenet.xlsx")

  def __build_string__(self, list):
    result = ""
    for element in list:
      result += str(element[0])+str(element[1])
      result += " "
    return result[:-1]

  def __encoder_error__(self, message):
    print(message)
    exit()
	
#  def __get_encoded_data__(self):
#    if(self.encoded_structure != []):
#      print("[ENC]: Loaded preprocessed data.")
#      return self.encoded_structure
#    else:
#      print("[ENC]: Result seems to be empty. Did you run __process__()?")
 #     exit()