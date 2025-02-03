x = ["apple", "banana", "cherry","a","b"]
a="apple"
b="banana"

print(x[1])

b = "Hello,World!"


print(b[5:7])
a = "Hello, World! HELLO WORD"
print(a.lower())
print(a.upper())

a = "            Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello,tt, World!"
new=a.split(",")
print(new) # returns ['Hello', ' World!']


a = "Hello"
b = "World"
c = a + " " + b +" " +"good" + str(2)
print(c)