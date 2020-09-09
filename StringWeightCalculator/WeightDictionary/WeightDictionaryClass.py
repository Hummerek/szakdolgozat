class WeightDictionaryClass:
  Index = 0
  WeightDictionary = []
  def __init__(self):
    self.Index = 0
    self.WeightDictionary = []
  def __add_record__(self, record):
    self.WeightDictionary.append([self.Index, record[0], record[1]])
    self.Index = self.Index+1
	
  def __add_req_record__(self, category, record):
    if (category == "SE"):
      category = 1
    else:
      if (category == "LF"):
        category = 2
      else:
        category = 0
    self.WeightDictionary.append([category, self.Index, record[0]])
    self.Index = self.Index+1