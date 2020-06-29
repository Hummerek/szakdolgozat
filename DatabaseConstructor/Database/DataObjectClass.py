class DataObjectClass:
  DataObjectID = ""
  DataBlockList = []
  def __init__(self, dataobjectid):
    self.DataObjectID = dataobjectid
    self.DataBlockList = []
  def __add_data_block__(self, datablock):
    self.DataBlockList.append(datablock)
  def __dump_data__(self):
    print(str(self.DataObjectID) + ": " + str(self.DataBlockList))