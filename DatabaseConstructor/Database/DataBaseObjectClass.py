class DataBaseObjectClass:
  DataBaseName = ""
  AttributeList = []
  DataRecordList = []
  datarecordcounter = 0
  attributecounter = 0
  def __init__(self, databasename):
    self.DataBaseName = databasename
    self.AttributeList = []
    self.DataRecordList = []
    self.datarecordcounter = 0
    self.attributecounter = 0
  def __add_attribute__(self, attribute):
    self.AttributeList.append([])
    self.AttributeList[self.attributecounter].append(attribute)
    self.attributecounter = self.attributecounter + 1
  def __add_data_record__(self, datarecord):
    self.DataRecordList.append([])
    self.DataRecordList[self.datarecordcounter].append(datarecord)
    self.datarecordcounter = self.datarecordcounter + 1
  def __dump_database__(self):
    print(self.DataBaseName)
    for attribute in self.AttributeList:
      attribute[0].__dump_attribute__()
    for data in self.DataRecordList:
        data[0].__dump_data__()