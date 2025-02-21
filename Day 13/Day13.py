# class MyClass:
#   x = 5


# class Person:
#   def __init__(self, name, age, v):
#     self.name = name
#     self.age = age
#     self.v = v

# p1 = Person("John", 36,2)

# print(p1.name)
# print(p1.age)
# print(p1.v)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}{self.age}"

# p1 = Person("John", 36)

# print(p1)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)
#   def myf(self):
#     print("Hello " + self.name)
  
# p1 = Person("John", 36)
# print(p1)
# p1.myfunc()
# p1.myf()

# class Person:
#   def __init__(my, name, age):
#     my.name = name
#     my.age = age

#   def myfunc(a):
#     print("Hello my name is " + str(a.age))

# p1 = Person("John", 36)
# p1.age = 40
# del p1.name
# p1.myfunc()


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
# x.printname()

# class Student(Person):
#   pass

# x = Student("Mike", "Olsen")
# x.printname()
# class Student(Person):
#   def __init__(self, fname, lname):
#    Person.__init__(self, fname, lname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)
#     self.graduationyear = 2019

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year
#     self.fname=fname
#     self.year

# y = Student("Mike", "Ol", 2019)
# print(y.fname)

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()