
# try:
#     print(x)
# except:
#    print("An errror")


# try:
#   print(x==4)
# except NameError:
#   print("Variable is not defined")
# except:
#   print("Something else went wrong")

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

# try:
#   print("x")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")
# finally:
#   print("The 'try except' is finished")

# username = input("Enter username:")
# print("Username is: " + username)

# txt = f"The price is 49 dollars"
# print(txt)

# price = input("value: ")
# txt = f"The price is {price} dollars"
# print(txt)


# price = 49
# txt = "The price is {} dollars"
# print(txt.format(price))


# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
# print(myorder.format(quantity, itemno, price))
f = open("D:/Coding/Python/course/Day 16/demofile.txt",'r')
# print(f.read())

# f = open("D:/Coding/Python/course/Day 16/demofile.txt", "r")
# print(f.read(7))

# print(f.readline())

# for x in f:
#   print(x)

# f = open("D:/Coding/Python/course/Day 16/demofile.txt",'w')
# f.write("Now the file has more content!")
# f.close()

# #open and read the file after the appending:
# f = open("D:/Coding/Python/course/Day 16/demofile.txt",'r')
# print(f.read())


# f = open("D:/Coding/Python/course/Day 16/demofile.txt",'w')
# f.write("new text!")
# f.close()

# #open and read the file after the appending:
# f = open("D:/Coding/Python/course/Day 16/demofile.txt",'r')
# print(f.read())
# f = open("D:/Coding/Python/course/Day 16/myfile.txt", "x")
import os
os.remove("D:/Coding/Python/course/Day 16/myfile.txt")