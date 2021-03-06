import sys
import tkinter
from time import sleep

class Progressbar_class:
  title=""
  width=0
  upper_limit = 0
  progress_unit = 0
  progress = 0
  percentage = 0.0
  current_progress = 0
  bar_string = ""
  details_string = ""
  full_print_data_string = ""
  scale = 0
  scale_precision = 0
  scale_info = 0
  prev_scale_info = 0
  inverted_scale = False
  finalmessage=""
  progress_step = 0
  guiobject_statuslabel = []
  guiobject_progressbar_label = []
  guiobject_progressbar_parent = []
  guiobject = []
  locx = 0
  locy = 0
  

  def __init__(self, title, width, limit, scale, finalmessage, guiobject, guiobject_statuslabel, guiobject_progressbar_parent, guiobject_progressbar_label, locx, locy):
    self.guiobject_statuslabel = guiobject_statuslabel
    self.guiobject_progressbar_label = guiobject_progressbar_label
    self.guiobject_progressbar_parent = guiobject_progressbar_parent
    self.guiobject = guiobject
    self.locx = locx
    self.locy = locy
    self.title = title.ljust(40)
    self.width = width
    self.upper_limit = limit
    self.progress_step = 1
    if(limit < 130):
      self.upper_limit *= 2
      self.progress_step = 2
    self.progress_unit = int(self.upper_limit/(self.width+1))
    self.progress = 0
    self.percentage = 0.0
    self.current_progress = 1
    self.bar_string = ""
    self.details_string = ""
    self.full_print_data_string = ""
    self.scale_precision = scale
    self.inverted_scale = False
    self.finalmessage=finalmessage
    self.__calculate_scale__(self.scale_precision)
    self.scale_info = 0
    self.__update_scale_info__()
    self.__initialize__()

  def __initialize__(self):
    print("a")
    #sys.stdout.write(self.title+"[{0}]".format(" " * self.width))
    #sys.stdout.flush()
    #sys.stdout.write("\b" * (self.width+len(self.title)+1))
	
  def __update__(self):
    self.current_progress += self.progress_step
    self.__update_scale_info__()
    if((self.inverted_scale == True) or (self.inverted_scale == False and (int(self.scale_info) != int(self.prev_scale_info)))):
      self.__update_percentage__()
      self.__update_progress__()
      self.__update_bar__()
      self.__update_details__()
      self.__display__()

  def __calculate_scale__(self, scale):
    self.scale = 100.0
    for i in range(scale):
      self.scale *= 10.0
    if(int(self.scale) > self.upper_limit):
      self.inverted_scale = True
      self.__normalize_scale__()
    self.scale = self.upper_limit/self.scale
	
  def __normalize_scale__(self):
    while(int(self.scale) > self.upper_limit):
      self.scale /= 10.0
	
  def __update_scale_info__(self):
    self.prev_scale_info = self.scale_info
    self.scale_info = float(self.current_progress)/self.scale
	
  def __update_percentage__(self):
    self.percentage = "{:.{}f}".format((float(self.current_progress)/float(self.upper_limit))*100, self.scale_precision)
	
  def __update_progress__(self):
    new_progress = round(int(self.current_progress/self.progress_unit))
    if(new_progress > self.width):
      self.progress = self.width
    else:
      self.progress = new_progress
	
  def __update_bar__(self):
    self.bar_string = "["
    if(self.progress >=1):
      for i in range(self.progress):
        self.bar_string += "-"
    self.bar_string += ">"
    if(self.progress <1):
      for i in range(self.width):
        self.bar_string += "/"
    else:
      for i in range(self.width-self.progress):
        self.bar_string += "/"
    self.bar_string += "]"
	
  def __update_details__(self):
    self.details_string = "" + str(self.percentage) + "% (" + str(int(self.current_progress/self.progress_step)) + "/" + str(int(self.upper_limit/self.progress_step)) + ")"

  def __display__(self):
    self.full_print_data_string = "" + self.bar_string.rjust(110)
    self.guiobject_progressbar_label.set(self.full_print_data_string)
    self.guiobject.percentagestringvar.set(self.details_string)
    self.guiobject.tasktitlestringvar.set(self.title)
    self.guiobject_progressbar_parent.config(text="" + str(self.guiobject_progressbar_label.get()))
    self.guiobject.percentage.config(text="" + str(self.guiobject.percentagestringvar.get()))
    self.guiobject.tasktitle.config(text="" + str(self.guiobject.tasktitlestringvar.get()))
    self.guiobject.window.update()
    #self.guiobject_progressbar_parent.place(x=self.locx, y=self.locy)
    #sys.stdout.write("\b" * (len(self.full_print_data_string) + 2))
    #sys.stdout.write(self.full_print_data_string)
    #sys.stdout.flush()

  def __update_final_message__(self, message):
    self.finalmessage = message

  def __finalize__(self):
    print("a")
    #sys.stdout.write("\b" * len(self.details_string))
    #sys.stdout.write("Done. {}{}\n".format(self.finalmessage, " " * (len(self.details_string)-(len(self.finalmessage)+3))))
    #sys.stdout.write("Done. {}{}\n".format(self.finalmessage, " " * (len(self.details_string)-(len(self.finalmessage)+3))))
    #sys.stdout.flush()