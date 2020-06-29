from Database import AttributeObjectClass as AOC
from Database import DataObjectClass as DOC

def parse_attributes(Datab, attriblist):
  for attribute in attriblist:
    attribute = str(attribute.rstrip()).split(' ')
    AttributeObject = AOC.AttributeObjectClass(attribute[1])
    attribute = (attribute[2].split("%"))[0].rstrip().replace('{','').replace('}','').split(',')
    for attrvalue in attribute:
      AttributeObject.__add_attribute_value__(attrvalue)
    Datab.__add_attribute__(AttributeObject)
    del AttributeObject
  return Datab

def parse_data(Datab, datalist):
  start_id = 0
  for dataentry in datalist:
    DataObject = DOC.DataObjectClass(start_id)
    dataentry = dataentry.split(',')
    for element in dataentry:
      element = element.replace("'", '').lstrip().rstrip()
      DataObject.__add_data_block__(element)
    start_id = start_id+1
    Datab.__add_data_record__(DataObject)
    del DataObject
  return Datab