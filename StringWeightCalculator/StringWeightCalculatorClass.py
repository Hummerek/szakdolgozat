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
  def __process_calculation__(self, data, searchedparam, weightsignificance):
    print("[DecisionTree] - Receiving data.")
    self.__set_data__(data)
    print("[DecisionTree] - Building word list.")
    self.__build_word_list_from_data__()
    print("[DecisionTree] - Building word dictionary.")
    self.__build_word_dictionary__(searchedparam, weightsignificance)
    print("[DecisionTree] - Building req dictionary.")
    self.__build_req_dictionary__(self.LearningData, self.WordDictionary)
  def __build_word_dictionary__(self, searchedparam, weightsignificance):
    for word in self.ListOfWords:
      element = self.__calculate_weight__(word, searchedparam, weightsignificance)
      print("Element: " + element[0] + " " + str(element[1]))
      self.WordDictionary.__add_record__(element)
  def __build_req_dictionary__(self, data, dictionary):
    score = 0
    for req in data:
      score = self.__calculate_score_for__(req)
      result = []
#	      result.append(req[0].DataBlockList[1])
      result.append(score)
#      print("Adding record: " + str(req[0].DataBlockList[2]) + "   " + str(result))
      self.ReqDictionary.__add_req_record__(str(req[0].DataBlockList[2]), result)
  def __calculate_score_for__(self, req):
   # print("calculating score for: " + str(req[0].DataBlockList))

    score = 0
    wordlist = req[0].DataBlockList[1].split(' ')
    reqsize = len(wordlist)
    for wd in wordlist:
      formattedword = self.__format_word__(wd)
      tempscore = self.__get_score_from_list__(formattedword)
 #     print("Increasing score by " + str(tempscore) + "for the word " + formattedword)
      score = score + int(tempscore)
 #     print("Score is therefore now " + str(score))
    score = score/reqsize
 #   print("Score for " + req[0].DataBlockList[1] + " is: " + str(score))
    return score
  def __get_score_from_list__(self, word):
    score = 0
    for entry in self.WordDictionary.WeightDictionary:
#      print("Checking " + str(entry[1]) + " against " + str(word) + ".")	
      if(entry[1] == word):
        score = entry[2]
    return score
  def __calculate_weight__(self, word, searchedparam, weightsignificance):
#legyen a kezdeti suly 0
#    print("resetting.")
    weight = 0
#minden learning recordban
    for entry in self.LearningData:
#A DataBlockList az entry azon elementje, amivel foglalkozunk
      entry = entry[0].DataBlockList
#A DataBlockList harmadik tagja tartalmazza a requirement kategoriajat
      textparam = entry[2]
#A requirement szoveget szavakra bontjuk
      tokenizedentry = entry[1].split(' ')
#A kezdeti frekvencia 0
      freq = 0
#minden kapott szora
      for wd in tokenizedentry:
#ha a keresett szo ugyanaz mint a vizsgalt szo
        if(word == wd):
#ha a keresett parameter ugyanaz mint a vizsgalt parameter, pl 'SE'
          if(textparam == searchedparam):
#akkor noveljuk a sulyt
            weight = weight+weightsignificance
#            print("Word " + word + " + 1000, so " + str(weight))
#minden talalattal noveljuk a freqt
            freq = freq + 1
#egyebkent pedig csokkentjuk a sulyt
          else:
            weight = weight - 1
#            print("Word " + word + " - 1, so " + str(weight))
#a frekvencia attol no
            freq = freq + 1
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
    word = word.lower()
    return word
  def __is_this_word_new__(self, wd):
    result = True
    for word in self.ListOfWords:
      if (word == wd):
        result = False
    return result
