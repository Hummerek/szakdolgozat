class BinaryTreeClass:
  Left = []
  Right = []
  Content = []
  Contentsize = 0
  Side = ""
  Count = 0
  def __init__(self):
    self.Left = []
    self.Right = []
    self.Content = []
    self.Side = ""
    self.Contentsize = 0
    self.Count = 0
  def __set_left_child__(self, child):
    self.Left = child
    self.__update_count__()
  def __set_right_child__(self, child):
    self.Right = child
    self.__update_count__()
  def __set_content__(self, side, content):
    self.Side = side
    self.Content = content
    self.Contentsize = len(content)
  def __get_content__(self):
    return self.Content
  def __update_count__(self):
    leftcount = 0
    rightcount = 0
    if(isinstance(self.Left,list)):
	  leftcount = 1
    else:
      leftcount = self.Left.__update_count__()
    if(isinstance(self.Right,list)):
	  rightcount = 1
    else:
      rightcount = self.Right.__update_count__()
    self.Count = leftcount + rightcount
    return self.Count
  def __print_tree__(self, level):
    print("[" + str(level) + "]("+self.Side+"):" + str(self.Contentsize) + ".. " + str(self.__get_content__()))
    if(self.Left):
      self.Left.__print_tree__(level+1)
    if(self.Right):
        self.Right.__print_tree__(level+1)
    if(self.Left == False):
      if(self.Right == False):
        print(str(self.Content))