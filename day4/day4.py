thislist = ["branch", "apple", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["apple", "cango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse= True)
print(thislist)


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(thislist.copy())

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

fruits = ['apple', 'banana', 'cherry',"cherry"]

x = fruits.count("cherry")

print(x)