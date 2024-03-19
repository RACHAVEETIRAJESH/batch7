#Positional args
#keyword args
#default args
#variable length args
# keyword variable length args


# Positional args
# ? the position of parameter have to be same as positions
# as arguments

# def profile(name,phone,mark):
#     txt="My name is{}. My phone number{}. I got{} marks{}."
#     print(txt.format(name,phone,mark)) 
# profile(96668686,"raj",100) #unexpected

#EG2
# # keyword args
# def profile(name, phone, mark):
#     txt="My name is{}. My phone number{}. I got{} marks{}."
#     print(txt.format(name,phone,mark))  
    
    
# profile(name="raj", phone= 8919211190,  mark=90)
# profile("raj", phone= 8919211190,  mark=90)

# * todo --> Exception of keyword args function
# def profile(name, phone, mark):
#     txt="My name is{}. My phone number{}. I got{} marks{}."
#     print(txt.format(name,phone,mark))

# profile(name = "# `shashank` is being passed as an argument to the `name` parameter in the `profile`
# function. The function `profile` then uses this argument to display the name in
# the output message.
# shashank", mark=99, phone=9876543210) # Error
# profile(9876543210,name= "shashank", mark=99) # error
# profile("shashank",mark=98,phone=9876543210)

# * default args
# ! eg:1
# def profile(name, phone, place="kadapa"):
#     txt = "my name is {}. my phone number is {}. i am from {}."
#     print(txt.format(name, phone, place))
    
# profile("sid", 8989898989, "guntur")

# eg:2
# def profile(name, phone, place="kadapa"):
#     txt = "my name is {}. my phone number is {}. i am from {}."
#     print(txt.format(name, phone, place))
    
# exception 
# profile (name, place="kadapa", phone)
# if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
#     txt="My name is{}. My phone number{}. I got{} marks{}."
#     print(txt.format(name,phone,place))
# else:
#     print("You are not eligible to Signup")
# file("Shashank",9876543210) 

# variable length params
# # * eg: 1
# def profile(name):
#     print("my name is",name)
# profile("raj", 'name2', 'name3')  

# variable length params
# # * eg: 1
# def profile(name):
#     print("my name is",name)
# profile("raj", 'name2', 'name3')
# name = "sid", "name1", "name2"
#     for val in name:
#         print("my name is", val)
# profile("raj", 'name2', 'name3')
# EG : 2
# def profile(*name, age):
#     for val in name:
#         print("my name is", val, "my age is", age)
# profile("raj",'name2', 'name3', 28)

# def profile(age, *name):
#     for val in name:
#         print("my name is", val, "my age is", age)
# profile(28, "raj",'name2', 'name3')
# 
# 
# ! eg:1
# def price(price_list):
#     price(price_list)

#print()

# d1 = {"a":100, "b":200, "c":300}
# d1 = dict(a=100, b=200, c=300)
# print(d1)



# def price(**price_list):
#     print(price_list)
    
# price(shirt=1000, iphone=80000)

# n = 5
# {1:1, 2:4, 3:9, 4:16, 5:25}
# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}def generate_squared_dictionary(n):
# squared_dict = {}
# for x in range(1, n+1):
#     squared_dict[x] = x*x
# return squared_dict

# n = 5
# result_dict = generate_squared_dictionary(n)
# print("Sample Dictionary (n = {}):".format(n))
# print("Expected Output:", result_dict)

# def generate_squared_dictionary(n):
#     squared_dict = {}
#     for x in range(1, n+1):
#         squared_dict[x] = x*x
#     return squared_dict

# # Example usage with n = 5
# n = 5
# result_dict = generate_squared_dictionary(n)
# print("Sample Dictionary (n = {}):".format(n))
# print("Expected Output:", result_dict)

# n = int(input("enter the number: "))
# d1 = {}
# for val in range(1, n+1):
#     d1[val] = val**2
# print(d1)

# def rajesh():
#     d1 = {}
#     for val in range(1, n+1):
#         d1[val] = val**2
#     print(d1)
# Rajesh(5)
# ----> object oriented programming
# the paradigms of objects oriented programming are
# class
# objects
#inheritance
#polymorphism
#abstraction
# encapsulation

# ! class is a blue print of an object
# l1 = [1,2,3,4,5,6]

# ? eg:1
# class c1:
#     name1 = 'sidhu'
#     print(name1) 

# ? eg:2
# class person:
#     name = "sidhu"
#     print(name1) 

# c=person() # c.os object
# the process of creation of an object is called as instalation
# print(c.name())

# ? eg:3
# create a method
# when the function is created with a mrthod is called as method
# method without parameter
# class person:
#     def display(person):# it is a method
#         print("hello welcome to classes")  
# The code `# p = person()` creates an instance of the `person` class and assigns it to the variable
# `p`. However, the line `# p.display()` is commented out, so it does not have any effect on the
# program execution. If you uncomment this line, it would call the `display` method of the `person`
# class using the instance `p`.
# p = person()
# p.display()

# eg:4
# ! method with parameter
# class person:
#     def display(person,name,age):
#         print(name,age)
# p = person()
# p.display("raj", 28)

# ! eg:5
# class person:
#     name = "RAJESH" # atribute or variable
#     lname = "RACHAVEETI"
#     def display(person):
#         print(person.name)
        
        
#     def display_name(person):
#         print(person.name+" "+person.lname)
# p = person()
# p.display()
# p.display_name()

# eg :6
# constructer
# 
# ---> __int__{}
# class profile:
#     def d1(self): # constructor method 
#         print("hey")
    
# p = profile() # through this process
# p.d1()

# def fibonacci(n):
#     fib_sequence = [0, 1]  # Start with the first two Fibonacci numbers
#     for i in range(2, n):
#         next_fib = fib_sequence[-1] + fib_sequence[-2]  # Calculate the next Fibonacci number
#         fib_sequence.append(next_fib)  # Add it to the sequence
#     return fib_sequence

# n = 8
# fibonacci_sequence = fibonacci(n)
# print("Fibonacci sequence up to the {}th term:".format(n))
# print(fibonacci_sequence)
