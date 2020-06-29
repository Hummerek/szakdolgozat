from WeightDictionary import WeightDictionaryClass as WDC

class StringWeightCalculatorClass:
  LearningData = []
  ListOfWords = []
  WordDictionary = []
  ReqDictionary = []
  IsDataSet = False
  def __init__(self):
    self.LearningData = []
    self.ListOfWords = []
    self.WordDictionary = WDC.WeightDictionaryClass()
    self.ReqDictionary = WDC.WeightDictionaryClass()
    self.IsDataSet = False
  def __process_calculation__(self, data, searchedparam):
    print("[DecisionTree] - Receiving data.")
    self.__set_data__(data)
    print("[DecisionTree] - Building word list.")
    self.__build_word_list_from_data__()
    print("[DecisionTree] - Building word dictionary.")
    self.__build_word_dictionary__(searchedparam)
    print("[DecisionTree] - Building req dictionary.")
    self.__build_req_dictionary__(self.LearningData, self.WordDictionary)
    print(str(self.ReqDictionary))
  def __build_word_dictionary__(self, searchedparam):
    for word in self.ListOfWords:
      element = self.__calculate_weight__(word, searchedparam)
      self.WordDictionary.__add_record__(element)
  def __build_req_dictionary__(self, data, dictionary):
    score = 0
    for req in data:
      score = 0
      wordlist = req[0].DataBlockList[1].split(' ')
      for wd in wordlist:
        formattedword = self.__format_word__(wd)
        tempscore = self.__get_score_from_list__(formattedword)
        score = score + int(tempscore)
      result = []
      result.append(req[0].DataBlockList[1])
      result.append(score)
      print("Adding record: " + str(req[0].DataBlockList[2]) + "   " + str(result))
      self.ReqDictionary.__add_record__(result)
  def __get_score_from_list__(self, word):
    score = -1000
    for entry in self.WordDictionary.WeightDictionary:
#      print("Checking " + str(entry[1]) + " against " + str(word) + ".")	
      if(entry[1] == word):
        score = entry[2]
    return score
  def __calculate_weight__(self, word, searchedparam):
    weight = 0
    for entry in self.LearningData:
      entry = entry[0].DataBlockList
      textparam = entry[2]
      tokenizedentry = entry[1].split(' ')
      for wd in tokenizedentry:
        if(word == wd):
          if(textparam == searchedparam):
            weight = weight+10
          else:
            weight = weight-1
    result = []
    result.append(word)
    result.append(weight)
    return result
  def __build_word_list_from_data__(self):
    if(self.IsDataSet == True):
      for entry in self.LearningData:
        entry = entry[0].DataBlockList
        textparam = entry[2]
        tokenizedentry = entry[1].split(' ')
        for wd in tokenizedentry:
          wd = self.__format_word__(wd)
          checkword = self.__is_this_word_new__(wd)
          if(checkword == True):
            self.ListOfWords.append(wd)
  def __set_data__(self, data):
    self.LearningData = data
    self.IsDataSet = True
  def __format_word__(self, word):
    word = word.replace('.','')
    word = word.replace(',','')
    word = word.replace('!','')
    word = word.replace('\x91','')
    word = word.replace('\x92','')
    word = word.replace('(','')
    word = word.replace(')','')
    word = word.replace('\x93','')
    word = word.replace('\x94','')
    return word
  def __is_this_word_new__(self, wd):
    result = True
    for word in self.ListOfWords:
      if (word == wd):
        result = False
    return result
