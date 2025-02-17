# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["brand"]="fss"
# thisdict.update({"color": "red"})
# print(thisdict)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["year"]
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)


# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# print(myfamily["child1"]['name'])

# a = 33
# b = 20
# if b > a:
#   print("b is greater than a")


# a = 33
# b = 200
# if b > a:
#  print(b) # you will get an error
# a = 3
# b = 2
# if b > a:
#   print(b) # you will get an erro

# a = 33
# b = 3
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# elif a>b:
#   print(a)
# else:
#     print("empty")

# if a > b: print("a is greater than b")

# a = 2
# b = 330
# print("A") if a > b else print("B")

# a = 200
# b = 33
# c = 50
# if a > b and c > a:
#   print("Both conditions are True")


  
# a = 2
# b = 33
# c = 1
# if a > b or c > a:
#   print("conditions are True")


# a = 33
# b = 200
# if not a > b:    
#   print("a is NOT greater than b")


x = 1

if x > 10:
  print("Above ten,")
  if x > 0:
    print("and also above 20!")
  else:
    print("but not above 20.")