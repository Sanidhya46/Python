#                                    1). Check the given no. is even or odd

# n = int(input("Enter your number"))        #python by default takes input in string
# def even(n):
#     if(n%2 ==0):
#         print( "the no. is even")
#     else:
#         print("the no. is odd")

# even(n)  #call the function



# number = int(input("enter the number"))
# def check(number):
#     if(number %2 == 0):
#         print(f"{number} is even")    #using f string to printing  integer with string
#     else:
#         print(f"{number} is odd")

# check(number)


# num = int(input("Enter the number"))
# def check(num):   #defininng a function check with parameter num
#     if(num %2 == 0):
#         print(str(num) +" is even")
#     else:
#         print(str(num) +" is odd") 

# check(num)


#                                using bitwise operator 
# num  = int(input("Enter the number"))
# def even(num):
#     return num & 1 == 0
# if even(num):
#     print(str(num) + " is even")
# else:
#     print(str(num) + " is odd")


                #                          2). program to print multipication of number
# num = int(input("Enter the number "))
# def table(num):        #function name table with parameter num
#     for i in range (1,11):     #for loop which goes for specified range
#         print(num*i)      #for every iteration return the  result
    
# table(num)    #calling the function

# num = int(input("Enter the number"))
# def table(n):
#     for  i in range (1,11):
#         print("%d*%d = %d " % (n , i ,n*i))         # %d is format specifier used for old style string formatting 
#         # print("%d + %d = %d") % (n , i , n*i)     # % modulo operator used for formatting
#                                                     # (n,i , n*i) is tuple inserted into %d placeholder
# table(num)      #calling the user defined fuction


# Built-in Functions ---- Predefined in Python (e.g., print(), len())
# User-Defined Functions --- Created using def by the user
# Lambda Functions --- Anonymous one-line functions using lambda
# Recursive Functions ---  Functions that call themselves
# Higher-Order Functions --- Functions that take or return another function
# Generator Functions --- Use yield instead of return for lazy evaluation
# Nested Functions ---	Functions defined inside other functions
# Decorator Functions --- Modify the behavior of other functions

# num = int(input("Enter the number"))      # inputting a integer 
# def table(num):         # user defined function with parameter num  
#     for i in range (1,11):   # for loop where i iterates for ranges
#         print(f"{num} * {i} = {num * i}")    # Standard form of formating using f 
# table(num)    # for calling user defined function type function name and parameter in small brackets

# import builtins
# # print(dir(__builtins__))  # dir is used for list all attributes and method of an object 

# # Get all built-in functions
# builtin_functions = [f for f in dir(builtins) if callable(getattr(builtins, f))]    # f is string representing the name of built in function 
#                                                                                     # if callable checks if the attributes associted with the name f is callable (i.e function , method or class)
# # Print total count
# print("Total built-in functions:", len(builtin_functions))    # this is the print message for displaying all builtin_functions in python

#                                           using recursive function (multiplication of two number)
# Algorithm -- 1). make an recursive  function with a argument int n , int limit = 10 , int times = 1
#              2). base case if limit > times  return;   , recursive call --  n * recursive(times + 1)

# def recursive(n , limit = 10 , times = 1):
#     if times > limit:
#         return 0
#     print(f"{n}*{n} = {n*n}")        # f string method is used along with variables using curly braces for them
#     return n * recursive( n , limit ,times + 1)         # calling all the arguments is essential
    

# if __name__ == "__main__":        # scripts code runs only when executed directly  ....  __name__ is special built in variable and main isstring WHICH represents the scripts run directly
    
#    n = int(input("Enter the number"))       # assigning an integer input box to variable n
# recursive(n)     #calling the recursive function 

#   ********                             2).  Program to find sum of n natural numbers   i). for loop    ii). recursion  iii).formula 

#  Algo -- 1). defining a functionn with parameter int n
#          2). makng an variable for storing sum
#          3). runninig for loop from ranges 1 to n
#          4). on every iteration add results to sum  -- sum = sum + i , sum += i , 

# def cal_sum(n):
#     result = 0
#     for i in range (1,n):
#         result += i   #accumlate sum on every iteration and storing into result
#     return result
# n = int(input("Enter the number"))
# print(cal_sum(n))

#                                     using recursion method to find the sum of natural numbers
# Algo -- 1). making the fnction with parameter n 
#         2). making base case when (n == 0); return 0;
#         3). making recursive call return n + cal_sum(n -1)

# def cal_sum(n):
#     if(n == 0):
#         return 0
#     return n + cal_sum(n-1)         # cal_sum function calls recursively and add into n

# n = int(input("Enter the number"))
# print(cal_sum(n))

# def sum_n(n):0
#     if(n == 0):
#         return 0    # it stops the recursion
#     return n + sum_n(n - 1)

# n = int(input(" Enter the number "))
# print(sum_n(n))        

#                                 using formula for sum of n natural number
# Algo -- 1). making an function with parameter n
#         2). making an variable result which just do operatioin ( n * ( n+1 /2)) and stores the result

# def formula_sum(n):
#     result = n * ((n+1)/2)
#     return result

# n = int(input(" Enter the number "))
# print(formula_sum(n))
      
#                      3).   swap two number    i)/ using native approach with third variable  ii). expected approach without usig third variable  iii).  alternate approach built in swap
# Algo -- 1). make an function with two parameter a and b
#         2). creating  an variable temp to store value of a and  assign into b
#         3). print a and temp

# def swap_(a,b):
#     temp = a       #value  of a store into variable into temp
#     a = b          #  value of b is assigned to a
#     b = temp
#     #eturn swap_(a,b)   # this calls its own function for infinite times
#     return a ,b     # returning ariable for further use

# a = 10
# b = 40
# a , b = swap_(a,b)    # assigning new value is important
# print(a,b)

#                                using expexted approach without using third ariable
# Algo -- 1). defining a function which takes two parameters
#         2). value of a is assigning to b and value of b is assigning to a 
#         3). calls the function and print the variable a and b 

# def _swap(a,b):
#     a , b = b , a
#     return a , b    # returning multiple function

# a = 10
# b = 40

# print(_swap (a,b))

#                               using alternate approach built in swap 
# if __name__ == "__main__":     # using when you execute code directly
#     a = 10
#     b = 20
#     a , b = b , a
#     print(a,b)          

#                                   swaping using third variable 
#  Algo -- 1). defining a function with two parameter a and b 
#          2). making a new  variable temp assigning value of a ,   a = b , assigning value of temp in b

# def _sum(a,b):
#     temp = a
#     a = b
#     b = temp
#     return a , b    # python by default return multiples values in tuples

# a = 10
# b = 50
# print(_sum(a,b))

