print("hello world")

# This is single line coomment 
""" this is multiline comment"""

if 10>5:   
    print("10 is greater than 5")
else:
    print("10 is less than 5")       

# Variables
x = 5                 
y = "Hello, World!"   
print(x)
print(y)

   

# Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3             
z = float(3)  # z will be 3.0

# Get the type
x = 5       
y = "John"
print(type(x))
print(type(y))

import keyword      #keyword is a module in python
print("totoal keyword list is this")
print(keyword.kwlist)           #print all the reserved keywords in python
print(len(keyword.kwlist))

"""Value keyword = true , false , none
   operator keyword = and , or , not . is , in 
   control flow keywords = if , else , elif , while , for , break , continue ,  pass , try , except , finally , raise , assert
   Function and Class = def , return , lambda , yield , class
   context management = with , as 
   import and module = import , from , as 
   scope and namespce = global , nonlocal
   async programming = async , await
   """

print(float(True == False))
print(int(True == 0))

print(True + True + False + True)
print(type(None))

print(None == 0)
print(None == {})      #None is special constant which has no values, or null value

# operator keyword and , or , not , is , in
a = False
b = True

print (a + b)

print(3 in [1, 2 ,3])  #in is used to check the value is present in the list , tuple , set , dictionary or not

if 'p' in 'python':
    print('p is present in python')
else:
    print('p is not present in python')

if 50 is not 50:
    print('50 is 50')

a = 50
b = 60 
c = "hello"

if c is 'hello':
    print('c is hello')      #is is used for checking two variables are pointing to the same object or not

if a is not b:
    print("a is not b")

# Conditional keywords if, else , elif ,while, for , break , continue , pass , try , except , finally , raise assert
p = "python"
if p == "python":
    print("p is python")

x = 5
y = 7
z = 12

if x + y >= z:
    print("true")
if x != y:
    print("x is not equal to y")
else:
    print("false")

# python for loop is used for iterating over a sequence (List, Tuple, String) or other iterable objects

g = ["frog", "apple","cat"]
for i in g:  #i ia a variable wchich is used to iterate over the  list
    if i == "apple":
        print("apple is present in the list")
    print(i)

s = "hello"
for i in s:
        print(i)

# range() function is used to generate a sequence of numbers
for i in range(5 , 10 , 2):  #range(start, stop, step)
    print(i)

for i in "gfgfgfgggghytytytyffhfhfhytyt":
    if i == "g" or i == "f":
        continue  #continue keyword is used to skip the current iteration and continue with the next iteration
    print(i)

for i in "huhuhuhuioppppppppp":
    if i == "i":
        break  #break keyword is used to exit the loop  
    print(i)

for i in "sanidhya":
    if i == "n":
        pass  #pass keyword is used to write empty loops .... placeholder for future code
    print(i)

li = ["apple", "banana", "cherry"]
for i , j in enumerate(li):  #enumerate() function is used to loop through the list with the index
    print(f"Index {i} : {j}")
print(list(enumerate(li)))

def add(num1 : )
