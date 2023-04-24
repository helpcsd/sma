

#write a program to display prime numbers between 50 and 100

for i in range(50,101):
  if i>1:
    for n in range(2,i):
      if(i%n==0):
        break;
    else:
      print(i)

#find all the positive integer whose square is less than 100

i=1
while(i*i<100):
 print(i)
 i+=1

#demonstrate PASS statement

a=10
b=20
if(a>b):
  pass
else:
  print("a<b")

#DEFINE A FUNCTION TO DISPLAY THE FIBONNACI NUMBERS UNTIL THE GIVEN 'N'

def fib(n):
 if(n<0):
   print("Not valid")
 if(n==0):
   return 0
 if(n==1 or n==2):
   return 1
 else:
   return fib(n-1)+fib(n-2)


print("Enter the value of n")
n=int(input())
print("Fibonnaci series of n is :",fib(n))

#define a list with a hetrogeneous data

l=[1,'xyz',3]
print(l)

#define a code to distant append and extend function

l.append('a')
l.append(2)
print(l)

l.extend('b')
print(l)

#define a dictionary and list only the keys of the dictionary
a=[]
d={'x':1,'y':2,'z':3}
for i in d:
  a.append(i)
print(a)

#define a dic where each key will have multiple values

dic={'a':[2,5],'b':['xyz','abc']}
print(dic)

#define a set with a duplicate value
s={1,2,3,1,4}
s

s1={'a','b','c'}
s1

#apply set operations

#union
s|s1

#intersection
s&s1

#difference
s-s1

u={1, 2, 3, 4, 'a', 'b', 'c'}

#negation 
u-s

#define a variable 'a' as 10 and 'b' as HELLO then display the output of (a+b)
a=10
b='hello'
print(a,'+',b)

#find the smallest and largest number from the list,read list from user

print('Enter the size of list:')
n=int(input())
l=list()
print("Enter the elements of List(l)")
for i in range(n):
  x=input()
  l.append(x)
print("Minimum element of list(L):")
print(min(l))
print("Maximum element of list(L):")
print(max(l))

#split a list in half and store the elements in 2 diff list

ls=[1,2,3,4,'a','b','c','d']
l1=list()
l2=list()

x=len(ls)//2
x

l1=ls[:x]
l2=ls[x:]
print(l1)
print(l2)

#remove multiple empty strings from a list of strings

l3=['a','b','c','','d','e','']
print(l3)
while('' in l3):
  l3.remove('')
print(l3)

#interchange first and last element of the list
'''temp=list()
temp=ls[0]
ls[0]=ls[len(ls)-1]
ls[len(ls)-1]=temp
print(ls)'''
ls=[1,2,3,4,'a','b','c','d']
ls[0],ls[len(ls)-1]=ls[len(ls)-1],ls[0]
print(ls)

#print the elements with frequency greater than a given value K

l4=[1,1,1,2,3,4,5,5,5,6]
l5=list()
print("Set the maximum frequency:")
x=int(input())
for i in l4:
  if(l4.count(i)>x and i not in l5):
    l5.append(i)
l5

#define a function which adds and multiplies all the elements of the list separately and return both of them

def op(l):
 sum=0
 mul=1
 for i in l:
   sum=sum+i
   mul=mul*i
 return sum,mul

l=[1,2,3,4,5]
x=op(l)
print(x)

#write a function to create a list ranging from [4,20] incremented by 3

def create():
  l=list()
  for i in range(4,20,3):
    l.append(i)
  return l

print(create())

#write a function to return all the months which have 31 days

def month(m):
 l=list()
 for i in m:
   if(m[i]==31):
      l.append(i)
 return l

m={'jan':31,'feb':28,'mar':31,'apr':30,'may':31,'june':30,'july':31,'aug':31,'sep':30,'oct':31,'nov':30,'dec':31}
print(month(m))

#create a function to enumerate a list of 5 names with count starting from 3 and returns a list of tuples

def fun(lis):
  return list(enumerate(lis,6))


lis=['a','b','c','d','e']
print(fun(lis))

# Python Program to Find LCM

def lcm(a,b):
  if(a>b):
    greater=a
  else:
    greater=b
  while(True):
    if(greater%a==0 and greater%b==0):
      lcm= greater
      break
    greater+=1
  return lcm  

x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
lcm(x,y)

#Python Program to Find HCF

def hcf(a,b):
 if(a==b | b==0 ):
   return a
 if(a==0):
   return b
 if(a>b):
   return hcf(a-b,b)
 else:
   return hcf(a,b-a)
x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
print('The HCF of',x,'and',y,'is:',hcf(x,y))

'''def bin(a):
 b=list()
 while(a!=1):
   rem=a % 2
   a=a/2
   b.append(rem)
 print(b)
 return b


n=int(input("Enter the decimal number:"))
print("Binary number is:",reversed(bin(n)))'''

#convert decimal to binary

n=int(input('Enter the number:'))
print("Binary conversion of",n,'is',bin(n))

#convert decimal to octal

a=int(input('Enter the number:'))
print("Octal conversion of",a,'is',oct(a))

#convert decimal to hexadecimal

b=int(input('Enter the number:'))
print("Octal conversion of",b,'is',hex(a))

#ascii value

c=input('Enter the character: ')
c_ascii=ord(c)
print('ASCII value of',c,'is',c_ascii)

#Python Program to Make a Simple Calculator

def calci(key):
  a=int(input('Enter the first number:'))
  b=int(input('Enter the second number:'))
  if(key==1):
    print('Addition:',a+b)
  elif(key==2):
    print('Substraction:',a-b)
  elif(key==3):
    print('Multiplication:',a*b)
  elif(key==4):
    print('Division:',a/b)
  else:
    print('Invalid operation, Try Again!')

print('Enter the key for the operation:\n1.Addition 2.Substraction 3.Multiplication 4.Division ')
key=int(input('Enter key:'))
calci(key)

#calendar

import calendar
y=int(input('Enter the year:'))
m=int(input('Enter the month'))
print()
print(calendar.month(y,m))

#Fibonacci Series

def fib(num):
  a,b=0,1
  while a<num:
    print(a)
    a,b=b,a+b

num=int(input('num:'))
fib(num)

#factorial using function

def fact(n):
  if(n==0 or n==1):
     return 1
  else: 
     return n*fact(n-1) 
  

n=int(input('Enter the number:'))
fact(n)

#find the maximum of 3 numbers

num1=int(input('Enter num1:'))
num2=int(input('Enter num2:'))
num3=int(input('Enter num3:'))
if(num1>num2):
  if(num1>num3):
    print('%d is the greatest'%num1)
  else:
    print('%d is the greatest'%num3)
elif(num2>num3):
   print('%d is the greatest'%num2)
else:
  print('%d is the greatest'%num3)

#sum of all numbers in the list

l=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in l:
  sum=sum+i
print('Sum:',sum)

#fatorial using function with user input

def fact(n):
  fact=1
  for i in range(1,n+1):
    fact=fact*i
  return fact
n=int(input('Enter the number to find factorial:'))
res=fact(n)
print('factorial of',n,'is',res)

#check if number falls in specified range

lr=int(input('Define the lower range:'))
ur=int(input('Define the upper range:'))
num=int(input('Enter the number you want to check:'))
for i in range(lr,ur+1):
 if(i==num):
   print(num,'found in range',lr,'to',ur)
 else:
   print(num,'not found in range',lr,'to',ur)

s=str(input('Enter the string:'))

#return list without redundant element using new list

def new(l):
 l1=list()
 for i in l:
  if(i not in l1):
    l1.append(i)
 return l1


L=[1,1,2,3,4,4,5,5,6,7,8,9,9,10]
print('Original list',L)
print('New list',new(L))

#check if a given number is prime

def is_prime(n):
 count=0
 for i in range(1,n+1):
   if(n % i==0):
     count=count+1
 if(count==2):
   print('%d is prime number'%n)
 else:
   print('%d is not prime number'%n)


n=int(input('Enter the number:'))
is_prime(n)

#even number in the list

lis=[1,2,3,4,5,6,7,8,9,10]
for i in lis:
  if(i%2==0):
   print(i)

#palindrome

def palindrome(l):
 return l==l[::-1]

s=str(input('Enter string:'))
l=list(s)
print(l)
res=palindrome(l)
if(res==True):
  print('%s is a palindrome'%s)
else:
  print('%s is not a palindrome'%s)
