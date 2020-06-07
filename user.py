class User:
  def __init__(self,id,name):
    self.id = id
    self.name = name

  def getName(self):
    return self.name

  def setName(self,newName):
      self.name = newName

  def toString(self):
    print("User with id",self.id,"and name",self.name)

  def show(self)
   print(".....")