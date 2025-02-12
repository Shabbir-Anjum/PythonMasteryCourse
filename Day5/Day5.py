# mytuple = ("apple", "banana", "cherry",2, 2.2)

# print(mytuple[0])


# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))

# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))

# value=["apple", "banana", "cherry"]
# thistuple = tuple(value) # note the double round-brackets
# print(thistuple)
# print(type(thistuple))


# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])


# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])


# x = ("apple", "banana", "cherry")
# y = list(x)
# print(y)
# y[0] = "kiwi"
# x = tuple(y)

# print(x)


# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple =thistuple + y

# print(thistuple)

# thistuple = ("apple", "banana", "cherry")

# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists



# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)



# fruits = ("apple","dd", "banana", "cherry", "strawberry", "raspberry","value")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)



# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)


tuple1 = ("a", "b" , "c")
tuple2 = ("r","3")

tuple3 = tuple1 + tuple2
print(tuple3)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)


# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)

# thisset = {"apple", "banana", "cherry", True, 1, 2}

# print(thisset)
fruits,t,c = ["apple", "banana", "cherry"]
print(fruits,t,c)