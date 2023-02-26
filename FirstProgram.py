"""

#Variable Declaration :
#Ex1:
print('Hellow World')
age = 20
print(age)

#Ex2: Different data type variable declarition
#Note : Boolean value starts with Capital letter
name = "Adity Bhowmik"
age = 28
IsNew = False
print(name,age,IsNew)

#Taking input from user as string (default datatype) and put it in the variable
name = input("What is your name? ")
print("Hellow " + name)

#Type cast needed while taking input from user when input values are other than string
#As Python considers all the input from user as string
birth_year = input ("What is your birth year : ")
current_year = 2022
print("Your age is : ",current_year - int(birth_year))

#Basic Calculator:
First = float (input ("Enter First Number : "))
Second = float (input ("Enter Second Number : "))
print ("Sum : ",First + Second)
print ("Substraction : ",First - Second)
print ("Divide : ",First / Second)
print ("Multiply : ",First * Second)

#String data type
course = " Python for Beginner"
print(course.upper())
print(course.lower())
print(course.find('y')) #Find string location
print(course.find('Y')) #Python is case sensetive so need to be careful with caps/small letter
print(course.find('on')) #Find the start of the char index
print(course.replace('for','7'))
print('Python' in course) #in operator results boolean value

#Python Operator
print(2+2)
print(2-2)
print(2*2)
print(2**6) #Represents power of 2^6
print(10/3)
print(10//3) #Only takes the value before decimal
print(20%3)

#Augmented Assignment Operators :  +=, -=, *=, /=, //=, **=, |=, &=, >>=, <<=, %= and ^=
a=10
a = a+10
print(a)
a=10
a += 10
print(a)

#Comparison Operators

a = 21
b = 10
c = 0

if ( a == b ):
   print ("Line 1 - a is equal to b")
else:
   print ("Line 1 - a is not equal to b")

if ( a != b ):
   print ("Line 2 - a is not equal to b")
else:
   print ("Line 2 - a is equal to b")

if ( a < b ):
   print ("Line 4 - a is less than b")
else:
   print ("Line 4 - a is not less than b")

if ( a > b ):
   print ("Line 5 - a is greater than b")
else:
   print ("Line 5 - a is not greater than b")

a = 5;
b = 20;
if ( a <= b ):
   print ("Line 6 - a is either less than or equal to  b")
else:
   print ("Line 6 - a is neither less than nor equal to  b")

if ( b >= a ):
   print ("Line 7 - b is either greater than  or equal to b")
else:
   print ("Line 7 - b is neither greater than  nor equal to b")

# logical and operator

a = 10
b = 10
c = -10

if a > 0 and b > 0:
   print("The numbers are greater than 0")

if a > 0 and b > 0 and c > 0:
   print("The numbers are greater than 0")
else:
   print("Atleast one number is not greater than 0")

#Exercise 1 : Reverse a string :
val = input ("Please enter the sting : ")
print("Reverse : ",val[::-1])

#Exercise 2 : Weight conversion
weight = float(input("Please enter your weight : "))
type =  input("(K)g or (L)bs : ")
if ( type.upper() == 'K' ):
    print("Weight in Kg : " , round(weight/0.45,2))
elif (type.upper() == 'L'):                         #else - if
    print("Weight in Kg : ", round(weight * 0.45,2))
else:
    print("Not a valid input")


# While loop :
#Ex 1 :
i = 1
n = 5
while (i <= n):
    print(i)
    i+=1

#Ex 2 :
i = 1
n = 5
while (i <= n):
    print(i * '*')
    i+=1


#List :
a = ['Adity','Saikat','Mum','Tatai']
print (a)
a[0] = 'Aditi'
print (a)       #Print all
print(a[0:3])   #Location 0 ,1,2,3
print(a[::-1])  #Reverse

# List operations :
a = ['Adity','Saikat','Mum','Tatai']
a.append('Souvik') #Added at the end
print (a)
a.insert(2,'Atanu') #Insert in the mentioned location
print (a)
a.reverse()         #Reverse the list
print (a)
#a.reverse()
print (a[-1])       #Prints the last eliment
a.clear()
print(a)

number = [1,2,3,4,5]
print(1 in number)
print (10 in number)
print (len(number))

#For loop
number = [1,2,3,4,5]
for item in number:
    print (item)    #Print the items into separate lines

i=0
#Same with while loop
while (i<len(number)):
    print(number[i])
    i=i+1
"""
#Range
#Ex1 :
num = range (1,10)
for item in num:
    print(item)

num1 = range (1,10,2)
for item in num1:
    print(item)
print("Hello world")
#Tuple : They are same as list but the vaalues are not changable :also we use '()' to replresent tuple