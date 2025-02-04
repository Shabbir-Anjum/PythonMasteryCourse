b = "Hello, World!"
print(b[7:12])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = "          Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

b=a.split(",")
print(b[0][4])


a = "Hello"
b = "World"
c = a + b + "good"
print(c)


age = 36
txt = "My name is John, I am  36" + str(age)
print(txt)


price = 59
txt = f"The price is {price:.4f} dollars" 
print(txt)


txt = f"The price is {20 * 59} dollars"
print(txt)

txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)


print(10 > 9)
print(10 == 9)
print(10 < 9)


bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
print(bool("abc"))

print((6 + 3) - (6 + 3))


c=3+5+6


x = 5

x += 3

print(x)



mylist = ["apple", "banana", "cherry"," todo", 2]

print(mylist[4])


thislist = ["apple", "banana", "cherry"]
print(thislist[0])

j=("apple", "banana", "cherry", 4)
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

print(j)



thislist = ["apple", "banana", "cherry"]
print(thislist[-2])



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[4:])


thislist = ["apple", "banana", "cherry"]
print(thislist[1])
thislist[1] = "blackcurrant"
print(thislist[1])
print(thislist)



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

print(thislist[1:3])
thislist[0:2] = ["blackcurrant", "watermelon", "app,e", "mang"]
a,b= 1,2
print(thislist[0][1][0])


thislist = ["apple", "banana", "cherry"]
thislist[1] = ["blackcurrant", "watermelon"]
print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.insert(0, "watermelon")
print(thislist)


mylist = ['apple', 'banana', 'cherry']
mylist.insert(2, "kivi")
print(mylist)


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)



thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)




thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)