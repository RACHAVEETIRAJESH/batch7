# num = 8
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print("Factorial of", num, "is:", factorial)

# def catAndMouse(x, y, z):
#     dist_cat_a = abs(z - x)
#     dist_cat_b = abs(z - y)
#     if dist_cat_a == dist_cat_b:
#         return "Mouse C"
#     elif dist_cat_a < dist_cat_b:
#         return "Cat A"
#     else:
#         return "Cat B"
#     print(catAndMouse(1, 2, 3))  # Output: Cat B
# -----> while Loop
# 1.) iterate from 20 to 30 and break the loop in 27
# i=0
# while i<11:
#     print(i)
#     i=i+1

# i=10
# while :
#     print(i)
#     i=-1
# ! ------> 1+

#22222
# i=20
# while i<31:
#     if i==27:
#         break
#     print(i)
#     i+=1
#33333
# i = 20
# while i<31:
#     print(i)
#     if i == 27:
#         break
#     i+=1

#44444

# i = 20
# while i<31:
#     if i == 27:
#         print(i)
#         break
#     i+=1

#-----> continue
#----> eg 1
# i=20
# while i<31:
#     if i == 27:
#         i += 1
#         continue
#     print(i)
#     i+=1
 
# number = 20
# while number <= 31:
#     if number == 27:
#         number += 1
#         continue
#     print(number)
#     number += 1
# eg 5:
# while to iterate from 12 to 22
# and find the sum of all numbers
# i = 12
# sum = 0
# while i<22:
#     i+=1
#     sum=sum+i
# print(sum)
# eg 6
#find the average of the value from 20 to 25
# i = 20
# sum = 0
# while i<25:
#     i+=1
#     sum=sum+i
# avg=sum/5
# print(avg)
# eg 7
# i = 20
# sum = 0
# count = 0
# while i<25:
#     sum=sum+i
#     count+=1
#     i+=1
# print(sum/count)

#-----> nested if loop
#eg 1 
# for i in range(1,3+1):
#     for j in range(1,4+1):
#         print(i,j)

# eg 22
# * * * * 
# * * * * 
# * * * * 
# * * * * 
# for row in range (4):
#     for col in range(4):
#         print("*",end=" ")
#     print()

# for row in range(8):
#     for col in range(8):
#         print("row", end=" ")
#     print()

# sum = 0
# for row in range(8):
#     for col in range(8):
#         sum= sum +1
#         print("sum", end=" ")
#     print()
# for row in range(0,6):
#     for col in range(0,row+1):
#         print("*", end=" ")
#     print()
# 3 to print
# * * * * * * 
# * * * * * 
# * * * *   
# * * *     
# * *
# *
# for row in range(0,6):
#     for col in range(row, 6):
#         print("*", end=" ")
#     print()

# * * * * *
# *       *
# *       *
# *       *
# * * * * *
# for row in range(5):
#     for col in range(5):
#         if col==0 or col==5-1 or row==0 or row==5-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#      *
#     * *
#    * * *
#   * * * *
# for row in range(0, 5):
#     for col in range(0, 6):
#  if((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# for row in range(0, 5):
#     for col in range (0, 6):
#         if((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# for row in range(0,4):
#     for col in range(0,4):
#         if((row==0 and col==0) or (row==0 and col==1) or (row==0 and col==2) or (row==0 and col==3) or (row==0 and col==4)):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# ----> list
# -----> datatypes
# primary
#  number
#  string
#  boolean
#  none
 
#  collection
#  list
#  tuple
#  set

# ? ---> list 
# 1. if the collection of elements are surrounded by a square bracket, it is considerd 
# 2. be as a list
# eg:1
#  l1=[4,5,6,7,8,9,0] 

# charecterstics of list
# 1. list have surrounded by []
# 2. it is mutable(the elements in the list are changable)
# 3. every element inside list is index
# 4 the element inside list be in ordered format
# 5.it can hold duplicate values
# its heterogenous

# to acess the element in list
# l1=[1,2,3,4,5,6,7,8,9,0]
# print(l1)

#  ? ----> Indexing
# In the collection datatypes like list, tuple, string, the elements will be alloted with predefines unique value called index value

# We have 2 types of indexing
# Positive indexing ---> starts with 0 from left hand side
# Negative indexing ---> starts with -1 from right hand side

# --> Positive indexing
#lst-1 = [1,4,1,89,7.5,"p","i"]
# print(1st1[0])
# print(1st1[4])
# print(1st11[20]) --> error
# ---->Negative indexing
#lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
#print(lst1[-1])
#print(lst1[-5])

# ? ------> slicing
# lst1=[1, 4, 1, 7, 89.7, 75, "p", "i"]
# lst1[start_index:end_index:step]
# print(lst1[0:4])
# print(lst1[6:8])
# print(lst1[3:6])
# print(lst1[:4])
# print(lst1[:4])
# print(lst1[4:])
# print(lst1[0:7:2])
# print(lst1[:])

# trail = int(input())

# lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
# print(lst1[-4:-1])
# print(lst1[-1:-4])
# print(lst1[-7:-1])
# print(lst1[-7:-1:2])

# ! to insert to add the element inside list

# append() --> used to add element at last position of list
# l1 = [9,8,0,6]
# l1.append("car")
# print("l1") 
lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
n = int(input("enter the number of inputs:"))
for i in range(0, n):
    a, b = list(map(int, input().split()))
    print(a,b)