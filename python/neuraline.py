#                Video no. 2
#  1). string keyword always surrounded by quotation marks 
#  2). you can use double quotation 
#  3). triple quotation marks for multiline comment
#  4). bool are data type true or false

# str = "hello" 'heelo'
# ''' 
# Mullti comment'''

#               Video no. 3  Different type of operators
# print(9+2)
# print(3**5)
# print(8%2)
# print( 10 // 1)
# print(3 // -1)  # floor division always running down to the negative number 


# x = 20
# x = x + 10
# x += x + 30 + x
# print (x)
# # these ar the opearator combined with the airthmetic operaor 
 
# # 1). comparators operator is used for comparasion 
# # 2). and demands to both the condition to the true

# # == 
# # !=
# # <
# # >
# # <=
# # >=
# x = 10
# y = 60

# print(x == y)  #false
# print(x < y)   #true
# print(x != y)   #true

# x = "Hello"
# y = "Hellos"

# print(x == y)

# #             and or not
# print(10 < 20 and 20 > 80)
# print(50 > 10 and 50 == 50)

# print(not True)   #not true is falsee
# print(not 10 < 20)
# print(not 1 < 20)

# # 3). bitwise an operator which  is used to perform which is used to perform logical operations on binary number

# #                      user Input
# # 1). we are generally defines values directly in our code but sometimes which takes data from out side
# # 2). its done by using input function

# # input is always taken as input in string 

# x = input("Enter the no.")
# y = input("Enter number two")

# x = int(x)    # it specifies it is int 
# y = int(y)

# print(x + y**x)




# #          video no. 4    If statements and conditions  

# # 1). comparision operators returns true  
# # 2). if statement check conditions for true 


# x = input(" enter the no. of x ")
# y = input(" enter the input for the second no.")

# X = int(x)
# Y = int(y) 

# if x < y:
#     print("x is less than y!")
# elif x > y:  # for multiple condition 
#     print(" x is greater than y")  
#     if x > 100:
#         print("x is greater than 1000")  # nested conditions
# else: 
#     print(
#         "x is equal to y"
#     )

# 3). so with use of multiple conditions we are making decision trees of the conditions we are putting multiple logical decision structure 



#   Practice       Video no. 5     If statement and conditions

# x = input("enter the first no.")
# y = input("enter the second no.")

# X = int(x)
# Y = int(y)
# if X> Y:
#     print(" x is greater than y")
#     if(x > 2*y):
#         print("x is two times of y")

# elif  X == Y:
#     print(" x is equal to y")
#     if X % Y == 0:
#         print(" x is completely divide by y")

# else:
#     print("x is not greater than y")
    




#                                        Video no. 5    ||   Loops and Conditions
# 1). in previous video we learn about if and now move forward to our new video we are goona discuss about for loop and while loop
# 2). whhile loop - executes certain piece of code again and again till when the certain condition retrives true ... on each iteration it returns the result
# 3). for loops is used for counting and telling compiler how many times we need to return result
# x = 0
# while x < 30:
#     x += 10   # we add this again and again till x becames 10
#     print (x)
# while True:    # if you want loop for endless times 
#     print("Something")   
# 4). range is an float object because it only iterates for particular no. not float
# 5). imagine range is like array of that numbers 
# for x in range(100/4):
#     print(x/5)

# 4). x is an control variable with iterates from certain no. sequences

# for x in range(1, 21):
#     print(x)

# 5). on next video we are goona learn about for loop and 

# 6). onee thing is quite useful when it comes too loop control statement

# x = 0
# while x<10:
#     if x == 9:
#         break   # loop break statement
#     x += 1
#     print (x)

# x = 0
# while x < 20:
#     x += 1
#     if x == 5:
#         continue    # skip the current iteration
#     print(x)

# pass statement - Allows to Fill places in a script when code is needed when we really known what gonna put in this place at in fututre
# y = 250
# if y == 250:
#     pass 
# print("123")

# x = 25
# while x < 25:
#     pass
# print("the if statement is passes")






#                             Video no. 6 || Loops and conditions
# x = 0
# while(x < 20):
#    x += 10
#    print(x)
# x = 20
# while(x != 20):
#    print (x)

# for x in range(1, 21):
#    print(x)

# for x in range(20):
#    print(x)

# x = 0
# while(x < 10):
#     x += 1
#     if x== 5:
#         break   #stop the loop
    
#     print(x)
# x = 0
# while(x < 10):
#     x += 1
#     if x == 3:
#         continue    
#     print(x)

# x = 0
# while(x < 10):
#     x += 1
#     if x == 3:
#         pass
#     print(x)


#         Video no .6    ||  Sequences and Collections






#                  Video no. 7   ||  Functions

# 1). In pass 
# 2). function is just a block of reusable code  
# 3). so we are using function to making code more reusable code in less no. of code
# 4). def is an keyword and (define parameter) , : is says this funtion is ready to use 

# def helloworld():
#     print("hello world ")
#     print("hello world 66y")

# helloworld()
# 5). this is less block of code if we there were more code then this can more useful
# 6). python is all about dynamically and less code 
# def add(x , y , z):
#     print(x * y * z)

# add(10, 35 , 89)
# 7). after defining function we need to return the function

# def add( x, y , z):
#     return (x + y + z)


# result = add( 10, 20 , 30)
# print(result)

# result = add(19, 19 , 90)    # does not give result any thing 
    
# 8). Another tt pass default parameters then it prints nothing

# def add(x = 1, y=hing which we can do that we can define default value for the parameter sometimes we can give default paramater for the function   
# 9). If we can no0):      # you can set default value at starting 
#      return x + y * x
#      return x + y
# result = add()
# print(result)
# 10). for taking multiple positional argument we need to pass with in args
# def mysum(*numbers):
#     result = 0
#     for number in numbers:
#          result *= number
#     return result 

# print(mysum(10 , 20 , 30 , 40 , 50 , 60))


#                  Video no. 8  ||  Exception and Error handling in Python
# 1). When you typecast a text into number that does not contain a number it gets a error if it is unhandled then it becames unhandled
# 2). If the error happens then the next of the codes will not runs
# print(10/0)     # zero division error

# x = "sanidhya"
# int(x)   # invalid literal for int()

# try:     # if try block not correctly runs then run the block of except
#     x = int(input("enter the first number"))
#     y = int(input("Enter the second number"))
#     print(x/y)

# 3). at this point two errors were possible i). or i can divide by zero or ii). if i type that text which can not type cast then it shows errors 
# 4). A named except clause can not appears after the catch all clause    

# except:
    # print("there is an error")
# except ValueError:
#     print("there was an value error")
# except ZeroDivisionError:

# 5). generally we passes the handling condition when error occurs
   
    # print("Can not divide by zero!")
    # y = 1
    # print(x/y)

# 6). finally code always be executables 
# 7). finally is used for streams .. when we use generally use streams we always close to the streams

# finally:
#     print("Done!")

# 8). streams are very promient to errors ... opening streams , closing streams ..
# 9). some times we have functions and specific conditions then we used to raise exceptions ... 

# 10). rasise function executes when the particular condition is true

# def function():
#     if True:
#         raise ValueError("Something went terribly wrong")
    
# function()

# 11). assert function gives exception if the given condition is not true

# x = 4
# y = 9

# assert(x > y)






#         Video no. 9     ||     Exception and Error Handling

# print(4/0)

# try:
#     x = int(input("enter the first number"))
#     y = int(input("enter the second number"))
#     print(x/y)    # zero division error && string
# # except:
# #     print("there is an error")
# except ZeroDivisionError:
#     print("don't include zero")
#     y = 1
#     print(x/y)

# except ValueError:
#     print(" there in type casting ")

# finally:       
#     print("Done")

# # raise function gives response when the condition is true 

# # def function():
# #     True
# #     raise ValueError  

# # function()

#     x = 5
#     y = 4
#     assert(x < y)   # assertion  error

#                      File Streams       
# 1). for open file,.. file = open('filename.txt','r')

# every streams need to be closed 
# file = open('myfile.txt','r')
# content = file.read()
# file.close()
# print(content)

# 2). use with statement when you work with file 
# 3). when we used with statement as there were no need to openn and close the stream

# 4). read method is for get the content of the file
# r - reading mode ..

# import os  
# # os.path.exists()
# file_path = r"C:\Users\sanid\OneDrive\Desktop\myfile.txt.txt"
# if os.path.exists(file_path): 
#     print("file exist")
# else:
#     print("file not found")

# file_path = r"C:\Users\sanid\OneDrive\Desktop\myfile.txt.txt"
# with open(file_path, 'r') as f:
#      content = f.read()
# print(content)

# file = open(r"C:\Users\sanid\OneDrive\Desktop\myfile.txt.txt", 'w')
# file.write("hello youtube")
# file.close()
# print(content)

# 5). file.close() not only close the files but also flushes the streams 
# 6). if you flush() you can use the stream but while you use the close you can't use the stream again

# file = open(r"C:\Users\sanid\OneDrive\Desktop\myfile.txt.txt" , 'r')
# content = file.read()

# print(content)
# file.close()

# 7). for overwrite something using overwrite method

# 8). if any error occured while using file stream then use try catch method 

  # try  # some stream code 
  # except # catch the error
  # finally # is used for closed the stream

# file = open(r'C:\Users\sanid\OneDrive\Desktop\myfile.txt.txt', 'a')
# file.write("hello youtube")
# file.close()
# file.flush()

# For renamed file or removed file we can use os module   

# you can create directory and remove directory 


# from os import *

# mkdir("test")  # make directory
# chdir("test")  # change directory

# rename('myfile.txt', 'file.txt')

# remove('file.txt')


#                Video no. 10    ||   String functions
# 1). sometimes handling string is very important fudamental to use that in future
# 2). string is sequence of characters so we treat as list 
# 3). we can apply list operations on string 
# 4). we can apply list methods on to the string as when its needded 

# text = "hello world "
# print(text[4])
# print(text[9:])

# for letter in text:
#     print(letter)

# print(text[6:])
# print(len(text))

# 5). back slash n is used for break the line 
# text = "hello world!\n this is today moring"
# '''
# asdfdfdsf
# asdfsdfds
# '''
# \t -- tab and \b - backspace \a - space 
# print(text)

#               string formatting 
# name = input("give your name")
# age = int(input())

# %d is usedd for specifying integers and quotation marks wwe need to specify variables with %
# print("my name is " + name + " and i am" + age +"year old")

# more simplified way for formatting is {} placeholder 
# print("My name is %s and I am %d years old " % (name, age))
# print("my name is {} and i am {} year old ".format(name,age))
# print("hello world on today {} i specified my way to visit america los angeles one {} pm".format(name, age))

#                              String functions 
# text = "This is my text"
# text = "Hello world"
# text = text.upper() # capitalises every word
# text = text.title()  # capitalises only first characters of each word
# text = text.swapcase()  # swapcase each characters present in a string

# text = "A city 4 delhi is PPolluted by the careless peoples"

# # # 6). .count is used for how many times your particular string occur in your string 
# # 7). you can make a count of multiple strings or of uppercase and together 
# print(text.count("delhi") + text.count("P"))
# print(text)

# # 8). .find returns the starting index of particular substring in a string 
 
# text = "I am sanidhya and i am 17 year old then what i need is you"

# print(text.find("I"))


# text = "My self sanidhya a coding enthusiasts who loves to coding in python and c++"
# text = text.find("My")
# print(text)

# # 9). do int function is use to join a string separated by separator

# separator = ' - and - '
# mylist = ['Kitchen', 'dogs', 'cats', 'vehicles', 'gardens']

# print(separator.join(mylist))

# # 10). we can convert a string into sequence by using split method with given string variable

# # 11). No method or attribute it means you not use the method properly
# # 12). we can split and remove a particular substring in a string 


# # name = ['rotwiller', 'labrador', 'husky' ,'pamoleon', 'great den',]
# # separator = ' '

# # 13). split is used for splitting a particular substring for all occurences in string

# name = "rotwiller husky dalmitian pamoraian husky great den pitbull germanshepered"
# # print(separator.join(name))

# dogs = name.split('a')
# print(dogs)





#                             Intermidiate 1 || Python Object

# 1). Python object is an paradigm of an object which is usedd for converting real world applications into our programming world like examples city , villages and all of them 
# 2). __intit__ is constructor method  to defining a object
# 2). self parameter is a parameter which refers to object , self parameters points to the attribute of the object 
# 3). 

# class Animal:
#     price = 0
# # 4). if you want more types of values pass more parameters into init method 
# # this set of block is called as constructor method 
# # 5). self refers to the current object , init is a special method in a python class it is automatically runs when a new objectt is created 
#     def __init__(self,  agename , , height):
#         self.name = name
#         self.age = age
#         self.name = name
#         self.height = height
#     # amount is not refered to self so it is called along class
#         Animal.price += 1
        
#     def __del__(self):
#         Animal.price -= 1
      
#     def __del__(self):
#         print("Object Deleted")
# # calls the constructor
# # from accessing the attribute we need to use of . method 

# # first object 
# print(Animal.price)
# Animal1 = Animal("Mike", 30, 180)

# print(Animal1.name)
# print(Animal1.age)
# print(Animal1.height)

# Animal2 = Animal("Pitbull", 25, 400)
# print(Animal2.name)
# print(Animal1.age)
# print(Animal2.height)




# # 6). del keyword is used for deleting a particular del keyword
# # 7). del Animal1 from the memory  so you can use it later in the code 
# del Animal1  

# # 8). class variables also be used to track how many objects have been created from the class


#                  Intermidiate 2  ||  Inheritance 
# 1). Inheritance is a fundamental concept in object-oriented programming where a class (child or derived class) acquires the properties and behaviors (data and functions) of another class (parent or base class).
# 2). Overriding is when a subclass (derived class) provides its own specific implementation of a method that is already defined in its superclass (base class).

# class Person:
#     # this is an constructor method init is an initialiser self refers to the instace of the classes and name , age and height are the attributes that are setted while the creation of objects 
#     def __init__(self, name, age, height):
#         # these are instance variable assignments. they store the input values as attributes of the object being created using the self instances 
#         self.name = name
#         self.age = age 
#         self.height = height

#     def __str__(self):
#         return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)

#     def get_older(self,years):
#         self.age += years
 
#     def __str__(self):
#         text = super().__str__()
#         text += ", Salry {}".format(self.salary)
#         return text 
#     # from now we have all the overwritten methods 
# class worker(Person):  #worker is an person and treated as person 
#     # This class have all the attributes of the base class so reinitiallised everything is not be the good reason 
#     def __init__(self, name, age, height , salary):
#         # super method is a method is used to call a method from a parent class inside a child class also extends the functionality of the parents function 
#         # __init__ function being callled by __init__ method 
#          super(worker,self).__init__(name, age, height)
#          self.salary = salary

#     def calc_yearly_salary(self):
#         return self.salary * 20

# Worker1 = worker("Henry", 40, 176, 3000)
# print(Worker1)
# print(Worker1.calc_yearly_salary())

#                                   Operator Overloading 
# 1). operator overloading defines what happens when you are applying operations on two or more objects 
# 2). Operator overloading allows programmers to redifining the behaviour of standard operations with the objects 
# 2). java do not allowed operator overloading , whereas c++ and python allows 
# 3). (***IN vectors Operator overloading are generally and perscibally used to add particular value with the vector)
# 4). (***Python uses dunder ,methods or magic methods allows custom behavious ..) which automatically specifies the behavious of standard operators like subraction for subtraction of vector objects and addition function addition only when it satisfied on to the class 

# class Vector:
#     def __init__(self, x, y):
#         self.x =x 
#         self.y = y 
#     def __add__(self, another):
#         return Vector(self.x  + another.x , self.y + another.y)
#     def __sub__(self, another):
#         return Vector(self.x - another.x, self.y - another.y)
#     def __str__(self):
#         return "X: {}, Y: {}".format(self.x, self.y)
    
# v1 = Vector(2,5)
# v2 = Vector(6,3)

# print(v1)   
# print(v2)   

# v3 = v1 - v2
# print(v3)  

#                        Multithreading 
# 1). threading - increase the speed of the programs by the runs multiples path at a time
# 2). run multiple threads simultaniously so it increases speed inbetween cordinations and every thing
# 3). Multithreading is a programming techinques where multiple threads executed concurrently to perform tasks at the same time within a single process 
import threading 

# after importing threading it allows u to work on everything means everything like from printing hello world 100 times to perform operations multithreading evrythig should be done as you want 

# def helloworld():
#     print("helloworld") 

# a thread is the smallest unit of execution or process within a pocess it represents a single sequence of instructions that can be managed independently 
# threading.Thread class is used to create and manage threads and target parameter specifies the function that the thread should execute
# target parameters except a reference to a function object that is the function itself without executing it.
# target = must be a function object   

# t1 = threading.Thread(target=helloworld())
# t1.start()

# we can also perform threading on multi functions 
# def function1():
#     for x in range(1000):
#         print("CBSE")

# def function2():
#     for x in range(2000):
#         print("two")

# # for running both loop same times concept of multi threading concept are introduced to handling both of them 
# t1 = threading.Thread(target=function1)
# t2 = threading.Thread(target=function2)

# # run function does'nt works parallel 

# t1.start()
# t2.start()


# def hello():
#     for x in range(50):
#         print(50)

# t3 = threading.Thread(target=hello)
# # the main thread doesn't wait for t3 to finish unless explicitly tells it to do so 
# t3.start()
# # sanidhya was too hury for execution the tasks for sanidhya run simultaneously the chances of result could be anything it depends 

# print("Sanidhya")

#                  Synchronizes threading 
# handles the condition of multiple threats 
# How to manages multiple threats at once like some of the want to execute different multiple operations at same time like some executes read some write etc, 
# A locking method is a method which is used for gaining a control access to shared resources in a multithread ennviornment it prevents - (i) race conditions(multiple data comes) , (ii) data inconsistencies, (iii) ensure only one thread at a time 
# for string concatenation or formatting issues - when multiples values are priniting together 

# import threading
# import time 

# # Note - lock.aquire() If no other thread is holding the lock → it gains access immediately.
# # Note - other wise it waits block until the lock is released 
# x = 12148
# # create a Lock object from the threading module and store it into a lock variable 
# lock = threading.Lock()
# def function1():
#     global x , lock   # defining global is essential because python thinks x is local variable 
#     # lock thread ensures only one thread at a time like putting a Do Not Disturb sign on the doors 
#     # ask the lock for enter the critical section , if available enters if not wait untill its free 
#     lock.acquire()
#     # now thread gets exclusive access to resource or section of code 
#     while(x < 163284):
#       x *= 2
#       print(x)
      
#       # programe pauses or sleeps for 1 second 
#       time.sleep(1)
      
#     print("Reached the maximum")
#     # when is locked reset it to the unlocked 
#     lock.release()

# def function2():
#     # use x and lock from global variable 
#     global x , lock 
#     lock.acquire()
#     while(x > 100):
#         x /= 2
#         print(x)
#         time.sleep(1)
#     print("Reached the manimum")
#     # release a lock
#     lock.release()
    
# ta = threading.Thread(target=function1)
# tb = threading.Thread(target=function2)

# ta.start()
# tb.start()


#                  Semaphore Method   (parking)
# 1). Semaphores are used in multithreading or multiprocessing enviornments to control access for shared resources to shared resources - espicially when there is limited no. of units of resources or available.
# 2). limit the access to the resources to maximum value 
# 3). printer case only 2 people can access the printer at once so semophores limit the access for 2 peoples and avoids overloading 
# 4). parking only 4 car can park in the parking so i limit the access for 4 cars by putting a banner with only 4 car allowed for parking so it prevents 
# import threading
# import time 

# # this line creates a bounded semaphore with initial count 5 limnit resources to 5 threads
# semaphore = threading.BoundedSemaphore(value=4)
# # for accessing particular thread 
# def access(thread_number):
#         print("{} is trying to access!".format(thread_number))
#     # after 5 time we are granted access to the semaphores 
#        # gain access to shared resource for one thread at a time 
#         semaphore.acquire()
#         print("{} was granted access!".format(thread_number))
#         time.sleep(5)
#         print("{} is now releasing! ".format(thread_number))
#         semaphore.release()

# # *** t is threaded object that is assigned to execute the function access as its target when started 
# t = threading.Thread(target=access, args=(4,))
# t.start()
# for thread_number in range(1,6):
#  #  *args - passing an argument in thread variable 
#     t = threading.Thread(target=access , args = (thread_number,))
#     t.start()
#     time.sleep(1)

#         Events and Daemons thread ()
# Events - In Python threading, an Event is a synchronization primitive that is used to signals between threads.
# 1). The gate is closed (event not set).

# A worker (thread) arrives and waits outside the gate (event.wait()).
# The manager (main thread) asks: “Should I open the gate?” (input()).
# If you say "Y", the manager opens the gate (event.set()).
# The worker walks in and starts working (performing action to xyz).

# import threading

# # event is an object that have to perform some action
# event = threading.Event()   #  (signal initially set to OFF).

# def myfunction():
#       print("waiting for event to trigger.. ")
#      # wait until the event is triggred 
#       event.wait() # wait till get signal from thread to trigring a event  # wait for signal event to turn on, then it continues to execute , 
#       print("performing action to xyz")

# # thread running my function 
# t1 = threading.Thread(target=myfunction)
# t1.start()


# # Any code out side the threading.thread is consider and executes as main thread.
# x = input('do you want to triger')
# if x == "Y":
#       event.set()  # All the waited events are now trigred 
    


#                     Demons thread (*janitor of office)
  
# Demons threads are used for background tasks that should not block by the program 
# Demons threads are special threads used for background tasks are that are not essential to keep programm running 
# i). daemon=True - Marks a thread as daemon before .start()
# ii). Auto-terminates - Dies when the main program ends (even if it's still running)
# iii). No blocking - Won’t prevent the program from exiting
# imagine demons thread as janitor working and cleaning in office ones everyone leaves the office(main thread ends) he stops working and goes home. 
# iv). t is an optional 


# "r"	Read (default)
# "w"	Write (overwrite)
# "a"	Append
# "r+"	Read + Write (no truncate)
# "w+"	Write + Read (truncates)
# "a+"	Append + Read

# import threading
# import time 

# path = "text.text"
# text = ""

# def readFile():
#       global path, text
#       while True:
#             with open("text.text","w+") as f:
#                   text = f.read()
#             time.sleep(3) 

# def printloop():
#       for x in range(30):
#             print(text)
#             time.sleep(1) 

# # "t"  is modifier stands for text mode (which is already the default).
# # "t" alone is not a valid mode. It needs to be paired like "rt" (read text) or "wt" (write text), but "r" or "w" 
# t1 = threading.Thread(target=readFile, daemon=True)   # the thread marks as daemons thread should ends when main threads ends   # This thread is a background helper. It should not block the program from exiting.” 
# t2 = threading.Thread(target=printloop)

# t1.start()
# t2.start()  

#                      Queues (Producer and consumer)
# 1). When multiple threads are working together, they often need to share data. But just sharing variables directly is risky — it can lead to race conditions or data corruption.
# 2). Producer-Consumer Problem (Classic Example) - Producer thread are generatings tasks ii). consumer threads are processing/handling those tasks iii). buffer to hold data between producer and consumer by .. i) Adds item in the queue ii). takes items from the queue and process the item  by adding data into the queue and taking data/task from the producer in queue and takes data the queue for 
# 3). Queues are providing safest way for threads to communicate and share data.

# 4). queue.Queue(): A thread-safe FIFO queue
# 5). put(): Adds an item (blocks`` if full)
# 6). get(): Takes an item (blocks if empty)
# 7). task_done(): Signals that a task is finished
# 8). daemon=True: Makes consumer a background thread that dies with main program

# 9). If there were multiple methods the best method to get data is via queue gives next data and can not be get back to them 

import queue 
#  getting list a data getting for a data 

q = queue.Queue()
numbers = [10, 20, 30, 40, 50]

for numbers in numbers:
   q.put(numbers)


print(q.get())
print(q.get())
print(q.get())

# 
import queue
q = queue.LifoQueue()  # start giving the last element from the queue

numbers = [1,2,3,4,5,6,7]
for number in numbers:
   q.put(number)
   q.put(number)

print(q.get())
print(q.get())
print(q.get())

q = queue.PriorityQueue()  # python min heap , the smallest item retrive first based on the key

q.put(2, "hello world")
q.put(11,99)
q.put(2,5)
q.put(1,True)

while not q.empty():
   print(q.get())


#            Sockets And Network Programming 
# 1). Sockets are end points of the channel 
# 2). Server are used to making connections between client and server communnication
# 3). phone call as an example 

# import socket 
# # for creating socket tell them 
# s = socket.socket(socket.AF_int , socket.SOCK_STREAM)
# s.bind(('127.0.0.1', 55555))
# s.listen()

# while True:
#     client, address = s.accept() #when clients start to sharing data 
#     print("connencted to {}". format (address))
#     client.send("You are connnected ".enncode())
#     client.close()


#           DATABASE 

import sqlite3
connection = sqlite3.connect("mydata.db")
cursor = connection.cursor()
cursor.execute("""
               CREATE TABLE Persons(
                    first_name TEXT,
                    last name TEXT,
                    age integer
                         ) """)

connection.commit()
connection.close()  
#  for inserting data into the tables 

cursor.execute("""
(ISERT INTO persons VALUES
('paul', 'smith', 24)),
('Mark', 'johnson', 42),
('Anna', 'smith', 34)
               """)


# .connect - connecting database in current working directory 
# .cursor is used for making connection between database for performing sql queries or queries to the database
# .execute is used for performing sql queries 
# .commit - without commit data is not updated 
# 




