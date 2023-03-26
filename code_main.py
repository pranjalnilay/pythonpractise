# Control Structures and Functions
Control structures are the essence of programming; they help computers do what they do best: automate repetitive tasks intelligently. The most common control structures are if-else statements, for and while loops, and list and dictionary comprehensions. This session will cover all these concepts.

### If statements
"IF" statements are imperative in Python and they help us build programs that could make decisions based on a specified condition


*   If I am tired, I'll go to bed

*   If I am hungry, I'll order food

Notice all these applications start with the word 'IF' and that is the first way we are going to control our applications.

And before writing down a code to mimic a decision, let us first look at the relational operators that would help us test or define some kind of relation between two entities.

Relational operators are used to test equality or inequality of a condition and that condition might change based on your preference.

```
Example -
If its raining == True:
  I'll get an umbrella

```









<h2 style = "color:Brown"> Relational Operators</h2>

- Compares the values on either side of the operator and returns and boolean value as True or False.

#### Double equal to operator

10 == 10

<h4 style = "color:Red">Note</h3>

#####' = ' is an assignment operator; it is used to assign value to a variable on the left.

#####'==' is a relational operator; it is used for comparision of equality.

10 == 5

#### Not equal to operator

10 != 5

#### Greater than operator

10 > 5

#### Less than operator

10 < 5

#### Greater than equal to operator

10 <= 5

#### Less than equal to operator

10 >= 5

<h2 style = "color:Brown">Decision Making

Now let's get back to writing a conditional statement with the 'if' condition

To do that we would write it 'if' followed by an expression

#### Write a program to check value in variable x is less than 99

x = 45

if x < 99:
    print(x, "is less than 99")
else:
    print(x, "is more than 99")

x = 919

if x < 99:
    print(x, "is less than equal to 99")
elif x == 99:
    print(x, "is equal to 99")
else:
    print(x, " is more than 99") 

## Logical Operators
We use logical operators in situations where we have multiple conditions

####   AND
####   OR
####   NOR
####   XOR

Are some of the common and most widely used logical operators
You can learn more about them from this link: https://pythonlessons.net/python-logic-gates/




#### Write a program to record the age of visitor and allows him to an exclusive children's day party hosted by Mr Obama only if he or she is above 60 years or below 18 years of age

x = int(input("Enter your age : "))

if x <= 18 or x >= 60 :
    print("Welcome to Party!!")
else:
    print("Sorry!! you do not fit in the age criteria")

#### Write a program which offers various discounts based on purchase bills

shoppinng_total = 550

if shoppinng_total >= 500:
    print("You won a discount voucher of flat 1000 on next purchase")
elif shoppinng_total >= 250:
    print("You won a discount voucher of flat 500 on next purchase")
elif shoppinng_total >= 100:
    print("You won a discount voucher of flat 100 on next purchase")    
else:
    print("OOPS!! no discount for you!!!")

#### Example on nested if-else

world_cups = {2019 : ['England', 'New Zealand'], 2015:["Australia", "New Zealand"], 2011 : ["India", "Sri Lanka"], 2007: ["Australia", "Sri Lanka"], 2003: ["Australia", "India"]}

year = int(input("Enter year to check New Zealand made it to Finals in 20th century : "))

if year in world_cups :
    if "New Zealand" in world_cups[year] :
        print("New Zealand made it to Finals")
    else:
        print("New Zealand could not make it to Finals")
        
else:
    print("World cup wasn't played in", year)


X = 12

if X > 10 & X < 15:
    print('YES')
else:
    print('No')

<h2 style = "color:Brown">Loops and Iterations


Let’s look at a small example where you have a person’s income and expense data across five months in the form of a list, and you want to compute his savings across these five months. You may be thinking of doing this manually by taking the first elements from the two lists and subtracting them, then again taking the second elements and subtracting, and so on. This may look simple, but let’s say it is across 10 or 20 years. Would you do the same? 

 

This is where the concept of iteration comes in handy, as you are repeating the same operation multiple times. With this in mind, let’s learn more about it.

Let's start with a simple 'While' loop - 
##### A while loop begins with a keyword 'While' followed by an expression 
##### So While this condition is satisfied keep running the loop

# Let's create a pin checker which we generally have in our phones or ATMs
pin = input("Enter your four digit pin: ")
while pin != '1234':
    pin = input('Invalid input, please try again: ')  
print("Pin validation successful.")

# Now if we want to add a maximum number of tries allowed condition we'll use the if loop

import sys    #required for exiting the code and displaying an error

pin = input("Enter your four digit pin: ")
attempt_count = 1
while pin != '1234':
    if attempt_count >= 3:
     sys.exit("Too many invalid attempts")   #error code
    pin = input('Invalid input, please try again: ')  
    attempt_count += 1
print("Pin validation successful.")



# iterate over list of integers

l = [1,3,4,2,5,6]
for i in l : 
    print(i)

# iterate over a string

string = "New York"
for ch in string:
    print(ch)

# iterate over a string - modify print using end

string = "New York"
for ch in string:
    print(ch, end = ":") # default value of end = "\n"

# iterating over a dictionary

students_data = {1:['Sam', 24] , 2:['Rob',25], 3:['Jack', 26], 4:['Cornor',24], 5:['Trump',27]}
for key, val in students_data.items():
    print(key, val)

# iterate over keys of a dictionary
for key in students_data.keys():
    print(key)

l = []
for i in range(-100, 0):
    if(i % 2 == 0):
        l.append(i)
l

# Generate range of values.
range(1, 101)

l = list(range(1,101))
l

# Iterate over range of values

for i in range(1, 101):
    print(i, end = " ")

# different variations in range

print(list(range(1, 100, 2) ))# gives numbers from 1 to 100 with a step count of 2
print(list(range(100, 0, -1))) # gives a reversed sequence of numbers from 100 to 1

#### Ex. Write a program to print prime numbers between 1 to 20

for n in range(1, 20):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break   
    if flag :
        print(n)

<h2 style = "color:Brown">Comprehensions

l1 = ["automobiles", "Honda", "Benz", "Suzuki", "Morris Garages" ]

l2 = []

for i in l1 :
    l2.append(len(i))
    
l2 

#### The Functional Approach

# Example on list comprehension

l1 = ["automobiles", "Honda", "Benz", "Suzuki", "Morris Garages" ]

# Create a list consisting of length of each element from the above list

l2 = [len(i) for i in l1]

print(l2)

l1 = ["automobiles", "Honda", "Benz", "Suzuki", "Morris Garages" ]

l2 = [(word.upper()) for word in l1]
l2

d = {x.upper(): x*3 for x in 'acbd'}
print(d)

# iterating over l1 and l2 simultaneously

for i,j in zip(l1,l2):
    print(i, " - ", j)

#### Dictionary comprehension

# Example on dictionary comprehension

l1 = ["automobiles", "Honda", "Benz", "Suzuki", "Morris Garages" ]

# Create a dictionary consisting of element and length of each element from the above list

d = {i : len(i) for i in l1}

print(d)

#### Set Comprehensions

#### Ex . Write a program which takes a word as input from user and returns vowels from the word

word = input("Enter a word : ")
vowels = {i for i in word if i in "aeiou"}
vowels

<h2 style = "color:Brown">Functions</h2>

#### Ex. Write a function which takes a value as a parameter and returns its factorial

def factorial(n):
    
    fact = 1
    
    for i in range(1, n+1):
        fact *= i
    
    return fact

factorial(5)

factorial()

#### Function Arguments

def func(name, age = 35):  # default parameter
    print("name : ", name)
    print("age : ", age)

func("Jane", 25)

func("Jane")

def func(name, age = 35, city = "New York"):
    print("name : ", name)
    print("age : ", age)
    print("city : ", city)
    
func("Jane", city = "Seattle") # key-word argument

def var_func(*args):
    print(args)
    
var_func(1,3,"abc") # variable-length argument

<h2 style = "color:Brown"> Lambda Function

# Write a lambda function to check a number is even or odd

f = lambda x: "even" if x % 2 == 0 else "odd"

f(10)

<h2 style = "color:Brown">map - filter - reduce

#### Some more examples on map - filter - reduce

L1 = [2,4,5]
print(map(lambda x: x**2, L1))
print(list(map(lambda x: x**2, L1)))

#### Defining a function and using it in map

L1 = [2,4,5]
def squareit(n):
    return n**2

print(list(map(squareit, L1)))

#### Filter function to return the multiples of 3 

my_list = [3,4,5,6,7,8,9]

divby3 = lambda x:  x % 3 == 0

div = filter(divby3, my_list)
print(list(div))


#### Ex. Write a python program to count the students above age 18

students_data = {1:['Sam', 15] , 2:['Rob',18], 3:['Kyle', 16], 4:['Cornor',19], 5:['Trump',20]}

len(list(filter(lambda x : x[1] > 18, students_data.values())))

#### Reduce to return product of elements

from functools import reduce

q  = reduce(lambda x, y: x*y, range(1,4))

print(q)

input_list = ['Santa Cruz','Santa fe','Mumbai','Delhi']


input_list = ['Santa Cruz','Santa fe','Mumbai','Delhi','Mumbai']

len(list(filter(lambda x : x[0][0] == "S", input_list)))

input_list = ['Santa Cruz']
input_list[0][0]+input_list[0][-1]

def check(x):
    print(x[0])
    print(x[-1] )
    if x[0] == "s" and x[-1] == 'p':
        return(x)
   

# Python Exam Practice

## Chapter 1- Loops

### Activity 1 - Print First 10 natural numbers using while loop

a = 1
while a<=10:
    print (a)
    a = a+1

### Activity 2 - Print the following pattern
![image.png](attachment:image.png)

n = 5
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print(j,end = ' ')
    print(" ")

### Activity 3 - Calculate the sum of all numbers from 1 to a given number

n=int(input("enter a number"))
s=0
for i in range(1,n+1,1):
    #print(i)
    s = s+i
print(s)

### Activity 4 - Write a program to print multiplication table of a given number

n=int(input("enter a number"))
for i in range(n,n*11,n):
    print(i)

### Activity 5 - Display numbers from a list using loop
![image.png](attachment:image.png)
numbers = [12, 75, 150, 180, 145, 525, 50]

numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    #print(i)
    if i%5==0 and i <=500:
        print(i)
    if i > 150:
        continue;
    if i >500:
        break;

### Activity 6 - Count the total number of digits in a number 75869

n = 75869
count = 0
while n != 0:
    n = n//10
    count = count+1
print(count)

### Activity 7 - Print the following pattern
![image.png](attachment:image.png)

n=5
for i in range(1,n+1,1):
    for j in range(n,0,-1):
        print(j,end = ' ')
        
    print(" ")
    n=n-1

### Activity 8 - Print list in areverse order using loop 
[10, 20, 30, 40, 50]

l = [10,20,30,40,50]
l = list(reversed(l))
for i in range(0,len(l),1):
    print(l[i])


### Activity 9 - Write a program to print all prime numbers within range 25,50

a = 25
b = 50
for i in range(a,b):
    if i > 1:
        for j in range(2,i):
            if i%j == 0:
                break;
        else: print(i)
            


### Activity 10 - Display Fibonacci series up to 10 terms

#[0,1,2,3...]
n = 10
l=[0,1]
for i in range(1,n-2,1):
    s=l[i-1]+l[i]
    l.append(s)
l     

### Activity 11 - Find the factorial of a given number 5

n = 5
s=1
for i in range(n,0,-1):
    s=s*i
print(s)

### Activity 12 - Reverse a given integer number 76542

n = 76542
count = 0
k = []
while n!= 0:
    s = n%10
    n = n//10
    k.append(s)
#76542%10
#76542//10
k = [str(i) for i in k]
''.join(k)

### Activity 13 - Calculate the cube of all numbers from 1 to a given number 6
![image.png](attachment:image.png)

n = 6
for i in range(1,n+1,1):
    print("Current Number is : {} and the cube is {}".format(i,i**3) )

### Activity 14 -  Find the sum of series - 2 upto n terms (n=5)
![image.png](attachment:image.png)


n=5
a=2
l=[]
for i in range(1,n+1,1):
    l.append(str(a)*i)


l = [int(i) for i in l]
sum(l)

### Activity 15 - Print the following pattern
![image.png](attachment:image.png)

n=5
for i in range(0,n,1):
    for j in range(0,i+1,1):
        print("*",end= ' ')
    print(" ")

for i in range(n-1,0,-1):
    for j in range(i+1,1,-1):
        print("*",end= ' ')
    print(" ")

## Chapter 2 - Strings

### Activity 16 - Create a string made of the first, middle and last character "James"

s = "James"
s[0]+s[int(round(len(s)/2,0))]+s[-1]

### Activity 17 - Create a string made of the middle three characters "JhonDipPeta"

s = 'JhonDipPeta'

s[int(len(s)/2)-1:int(len(s)/2)+2]

### Activity 18 - Append new string in the middle of a given string
![image.png](attachment:image.png)

s1 = 'Ault'
s2 = 'Kelly'
s1[0:int(len(s1)/2)]+s2+s1[int(len(s1)/2):len(s1)+1]

### Activity 19 - Arrange string characters such that lowercase letters should come first PyNaTive

s = 'PyNaTive'
for letters in s:
    if letters.islower() == True:
        print (letters,end='')
     
for letters in s:
    if letters.islower() == False:
        print (letters,end='')


### Activity 20 - Count all letters, digits, and special symbols from a given string "P@#yn26at^&i5ve"

s = "P@#yn26at^&i5ve"
l1 = []
l2 = []
l3 = []
for letters in s:
    if letters.isalpha() == True:
        l1.append(letters)
    elif letters.isdigit() == True:
        l2.append(letters)
    else:
        l3.append(letters)
print("letters = {}".format(len(l1)))
print("digits = {}".format(len(l2)))
print("symbols = {}".format(len(l3)))

### Activity 21- Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter
s1 = "Yn"
s2 = "PYnative"

s1 = 'Yn'
s2 = 'PYnative'

s1 = s1.lower()
s2 = s2.lower()

for letters in s1:
    if letters in s2:
        flag=1
    else:
        flag=0
if flag==1:
    print (True)
else: print(False)

### Activity 22 - Write a program to find all occurrences of “USA” in a given string.
str1 = "Welcome to USA. usa awesome, isn't it?"

str1 = "Welcome to USA. usa awesome, isn't it?"
str1 = str1.lower()
str1 = str1.replace('.','')
count=0
for word in str1.split():
    print(word)
    if word == 'usa':
        count = count+1
print(count)

### Activity 23 - Calculate the sum and average of the digits present in a string "PYnative29@#8496"

s = "PYnative29@#8496"
l = [int(i) for i in s if i.isdigit()==True]
print('sum = {}, average = {}'.format(sum(l),sum(l)/len(l)))


### Activity 24 - Write a program to count occurrences of all characters within a string "Apple"

str1 = 'Apple'
str1 = str1.lower()
d = {}
for letters in str1:
    if letters not in d.keys():
        d[letters] = 1 
    else: d[letters] = d[letters]+1
        
print(d)

### Activity 25 - Reverse a given string ""PYnative""

str1 = "PYnative"
d = []
for i in range(len(str1)-1,-1,-1):
    d.append(str1[i])
print(''.join(d))
print(str1[::-1])

### Activity 26 - Split a string on hyphens "Emma-is-a-data-scientist"

str1 = 'Emma-is-a-data-scientist'
for word in str1.split('-'):
    print(word)

### Activity 27 - Remove empty strings from a list ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

l1 = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
list(filter(None,l1))

### Activity 28 - Replace each special symbol with # in the following string '/*Jon is @developer & musician!!'

str1 = '/*Jon is @developer & musician!!'
l1 = []
for letters in str1:
        
    if letters.isalpha()==False and letters.isdigit()==False and letters != ' ':
        letters = '#'
        #print(letters)
    l1.append(letters)

''.join(l1)

### Activity 29 - Removal all characters from a string except integers 'I am 25 years and 10 months old'

str1 = 'I am 25 years and 10 months old'
l1 = []
for letters in str1:
    if letters.isdigit() ==True:  
        l1.append(letters)
''.join(l1)

## Chapter 3 - Functions

### Activity 30 - Write a program to create a function that takes two arguments, name and age, and print their value.

def profile(name,age):
    return (name,age)
profile('Pranjal',27)

### Activity 31 - Write a program to create function func1() to accept a variable length of arguments and print their value.

def func1(*args):
    return(args)
func1('1','a',3,'f')

### Activity 32 - Write a program to create a function show_employee() using the following conditions.

It should accept the employee’s name and salary and display both.
If the salary is missing in the function call then assign default value 9000 to salary

def show_employee(name,salary=9000):
    return(name,salary)
print(show_employee('Pranjal',1000))
print(show_employee('Pranjal'))

def outer_func(a,b):
    def inner_func(a,b):
        return(a+b)
    return (inner_func(a,b)+5)
outer_func(5,5)

### Activity 33 - Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

def rec_sum(n):
    if n>0:
        return( n + rec_sum(n-1))
    else:
        return 0
rec_sum(10)      

## Chapter 4 - Data Structures [Lists] (Tuples) Sets{} {Dictionary}

### Activity 34 - Create a list by picking an odd-index items from the first list and even index items from the second
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = [i for i in l1 if i%2!=0]
l4 = [i for i in l2 if i%2==0]
l3+l4

### Activity 35 - Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
list1 = [54, 44, 27, 79, 91, 41]

list1 = [34, 54, 67, 89, 11, 43, 94]
element = list1.pop(4)
print(list1)
list1.insert(2,element)
print(list1)
list1.insert(len(list1),element)
print(list1)

### Activity 36 - Slice list into 3 equal chunks and reverse each chunk [11, 45, 8, 23, 14, 12, 78, 45, 89]

l1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]
l2 = l1[0:int(len(l1)/3)]
l3 = l1[int(len(l1)/3):int(len(l1)/3)*2]
l4 = l1[int(len(l1)/3)*2:int(len(l1)/3)*3]
print(list(reversed(l2)),list(reversed(l3)),list(reversed(l4)))


### Activity 37 - Count the occurences of each element from the list [11, 45, 8, 11, 23, 45, 23, 45, 89]

l1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]
d={}
for i in l1:
    if i not in d.keys():
        d[i] = 1
    else: d[i] = d[i]+1
print(d)

### Activity 38 - Create a Python set such that it shows the element from both lists in a pair
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
Expected Output - {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}

first_list = [2, 3, 4, 5, 6, 7, 8] 
second_list = [4, 9, 16, 25, 36, 49, 64]
first_list = set(first_list)
second_list = set(second_list)
d = []
for i in first_list:
    for j in second_list:
        if i**2 == j:
            d.append((i,j))
        
print(d)

first_list = [2, 3, 4, 5, 6, 7, 8] 
second_list = [4, 9, 16, 25, 36, 49, 64]
print(set(zip(first_list,second_list)))

### Activity 39 - Find the intersection (common) of two sets and remove those elements from the first set
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
elements  = first_set.intersection(second_set)
[i for i in first_set if i not in elements] 

### Activity 40 - Checks if one set is a subset or superset of another set. If found, delete all elements from that set
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
if first_set.issubset(second_set):
    first_set.clear()
if second_set.issubset(first_set):
    second_set.clear()
print(first_set)
print(second_set)

### Activity 41 - Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
for l in roll_number:
    if l not in sample_dict.values():
        roll_number.remove(l)
roll_number

### Activity 42 - Remove duplicates from a list and create a tuple and find the minimum and maximum number
[87, 45, 41, 65, 94, 41, 99, 94]

l1 = [87, 45, 41, 65, 94, 41, 99, 94]
t1 = tuple(set(l1))
print(t1)
print(max(t1))
print(min(t1))

### Activty 43 -  Unpack the tuple into 4 variables 
tuple1 = (10, 20, 30, 40)

tuple1 = (10, 20, 30, 40)
a,b,c,d = tuple1
print(a,b,c,d)

### Activity 44 - Sort a tuple of tuples by 2nd item (('a', 23),('b', 37),('c', 11), ('d',29))

tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)

### Activity 45 - Write a program to add all its elements into a given set.
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
sample_set.update(sample_list)
sample_set

### Activity 46 - Return union,intersection, a set of item present in set 1 but not in set 2 and a set of elements present in Set A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

### Activity 47 - Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
d = dict(zip(keys,values))
print(d)

### Activity 48 - Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)

### Activity 49 - Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
sampleDict['class']['student']['marks']['history']

### Activity 50 - Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

###### Keys to remove
keys = ["name", "salary"]

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)

### Activity 51 - Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

a = min(sample_dict.values())
for key,values in sample_dict.items():
    if values == a:
        print(key)

#Another way
print(min(sample_dict, key=sample_dict.get))