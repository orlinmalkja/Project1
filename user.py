class User:
  def __init__(self, ID, email, password,name,surname,age,status):
    self.id = ID
    self.email = email
    self.password = password
    self.name = name
    self.surname = surname
    self.age = age
    self.status = status
    #status do jet "admin" ose "user" si string, mund edhe ta bejme True ose False po nuk ka rendesi
    self.bills = []


  @classmethod
  def fromstring(cls,x):
    _ID,_email,_password, _name, _surname, _age, _status = x.split("-")
    return cls(_ID,_email,_password,_name, _surname,_age, _status)

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

  def getStatus(self):
    return self.status


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

  def setStatus(self, status):
    self.status = status
 
