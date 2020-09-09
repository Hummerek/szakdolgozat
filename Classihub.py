from DatabaseConstructor import DatabaseConstruct as DC
from DecisionTreeClassifier import DecisionTreeClassifierClass as DTCC
from StringWeightCalculator import StringWeightCalculatorClass as SWCC
from SupportVectorMachineClassifier import SupportVectorMachineClassifierClass as SVMCC

weightsignificance = 10

print("[Classihub] - Caching learning data.")
DatabaseObject = DC.construct_database("D:/Szakdolgozat/nfr-20200323T145233Z-001/nfr/nfr.arff")

print("[Classihub] - Caching questionnaire.")
TestObject = DC.construct_database("D:/szakdolgozat/test.txt")

print("[Classhub] - Preprocessing learning data.")
DictionaryObject = SWCC.StringWeightCalculatorClass()
DictionaryObject.__process_calculation__(DatabaseObject.DataRecordList, "SE", weightsignificance)

print("[Classihub] - Running Decision Tree Classification.")
DecisionTreeClassificationObject = DTCC.DecisionTreeClassifierClass()
DecisionTreeClassificationObject.__classify__(DictionaryObject)
DecisionTreeClassificationObject.__answer__(DictionaryObject, TestObject.DataRecordList, weightsignificance)

#print("[Classihub] - Running Support Vector Machine Classification.")
#SupportVectorMachineClassificationObject = SVMCC.SupportVectorMachineClassifierClass()
#SupportVectorMachineClassificationObject.__calculate_coords__(DatabaseObject.DataRecordList, DictionaryObject)