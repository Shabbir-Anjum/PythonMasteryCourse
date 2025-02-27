# import mymodule

# mymodule.greeting("Jonathan")
# a = mymodule.person1["age"]
# print(a)
# import mymodule as mx

# a = mx.person1["age"]
# print(a)

# import platform

# x = platform.system()
# print(x)

# import datetime

# x = datetime.datetime.now()
# print(x)

# import datetime

# x = datetime.datetime.now()

# print(x.year)
# print(x.strftime("%A"))


# x = min(5, 10, 25)
# y = max(5, 10, 25)

# print(x)
# print(y)

# x = abs(-7.25)

# print(x)


# import math

# x = math.sqrt(64)

# print(x)


# import math

# x = math.ceil(1.1)
# y = math.floor(1.6)

# print(x) # returns 2
# print(y) # returns 1


import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-z]", txt)
print(x)
import re

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)

import re

txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

import re

txt = "The rain in Spain"
x = re.sub("\s", ", ", txt)
print(x)

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))