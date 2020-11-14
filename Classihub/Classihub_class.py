from Preprocessor import Preprocessor_class as pre
from Encoder import Encoder_class as enc
from Classifier import Classifier_class as cla
import sys

class Classihub_class:

  global_configuration_file = ""
  preprocessor_config_file = ""
  encoder_config_file = ""
  input_data_file = ""
  preprocessor_object = []
  encoder_object = []
  classifier_object = []
  preprocessed_data = []
  tfidf_data = []
  tfidf_feature_names = []
  gensim_data = []
  gensim_vocab_data = []
  glove_data = []

  def __init__(self):
    self.global_configuration_file = sys.argv[1]
    self.input_data_file = sys.argv[2]
    self.tfidf_data = []
    self.tfidf_feature_names = []
    self.gensim_data = []
    self.gensim_vocab_data = []
    self.glove_data = []

  def __process__(self):
    self.__load_global_configuration_file__()
    self.__load_preprocessor_object__()
    self.__preprocess__()
    self.__obtain_preprocessed_data__()
    self.__load_encoder_object__()
    self.__encode__()
    self.__obtain_tfidf_data__()
 #   self.__obtain_gensim_data__()
 #   self.__obtain_glove_data__()
    self.__load_classifier_object__()
    self.classifier_object.__perform__()

  def __load_global_configuration_file__(self):
    print("[CHB]: Loading global configuration file.")
    pre_loaded = False
    enc_loaded = False
    try:
      with open(self.global_configuration_file, "r") as file:
        for line in file.readlines():
          if(line.startswith("[PRE]:")):
            preprocessor_config_file = line[7:].rstrip()
            print("Preprocessor config will be found in file " + preprocessor_config_file)
            pre_loaded = True
          if(line.startswith("[ENC]:")):
            encoder_config_file = line[7:].rstrip()
            print("Encoder config will be found in file " + encoder_config_file)
            enc_loaded = True
      if(not(pre_loaded) or not(enc_loaded)):
        self.__classihub_error__("[CHB-0001]: Either the preprocessor or the encoder config is missing! Exiting.")
    except LookupError:
      self.__classihub_error__("[CHB-0002]: Could not load global configuration file, exiting.")
    except:
      self.__classihub_error__("[CHB-0003]: Unknown error occurred during loading the global configuration file. Exiting.")

  def __load_preprocessor_object__(self):
    print("[CHB]: Initializing preprocessor.")
    self.preprocessor_object = pre.Preprocessor_class(self.preprocessor_config_file, self.input_data_file)
	
  def __preprocess__(self):
    print("[CHB]: Preprocessing input data.")
    self.preprocessor_object.__process__()
	
  def __obtain_preprocessed_data__(self):
    print("[CHB]: Getting preprocessed data.")
    self.preprocessed_data = self.preprocessor_object.__get_preprocessed_data__()
	
  def __load_encoder_object__(self):
    print("[CHB]: Initializing encoder.")
    self.encoder_object = enc.Encoder_class(self.encoder_config_file, self.preprocessed_data)

  def __encode__(self):
    print("[CHB]: Encoding preprocessed data.")
    self.encoder_object.__process__()
	
  def __obtain_tfidf_data__(self):
    print("[CHB]: Getting TF-IDF data.")
    self.tfidf_data = self.encoder_object.__get_tfidf_data__()
  
#  def __obtain_gensim_data__(self):
#    print("[CHB]: Getting Gensim data.")
#    self.gensim_data, self.gensim_vocab_data = self.encoder_object.__get_gensim_data__()
  
#  def __obtain_glove_data__(self):
#    print("[CHB]: Getting GloVe data.")
#    self.glove_data = self.encoder_object.__get_glove_data__()
	
  def __load_classifier_object__(self):
    print("[CHB]: Initalizing classifier.")
    self.classifier_object = cla.Classifier_class()
    self.classifier_object.__set_tfidf_database__(self.tfidf_data)
#    self.classifier_object.__set_gensim_database__(self.gensim_data)
#    self.classifier_object.__set_glove_database__(self.glove_data)

  def __classihub_error__(self, message):
    print(message)
    exit()
	
  
	

