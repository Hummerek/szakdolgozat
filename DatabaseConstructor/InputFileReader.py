import os
import ntpath

def read_input_file(LearningDatabaseFullPath):
  databasename = ""
  attributes = []
  data = []
  CurrentDirectory = os.getcwd()
  LearningDatabaseFileName = ntpath.basename(LearningDatabaseFullPath)
  LearningDatabasePath = LearningDatabaseFullPath.replace(LearningDatabaseFileName,'')
  os.chdir(LearningDatabasePath)
  LearningDatabase = open(LearningDatabaseFileName,"r")
  
  for line in LearningDatabase:
    result = filter_comments_and_whitespace(line)
    #excluding comments and empty lines
    if(result != ""):
      if(result.startswith("@RELATION")):
        databasename = result.replace("@RELATION ","").rstrip()
        continue
      if(result.startswith("@ATTRIBUTE")):
        attributes.append(result.rstrip())
        continue
      #parsing DATA tag is not needed
      if(not(result.startswith("@DATA"))):
        data.append(result.rstrip())
        continue
  LearningDatabase.close()
  os.chdir(CurrentDirectory)
  return databasename, attributes, data
  
def filter_comments_and_whitespace(line):
  result = ""
  if(not(line.startswith('%'))):
    line = line.lstrip()
    if(line.rstrip()):
      result = line
  return result