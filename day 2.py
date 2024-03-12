a= 7,8
print(a)
print(type(a))

a,b=c=7,8
print(a)
print(b)
print(c)

a=b,c=7,8
print(a)
print(b)
print(c)


a=7
b=5

temp=a
a=b
b=temp
print(a,b)

a,b=b,a
print(a,b)

a=a*b
b=a/b
a=a/b
print(int(a),int(b))


# to find the address of memory
print(id(a))
print(id(b))

#----->keywords
import keyword
print(keyword.kwlist)

print(type(keyword.kwlist))


# to check the string is keyword or not
print(keyword.iskeyword("sid")) #false


print(keyword.iskeyword("except")) #false

# ! ----> literals
#literal is the constant value assigned to a variable
# a variable is consonant to be constant when it is ddefines
# in caps

a=78 # a is variable 
A=78 # A is constant

# hash() ---->it creates a hash value for constant datatypes and
# provides error for non constant datatypes
n1 = 89+7j
print(hash(n1))
f1 = [7,8,9]
print(hash(f1)) #error ---> list is non - constant or mutual datatype

a=9
b=9
b=90
print(id(a))
print(id(b))
#!------> operators
# operators are symbols which is used to perform various operations
# between 2 or more operands
arithematic
logical
relational or comparison
bitwise
identity
membership

# * ------> arithematic---> +,-,*,/,%,//,**
eg:1
a=8
b=6
c=9
print(a+b+c)

# input() ----> used to get the run time input
# eval()---> used to get the runtime values of all datatype


n1= int(input("enter the value: "))
print( type (n1))

a=2
b=2
print(a/b) # is used to get the quotient value
print(a%b) # is used to get the remainder value


# ! // ----> floor division

a = 765433
b = 19
# print(a/b) # -> the output will be in integer & the output will be
# based on thy floor

# ! **-- > used for the power of  number
print(2**4) # --> 16

# ! assignment
a=8
a+=2
print(a)

a=30
a-=5
print(a)

a=8
a+=2
print(a>b)

a=8
a+=2
print(a<b)

a+=8
a=8
print(a==a)

# ~ --->
a=9876
print(~a)
# << ,>>
print(5<<3)
print(5<<3)
16>4

# ! logical operator
# and ,or, not
a = 6
#  print (a>3 and a<10)
#  print(a>7 and a<30)
print(not(a>7 and a<30))

# ! identity operator
# is , is not
# ? it is used to compare the memory location
# ? are stored
a = 6
b = 3

print(a is b)

print(a == b)
print(a)

a = [1 , 2, 3]
b = [1 , 2, 3]
print(a is b)
print(a == b)

# ! membership operator
# in, not in

l1=[7,8,9,0,6,5]
num=55
print(num in l1)
print(num not in l1)

num= 678
print(8 in num)


# ! conditional statement



#----> C syntax
if (condition):{
       statement:
       statement
       statement:
}
   python syntax
      if condition
        statement
        statement
        statement


# eg :1
a=6
if a:
    print("hello")

#eg 2
a=6
if a>3:
    print("hey")
else
    print("no")
    

# if a number is even or odd
n = int(input("enter the number:"))
if n%2==0:
    print(n, " is even")
    else:
       print(n, " is odd")  



# name, age, nationality
n = int(input("enter the age:"))
m = str(input("enter the name:"))
l = str(input("enter the nationality:"))
print(n, "age")
print(m,"name")
print(l,"nationality")


# 

n = int(input("enter the age:"))
m = str(input("enter the name:"))
l = str(input("enter the nationality:"))
if age >18 and nationality == "indian":
print("eligible for vote")
else:
    print("not eligible")
























