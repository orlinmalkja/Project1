class User:
  def __init__(self, ID, email, password,name,surname,age):
    self.id = ID
    self.email = email
    self.password = password
    self.name = name
    self.surname = surname
    self.age = age
    self.bills = []


  @classmethod
  def fromstring(cls,x):
    _ID,_email,_password, _name, _surname, _age = x.split("-")
    return cls(_ID,_email,_password,_name, _surname,_age)

#getters

  def getID(self):
    return self.id

  def getEmail(self):
   return self.email

  def getPassword(self):
    return self.password

  def getName(self):
    return self.name

  def getSurname(self):
    return self.surname

  def getAge(self):
    return self.age



#setters 

  def setID(self,ID):
    self.id = ID

  def setEmail(self,email):
    self.email = email

  def setPassword(self,password):
    self.password = password

  def setName(self,name):
    self.name = name

  def setSurname(self,surname):
    self.surname = surname

  def setAge(self,age):
    self.age = age

 
