from DatabaseConstructor import DatabaseConstruct as DC
from DecisionTreeClassifier import DecisionTreeClassifier as DTC

DatabaseObject = DC.construct_database("D:/Szakdolgozat/nfr-20200323T145233Z-001/nfr/nfr.arff")
DecisionTreeClassificationObject = DTC.classify(DatabaseObject.DataRecordList, "SE")
#print("dumping:")
#DatabaseObject.__dump_database__()