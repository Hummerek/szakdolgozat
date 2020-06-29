class AttributeObjectClass:
  AttributeName = ""
  AttributeValues = []
  def __init__(self, attributename):
    self.AttributeName = attributename
    self.AttributeValues = []
  def __add_attribute_value__(self, attributevalue):
    self.AttributeValues.append(attributevalue)
  def __dump_attribute__(self):
    print(self.AttributeName + ": " + str(self.AttributeValues))	