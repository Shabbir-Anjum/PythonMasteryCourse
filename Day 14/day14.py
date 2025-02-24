# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# mystr = "banana"
# myit = iter(mystr)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# mytuple = ("apple", "banana", "cherry")

# for x in mytuple:
#   print(x)


# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Drive!")

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Sail!")

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# for x in (car1, boat1, plane1):
#   x.move()

# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Move!")

# class Car(Vehicle):
#   pass

# class Boat(Vehicle):
#   def moves(self):
#     print("Sail!")

# class Plane(Vehicle):
#   def moves(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object
# # print(car1.brand)
# # print(car1.model)
# # car1.move()
# # print(boat1.brand)
# # print(boat1.model)
# # boat1.move()
# for x in (boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()
#   x.moves()

# y=400
# def myfunc():
#  x = 300
#  print(x)
#  print(y)
# print(y)
# myfunc()
# print(100)



# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
#   myinnerfunc()

# myfunc()

# def myfunc():
#   global x
#   x = 300

# myfunc()

# print(x)

# def myfunc1():
#   x = "Jane"

#   def myfunc2():
#     nonlocal x
#     x = "hello"
#   myfunc2()
#   print(x)
#   return x

# print(myfunc1())



x = 300
def myfunc():
  x = 200
myfunc()
print(x)