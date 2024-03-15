# ? ----> common function for list 
# l1 = [6,7,8,9,0]
# print(len(l1))
# print(max(l1)) # ----> eroe cause its a combination of list and string
# print(min(l1)) # ----> error cause its a combination of list and string

# l1 = [6,7,8,9,0]
# print(len(l1))

# l1 = [6,7,8,9,0,8.89, -5, 0.16]
# # index()----> to get the index value of specific element
# print(l1.index(9))

# l1 = [6,7,8,9, 8,0,8.89, -5, 0.16]
# count()---> how many no of times an element is printed
# print(l1.count(8))

# some function which is specifically used for list
# to add element inside list 
# insert ()-----> to add element at specific index position
# l1 = [6,7,8,9,0,8.89, -5, 0.16] 
# l1.insert (7, "cars")
# print(l1)
# pop (index_value) ----> used to delete element at specific index
# l1.pop(4) # 4 is index value
# print(l1)

# remove(element) ----> used to delete element directly
# l1.remove(8.89)
# print(l1)

# l1.clear(7)
# print(l1)

# del.l1
# print(l1)

# l1 = [1,2,3,4]
# l2 = [1,2,3,4]
# print(l1+l2)

# or
# extend( ---> to combine 2 lists)
# l1.extend(l2)
# print(l1)

# ? -------> copy ()
# l1 =[6,7,8,9]
# l2 = l1.copy()
# print(l2)

# print(id(l1))
# print(id(l2))

# ! difference between shallow copy and deep copy
# shallow copy
# import copy
# l1 = [8,9,0,[5, 6], [3,2,1]]
# print(l1[-1][1])
# l2=copy.copy(l1)
# l1.append("cars")
# print(l1)
# print(l2)

# SORT 
# it is used to ASSENDING OR DESENDING ORDER 
# l1 = [1,3,3,2,4]
# l1.sort()
# print(l1)
# l1.sort(reverse=True)
# print(l1)

# l1 = ['z', 'i', 'o', 'p', '9']
# l1.sort()
# print(l1)
# ? list constructor
# * list() ---> to cover other collectiuon datatype to list


# l1 = [8,9,[0,8,7],["p", "o", "y"], [8, "t"]]
# print(l1[1 :4])
# print(l1[1 :1 ])

# ? to delete "t" from l1

# l1 = [8,9,[0,8,7],["p", "o", "y"], [8, "t"]]
# l1[-1].remove("t")
# print(l1)

# combine these 2 list in_["p", "o", "y"],[8, "t"] list in l1 ["p", "o", "y", 8, "t"]
# l1 = [8, "t"],["p", "o", "y"]
# l2 = copy
# print(l1+l2)

#   -----> touple
# 1.) tuple have to be surrounded by ()
# 2.) The element inside tuple are not changable
# 3.) The element inside tuple are indexed
# 4.) The element will excuted in order
# 5.) It is heterogenous
# 6.) It allow duplicate element

# eg 
# t1 = (8, 8, 9, 6, 5.78, [9,0], (6,8), "hey", (9+6))
# print(t1)
# print(type(t1))

# i1 = [8]
# print(type(i1))
# i1 = [8]
# print(type(i1)) # touple

# t1 = 8
# print(type(t1))


# t2 = 8
# print(type(t2))

# len(), min(), max(), index(), count() ----> all same as list

# to add element inside touple ---> cannot add
# cannot delete any element from touple

# join 2 touples
# my_tuple = ("a", "b")
# my_tuple2 = ("c", "d")
# print(my_tuple + my_tuple2)

# l1 = [6,7,8,9,0]
# print(sum(l1))

# * sort tuple
#t1 = (8, 9,0, 89, 12)
#print(tuple(sorted(t1)))
#print(tuple(sorted(t1, reverse=True)))

# * Iterate list and tuples

# l1 = [9, 8, 0, 6, 5]
# for i in l1:
#     print(i)
    
# Iterate based on index value

# l1=[9,8,0,6,5,7,36,54,55,6,43,5,66]
# for i in range(0,len(l1)):
#     print(l1[i])
#-----> strings
 
# s1 = " helo (world")
# #  # to access string 
 
# print(s1)
# # indexing and  slicing ---> same as list and tuple
 
# print(s1[0 : 5])

# --->common functions
# len(), sin(), max(), index(), count()
# s1 = (" helo world")
# print(len(s1))
# print(max(s1))
# print(min(s1))

# ord() ---> used to find the  ASCII value  of a charecter 
# s1 = "u"
# print = (ord(s1)) 
#strip()--->to eliminate the space in beginning and end of string
# s1=" where are you"
# print(s1.lstrip())
 
 
# ? split function()---.
# s1 = "where are you? "
# print(s1.split("e"))
# # print(s1.split(""))
# print(s1.count("e"))

# s1 = "where are you? "
# print(s1.split("e"))
# print(s1.count("e"))
# replace() --> to replace a specific char in the string
# replace
# # print(s1.replace("r", '&&'))


# swapace() --> to convert capital to small and small to capital at a time
# swape case
# s1 = "HEY there"
# print(s1.swapcase())

# title function()
# s1 = "HEY there"
# print(s1.title())

# capitalize() 
# s1 = "HEY there"
# print(s1.capitalize())
# join the strings
# s1 = "hello"
# s2 = " world "
# print(s1+s2)
#  s1= 'hey dont sleep there'
# i = 7
# find
# s1 = (" helo world")
# print(s1,find('z'))

# join function ()
# from multiprocessing.dummy import JoinableQueue


# l1 = ["hey", "there"]
# print(" ".join(l1))
# print(" $ ".join(l1))

# s1 = "welcome to all"
# print(s1.endswith('l'))
# print(s1.startswith('w'))


# print the function string in revesre
# s1 = "welcome to all"
# print(s1[::-1])

# ! =====> eg 1:
# wap to find the number of lower case letters
# s1 = " HEY there you aRE"
# count = 0
# for i in s1:
#     if i.islower():
#         count+=1
#     print("the total num of lower case letters: ",count)


# ! ----> eg:2
# s1 = 'restarter'
# s1 = "IMAGINE"
# fst = s1[0]
# bal = s1[1:]
# txt = bal.replace(fst,"$")
# print(fst+txt )

# str1 = "bbbbbyyybbbaaioo"
# str2 = "%"


# Lorem Ipsum is simply dummy text
# of the printing and typesetting industry.
# Lorem Ipsum has been the industry's standard 
# dummy text ever since the 1500s, when an
# unknown printer took a galley of type and 
# scrambled it to make a type specimen book. 
# It has survived not only five centuries, 
# but also the leap into electronic typesetting, 
# remaining essentially unchanged.
# It was popularised in the 1960s with 
# the release of Letraset sheets 
# containing Lorem Ipsum passages, and more recently
# with desktop publishing software like 
# Aldus PageMaker including versions of Lorem Ipsum.

s1 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# count = 0
# for i in s1:
#     if i in range():
#         count+=1
#     print("the total num of case letters: ",count)
charecters = len(s1)
print(charecters)

words = s1.split(" ")
print(len(words))

sentences = s1.split('.')
for val in sentences:
    if val =='':
        index = sentences.index('')
        sentences.pop(index)
print(len(sentences))

space = 0 
for val in s1 :
      