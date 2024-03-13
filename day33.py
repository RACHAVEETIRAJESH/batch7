# # ! eg:3
# # ? take the value of the length and breadth of a 
# # ?  from the user check if it is a square or not

# # length = int(input("enter the value of length:"))
# # breadth = int(input("enter the value of breadth :"))
# # if length == breadth :
# #  print("it is a square")
# # else:
# #  print("it is not a square")
 
#  # ! eg 4
#  # python program to check wether the 
#  # given integer is a multiple of both 5 and 7 
 
# # n = int(input("enter the number :"))
# # if n%5==0 and n%7==0 :
# #        print("yes")
# # else :
# #        print("no")

# # eg :5
# # write a program to accept the cost price of a bike and 
# # display the road tax to be paid
# # according to the following
# # cost price(in rs)                       tax
# #  >100000                                15 % + discount 6%
# #  <100000                                 5 % 

# # price = int(input("enter the price:"))
# # amount = 0
# # if price >= 100000:
# #       discount = price*(6/100)
# #       value = price-discount
# #       amount = value*(15/100)
# #       total =  value + tax
# # else:
# #       tax = price*(5/100)
# #       total =  price + tax
# # print("the on road cost of bike is :",total)

# # if elif 
# # a = 7
# # b= 9
# # c=30
# # if a>b and a>c:
# #       print("a is greater :")
# # elif b>a and b>c:
# #       print("b is greater :")
# # elif c>a and c>b:
# #       print("c is greater :")
# # a school has following rules for grading system:
# # a. Below 25 - F
# # b. 25 to 45 - E
# # c. 45 to 50 - D
# # d. 50 to 60 - C
# # e. 60 to 80 - B
# # f. Above 80 - A
# # Ask user to enter marks and print the corresponding grade.

# # mark = int(input("enter the mark:"))
# # if mark>=80 and mark<= 100:
# #       print("a")     
# # elif mark>=60 and mark<= 80:
# #       print("b")    
# # elif mark>=50 and mark<= 60:
# #       print("c") 
# # elif mark>=40 and mark<= 50:
# #       print("d") 
# # else:
# #       print("fail")

# # ! -----> short hand side 
# # 
# # a = 9
# # b = 60
# # if a>b:
# # print("a")
# # else:
# # print("b")
# # rules
# # 1.) statement inside if condition have to present at first
# # 2.)elif cannot be used in short hand side f else
# # 3.)always it have to end with else

# # print("a") if a>b else print ("b")

#  char = str(input("enter the  charecter:"))
# # if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" :
# #       print("is a vowel")
# # else:
# #       print("it is a conosonent")
# # ? or

# # str1 = "aeiouAEIOU"
# # if char in str1:
# #       print("vowel")
# # else:
# #       print("conosoent")

# # using shorthand if else
# char = input("enter the char:")
# str1 = "aeiouAEIOU"
# print("vowels") if char str1 else print("consonent")
# ! ------> elif ladder using short hand side if else
# eg 1
# find the greatest among 3 variables using the short hand side if else


# a=8
# b=5
# c=9
# print("a is greater") if a>b and a>c else print("b is greater")
# if b>a and b>c else print("c is greater")

#  !-----> looping
# looping can be implemented Usering 
# for Loop r or 
# while loop
# !------> for Loop
# ? for loop is used for iteration, if we know the number of times the loop have to run
# ? it is used to iterate the iterates eg( string, list, tuple, etc...)

# for syntax in python
# for userundifined_variable in range(start, end, step): default step value is 1
# statement
# statement
# statement

# ? eg 1:
# to print the value from 1 to 10 using for loop

# for i in range (0, 10): #(n, n-1)
#     print(i)
# for i in range (0, 10): #(n, n-1)
#     print("hello")
# ! eg:2
# for val in range (23, 50, 3):
#     print(val)
# for val in range (1, 50, 3):
#     print(val)
# ? eg :3
# to decrement the value

# for val in range(10, 0, -2):
#     print(val)
# ! print the output of 7th multiplication table from 21 to 43
# for val in range(21, 43+1): 
#     print(val*7) 
# for val in range(1, 10+1):
#     print(f"7 * {val}={val*7}")
# print('7','*',val,'=',val*7) method 1
# ans="7 x {} = {}"
#  print(ans.format(val,val*7)) method 2
# for val in range(1, 10+1):
#     print(f"7 * {val}={val*7}")method 3

# break
# eg 5:
# for val in range(1,25):
#     print(val)
#     if val ==6:
#         break  
# # eg 5:
# for val in range(1,25):
#     if val ==6:
#         break
#     print(val)

# ! continue
# for val in range(1,25):
#     if val ==6:
#         continue
#     print(val)

# ! practise problems
# ? print the even number between 20 to 40
# for val in range(20, 40, 2):
#      print(val-1)
# for val in range(20, 40, 2):
#     if val%2==0:
#         print(val)
# ! ----> while loop 
# ? while is used when we do not know the number of times the loop have to run
# ? to iterate the non iterable elements while loop is used
# intialisation
# while condition
# statement 
# increment or decrement

# ! eg 1
# to iterate number from 1 to 10
# i =0
# while i<11:
#     print(i)

# for loop prcatise
# write a program to display sum of odd numbers and even
# numbers that fall between
# 12 and 37 (including both numbers)
# for val in range (12, 37+1):
#     print(val)
# i=0
# while i<11:
#     print(i)
#     i=i+1

# i=10
# while :
#     print(i)
#     i=-1
# ! ------> 1+