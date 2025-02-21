# def my():
#   print("Hello from a function")
# my()

# def my_function(fname):
#   c=fname +"string"
#   print(c)
#   print(fname +" Refsnes")

# my_function("1")
# def my_function(fname, lname, age):
#   print(fname + " " + lname +" ", age)

# my_function("Emil", "Refsnes",1)

# def my_function(*kids):
#   print("The youngest child is " + kids[1])

# my_function("Emil", "Tobias", "Linus")

# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")


# def my_function(country= "Norway"):
#   print("I am from " + country)


# my_function("Sweden")
# my_function("India")
# my_function()
# def my(food):
#   print(food)
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my(fruits)

# def my_function(x):
#   print(x)
#   return 5 * x
# x=my_function(10)
# print(x)
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# def myfunction():
#   pass

# def my_function(*, x):
#   print(x)

# my_function(x=3)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)


a=[1,2,3]
b=[3,4,5]
a.append(b)
print(a)