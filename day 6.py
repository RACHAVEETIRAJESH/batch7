# 1.) Python program to capitalize the first and last character of each
# # word in a string 
# str1="anand"
# fst = str1[0].upper()
# lst = str1[-1].upper()
# print(fst+str1[1:len(str1)-1]+lst)
# print(str1.replace('a', 'A'))
# print(str1.replace('d', 'D'))

# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

# n = 128
# for i in n:
#     print(i)

# n = 128
# i = 0 
# while n!=0:
#     rem = n%10
#     print(" the value of rem  ", rem)
#     n = n//10
    
# n = 128
# temp = n
# str1 = ""
# i = 0 
# while n!=0:
#     rem = n%10
#     check = temp % rem
#     if check ==0:
#         print("yes")
#     else:
#         print("no")
#     n = n//10

# n = 128
# temp = n
# str1 = ""
# f1 = 0 
# while n!=0:
#     rem = n%10
#     check = temp % rem
#     if check ==0:
#         f1 = 1
#     n = n//10
#     if f1 == 0:
#         print("yes")
#     else:
#         print("no")

# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]
# l1=[1,2,3,4]
# l2=[5,6,7,8]
# # sum =(l1[0]+l2[0], l1[1]+l2[2])
# l3=[]
# for val in range(len(l1)):
#     ans = l1[val] + l2[val]
#     l3.append(ans)
# print(l3)

# ----> set
# charecterstics of set 
# 1.) set can becreated using{}
# 2.) The element inside set are not indexed
# 3.) Does not allow duplicate values
# 4.) it unordered
# 5.) heterogenous
# 6.) mutable or changable 

# eg:1
# s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
# print(s1)

# * Eg:2
#s2 = {5, 8, 98, [9, 0]}
#print(s2) ----> error


# Eg: 4
# min(), max(), len()

# * Eg:
# ? to add element inside set

#  s1 = {8, 78, 67, 'u'}
#add
#s1.add(43)
# print(s1)
# # eg
# ? to add element inside list

# s1 = {8, 78, 67, 'u'}
# s1.add(43)
# print(s1)


# # update()
# s1 = {8,6,7,3,546,'u'}
# s1.update([45,'i'])
# print(s1)

# discards(67)
# print(s1)
# eg
# ? to add element inside list
# s1 = {8, 78, 67, 'u'}
# s1.add(43)
# print(s1)

## update()
# s1 = {8,6,7,3,546,'u'}
# s1.update([45,'i'])
# print(s1)
# clear()

# l1 = {}
# print(type(l1)) 

# s1 = set() # --> to create empty set
# print(type(s1))

# s1 = {8,9,0}
# s1.clear()
# print(s1)

# s1 = {8,9,0}
# del s1
# print(s1)
# * join the sets
#s1 = {9, 0, 8}
#s2 = {9.90, "card", 't', 56}
# union() ---> to combine 2 sets
#s3 = s1.union(s2)
#print(s3)


# intersection()  ---> get common elements inside set
#s1 = { 4, 5, 6}
#s2 = {5, 6, 7, 8}
#print(s1.intersection(s2))

# * difference()
# s1 = { 4, 5, 6}
# s2 = {5, 6, 7, 8}
# print(s1.difference(s2))
# print(s1.difference(s1))
# print(s1.symmetric_difference(s2))

# isdisjoint(), issubset(), issuperset()
# s1 = {8, 9, 0}
# s2 = {7,5,8,9,0}
# print(s1.issubset(s2))
# print(s2.issuperset(s1))
# s1 = {1,2,3,4,5}
# s2 = {3,2,7,8,9}
# # n1 = {1,2,3}
# for val in s1:
#     if val in s2:
#     #     print("yes")
#     # else:
#     #     print("no")
#           str1 = "its joint set"
# print(str1)

# ------> dictionary
# eg 1
# d1 = {1:100, 'a':200, 4.5:"hello"}
# print(d1)
# print(len(d1))

# mech_name = ["name1", "name2", "name3"]
# mech_age = [23, 22, 24]
# mech_mark = [89, 79, 68]
# mech_email = ["name1@gmail", "name2@gmail", "name3@gmail" ]

# charecterstics of dictionary
# 1.) have to be surrounded by{}
# 2.) it have to be in the form of key, value pair
# 3.) it is mutable
# 4.) Duplicate keys are not allowed,
# 5.) Duplicate values are allowed
# 6.) It is unidexed
# 7.) It is ordered
# 8.) Key does nat allow mutable datatypes
# 9.) Values allow mutable datatypes

# d1={1:100,2:200,3:300,-4:400}
# #to access elements in dictionary
# print(d1)
# #or
#to access the values
# print(d1[-4])#---->o/p is 100

#some common functions
# #len(),min(),max()
# print(min(d1))
# print(max(d1))

#to find min,max based on values
# print(min(d1.values()))
# print(max(d1.values()))

# ?dictionary based functions
# to add element (key and value pair) in dict
# d1={1:100,2:200,3:300,-4:400}
# d1[5] = 500
# print(d1)

#? to replace a value in dictionary
# d1={1:100,2:200,3:300,4:400}
# d1[2]="mango"
# print(d1)

#? to delete a value in dictionary
# d1={1:100,2:200,3:300,4:400}
# d1.popitem()
# print(d1)

# d1={1:100,2:200,3:300,4:400}
#pop()
#d1.pop(2) # ---> 2 is the key in dictionary
#print(d1)

# clear(),del

# join 2 dictionary
#update()
#d1 = {1:100, 2:200, 3:300, 4:400}
#d2 = {"a":"apple", "b":"boy", "g":"game"}
#d1.update(d2)
#print(d1)

# get()------> used to get the value from a key
# d1 = {1:100, 2:200, 3:300, 4:400}
# print(d1[90])
# print(d1.get(90))
#to print the all the keys()
#print(d1.keys())
#print(type(d1.keys()))

# to print all the values
# print(d1.values)
# Iterating dictionary
# for val in d1:
# #     print(val)
# for key, val in d1.items():
#     print(key, val)

# ! problem- 1
#1.) swap elemwnts in string list
# The original list is :["Ggf", "best", "for", "geeks"]
# List after performing character swaps:]"efg",
# "bBgst", "for", "eGGks"]
# def reverse_string(string):
#     return string[::-1]
# string = ["Ggf"]
# reversed_string = reversed_string(string)
# print(string)
# def reverse_string(string):
#     return string[::-1]
# original_string = "hello"
# reversed_string = reverse_string(original_string)
# print(reversed_string)

# n=int(input("Enter of times:"))
# integer=[]
# float_value=[]
# string=[]
# for val in range(n):
#     value = eval(input("enter the values: "))
#     if type(value)==int:
#         integer.append(value)
#     elif type(value)==float:
#         float_value.append(value)
#     elif type(value)==str:
#         string.append(value)
#     else:
#         print("Pls provide data in int, float, string")
# print(integer)
# print(float_value)
# print(string)


# return a set of elements present in set A or B but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}

# str1 = {10, 20, 30, 40, 50}
# str2 = {30, 40, 50, 60, 70}
# sub =(str1[0]-str2[0],str1[1]-str2[2])
# str3=[]
# for val in range(len(str1)):
#     ans = str1[val] + str2[val]
#     str3.append(ans)
# print(str3)
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# l1=set1 ^ set2
# print(l1)
# n = int(input("Enter num of times : "))
# integer=[]
# float_value=[]
# string=[]
# for val in range(n):
#     value = eval(input("Enter the values : "))
#     if type(value)==int:
#         integer.append(value)
#     elif type(value)==float:
#         float_val.append(value)
#     elif type(value)==str:
#         string.append(value)
#     else:
#         print("Pls provide data in int, float, string")
# print(integer)
# print(float_value)
# print(string)

# 1.) Swap elements in String list
# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps : ['efg', 'is', 'bGst',
# 'for', 'eGGks']
# l1=[1,2,3,4] # key
# l2=["a","b","c","d"]  # value
# l3=(l1[0]=l2[0] l1[1],l2[1] or l1[2],l2[2]or l1[3],l2[3])
# print(l3)

