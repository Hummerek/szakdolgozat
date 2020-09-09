from BinaryTree import BinaryTreeClass as BTC

class DecisionTreeClassifierClass:
  level = 0
  DecisionTreeRoot = ""
  minval = 0
  maxval = 0
  
  def __init__(self):
    self.level = 0
    self.minval = 0
    self.maxval = 0
    self.DecisionTreeRoot = BTC.BinaryTreeClass()

  def __classify__(self, dictionary):
    WeightDict = dictionary.ReqDictionary.WeightDictionary
    print("[DecisionTree] - Sorting data.")
    WeightDict = self.__sort_data__(WeightDict, 2)
    print("[DecisionTree] - Building Binary Tree")
    self.DecisionTreeRoot = self.__buildtree__(WeightDict, self.DecisionTreeRoot, 1)
    self.DecisionTreeRoot.__set_content__("DecisionTreeRoot", [self.DecisionTreeRoot.Left.__get_content__()[0], self.DecisionTreeRoot.Right.__get_content__()[1]])
    print("[DecisionTree] - Done.")
    self.DecisionTreeRoot.__print_tree__(0)
  
  def __buildtree__(self, data, set, value):
    self.level = self.level + 1
    setsize = 0.0 + len(data)
    cutsize = 0
    leftlist = []
    left = BTC.BinaryTreeClass()
    rightlist = []
    right = BTC.BinaryTreeClass()
    cutsize = setsize/2
    index = 0
    for element in data:
      if(index < cutsize):
        leftlist.append(element)
      else:
        rightlist.append(element)
      index = index + 1
    if(self.__there_are_different_elements_in__(leftlist) and len(leftlist) > 1):
      left.__set_content__("left", leftlist)
      left = self.__buildtree__(left.__get_content__(), left, value)
      if(len(left.__get_content__()) > 1):
        if(self.__getmin__(leftlist) < self.minval):
          self.minval = self.__getmin__(leftlist)
        if(self.__getmax__(leftlist) < self.maxval):
          self.maxval = self.__getmax__(leftlist)
        left.__set_content__("left", [self.__getmin__(leftlist), self.__getmax__(leftlist)-1])
    else:
      temp = leftlist[0]
      left.__set_content__("left", [temp[2]])
    if(self.__there_are_different_elements_in__(rightlist) and len(rightlist) > 1):
      right.__set_content__("right", rightlist)
      right = self.__buildtree__(right.__get_content__(), right, value)
      if(len(right.__get_content__()) > 1):
        if(self.__getmin__(rightlist) < self.minval):
          self.minval = self.__getmin__(rightlist)
        if(self.__getmax__(rightlist) < self.maxval):
          self.maxval = self.__getmax__(rightlist)
        right.__set_content__("right", [self.__getmin__(rightlist), self.__getmax__(rightlist)])
    else:
      temp = rightlist[0]
      right.__set_content__("right", [temp[2]])
    if(not(isinstance(set, list))):
      set.__set_left_child__(left)
      set.__set_right_child__(right)
    self.level = self.level-1
    return set
  
  def __there_are_different_elements_in__(self, list):
    result = False
    firsttime = True
    type = 0
    for element in list:
      if(firsttime == True):
        type = element[2]
        firsttime = False
      if(element[2]!=type):
        result = True
    return result
 
  def __getmin__(self, list):
    result = 1000000
    for element in list:
      if(element[2]<result):
        result = element[2]
    return result
  
  def __getmax__(self, list):
    result = -1000000
    for element in list:
      if(element[2]>result):
        result=element[2]
    return result
  
  def __sort_data__(self, data, param): 
    length = len(data) 
    for i in range(0, length): 
      for j in range(0, length-i-1): 
          if (data[j][param] > data[j + 1][param]): 
            temp = data[j] 
            data[j]= data[j + 1] 
            data[j + 1]= temp 
    return data

  def __answer__(self, dictionary, testdatabase, weightsignificance):
    testresult = 0
    for testdata in testdatabase:
      testresult = self.__test_data__(dictionary, testdata)
      deviation = (abs(self.minval) + abs(self.maxval))/2/weightsignificance
      classification = self.__evaluate_data__(testresult, 0.833, deviation, testresult)
      print(str(testresult) + " so classification came out to be " + str(classification))
  
  def __test_data__(self, dictionary, data):
    resultscore = 0
    resultscore = dictionary.__calculate_score_for__(data)
    return resultscore
  def __evaluate_data__(self, score, threshold, deviation, testresult):
    result = 0
    decisions = 0
    State = self.DecisionTreeRoot
    examined = State.__get_content__()
    while(len(examined) != 1):
      if(len(examined)==2):
        if(score <= ((examined[0]+examined[1])/2)):
          State = State.Left
          examined = State.__get_content__()
          decisions = decisions +1
        else:
          State = State.Right
          examined = State.__get_content__()
          result = result+1
          decisions = decisions + 1
 #   print("Calculating intermediate, 0.0 + (" + str(result) + "/" + str(decisions) + "). Results in " + str(0.0+(float(result)/float(decisions))))
    intermediate = 0.0 + (float(result)/float(decisions))
#    print("Checking intermediate " + str(intermediate) + " against threshold " + str(threshold) + ".")
    if(intermediate >= threshold and testresult > (0.0-deviation)):
      return True
    else:
      return False