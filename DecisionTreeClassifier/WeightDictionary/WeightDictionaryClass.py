class WeightDictionaryClass:
  Index = 0
  WeightDictionary = []
  def __init__(self):
    self.Index = 0
    self.WeightDictionary = []
  def __add_record__(self, record):
    self.WeightDictionary.append([self.Index, record[0], record[1]])
    self.Index = self.Index+1