import InputFileReader as IFR
import InputDataParser as IDP
from Database import DataBaseObjectClass as DBOC

def construct_database(fullpathtofile):
  datbname, attributes, data = IFR.read_input_file(fullpathtofile)
  result = DBOC.DataBaseObjectClass(datbname)
  print("[DatabaseConstructor] - Parsing attributes.")
  result = IDP.parse_attributes(result, attributes)
  print("[DatabaseConstructor] - Parsing data.")
  result = IDP.parse_data(result, data)
  print("[DatabaseConstructor] - Done.")
  return result