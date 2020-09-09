import numpy as np
import matplotlib.pyplot as plt

class SupportVectorMachineClassifierClass:
  
#  def __init__(self):

  def __calculate_coords__(self, database, dictionary):
    dat = [[0, 0]]
    for dataline in database:
      print(dataline[0].DataBlockList)
      xcc, ycc = self.__get_coords__(dataline, dictionary)  
    #  print("Appending " + str(xcc) + "," + str(ycc) + ".")
      dat.append([xcc, ycc])
    for i in range(len(dat)):
      print(dat[i])
    x, y = zip(*dat)
    plt.scatter(x, y)
    plt.show()
 
  def __get_coords__(self, data, dictionary):
    xcoord = 0
    ycoord = 0
    ycoord = len(data[0].DataBlockList[1].split(' '))
    for element in data[0].DataBlockList[1]:
      for word in dictionary.WordDictionary.WeightDictionary:
        if (element == word[1] and word[2] > 0):
          xcoord = xcoord + word[2]
    return xcoord, ycoord
	
#  def __answer__(self):
  