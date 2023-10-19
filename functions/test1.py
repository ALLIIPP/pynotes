#!/usr/bin/python3

#functions
#---------------------------------------------------------------
def add_one(num):
    return num+1

add_one(10)
#---------------------------------------------------------------

#keyword arguments
#---------------------------------------------------------------
'''
function arguments preceded by an identifier // order doesnt matter
'''

def thing(arg1, arg2):
     #print(arg1+' '+arg2)
     pass

thing(arg2="huh", arg1='what')
#---------------------------------------------------------------



#*args
#---------------------------------------------------------------
'''
 *args - parameter that will pack all arguments into a tuple
        // makes it so that a function can accept a varying amount of arguments
'''
def dostuff(*things):
    num = 0
    for thing in things:
        num=num+thing
    return num

dostuff(1,2,3,4,5)

#---------------------------------------------------------------



#kwargs
#---------------------------------------------------------------
'''
**kwargs - parameter that will pack all arguments into a dictionary
          // function can accept varying amount of keyword arguments
'''

def aa(**kwargs):
    for key,value in kwargs.items():
       # print(key+' '+value)
       pass

aa(a='1',b='2',c='3')
#---------------------------------------------------------------



#Exception Handling
#---------------------------------------------------------------

try:
    a = 1
except NameError as e:
    print('Name Error: '+str(e))
except Exception as e:          #except Exception used as a 'catch-all' 
    print('Other Error: '+str(e))
else:                           #gets called if not errors
    pass
finally:                        #alweays gets called
    pass

#---------------------------------------------------------------



#file detection
#---------------------------------------------------------------
import os

path = '/home/uub/Desktop/py/samplle.txt'

if(os.path.exists(path)):       #checks if path exists
    print('the path exists')
if(os.path.isfile(path)):       #checks if path is a file
    print("It is a file")       
if(os.path.isdir(path)):        #checks if path is directory
    print("It is a directory")
#---------------------------------------------------------------



#write files
#---------------------------------------------------------------

path = '/home/uub/Desktop/py/sample.txt'

# 1) without using with statement
file = open(path, 'w')
file.write('hello world !')
file.close()

'''
An exception during the file.write() call in the first implementation
can prevent the file from closing properly which may introduce several
bugs in the code, i.e. many changes in files do not go into effect
until the file is properly closed. 
'''
 
# 2) without using with statement (safer)
file = open(path, 'w')
try:
    file.write('hello world')
finally:
    file.close()

'''
The second approach in the above example takes care of all the
exceptions but using the with statement makes the code compact
and much more readable.
'''

# 3) using with statement
with open(path, 'w') as file:       #overwrites file 
    file.write('hello world !\n')

with open(path,'a') as file:        #appends to file
    file.write('More test\n')

#---------------------------------------------------------------



#read files
#---------------------------------------------------------------
with open ('./sample.txt') as file:     
    #print(file.read())
    pass
#---------------------------------------------------------------



#copying a file
#---------------------------------------------------------------
import shutil
'''
copyfile() -> copies contents of a file
copy()     -> copyfile() + permission mode + destination can be a directory
copy2()    -> copy() + copies metadata (files creation/ modification times)
'''

#   shutil.copy('sample.txt','./fakedir')  

#---------------------------------------------------------------



#move a file / directory
#---------------------------------------------------------------
import os

source = '/home/uub/Desktop/py/fakedir'
dest = '/home/uub/Desktop/py/otherdir/fakedir'

try:
    if(os.path.exists(dest)):
        pass
       # print('theres already a file there')
    else:
        pass
       # os.replace(source,dest)     #move file from src -> dst

except FileNotFoundError:
    print('source was not found')

#---------------------------------------------------------------



#delete a file
#---------------------------------------------------------------
import os
import shutil

try:
    os.remove('sample.txt')     # remove files
    os.rmdir('fakedir')     #remove empty directory
    shutil.rmtree('fakedir')    # remove a directory containing files
except FileNotFoundError as e:
    pass
    #print('could not find directory')
#---------------------------------------------------------------



#import modules
#---------------------------------------------------------------
#type 1
#import modules.module as stuff      #import module from different folder

#type 2
from modules.module import greetings, add2nums

#type 3 
#from modules.module import *        #import all 

#greetings()

#---------------------------------------------------------------

 
#functions as variables
#---------------------------------------------------------------
'''
a function can be a variable
'''

say = print             # both point to the same location in memory 
                        # ( the location of the function)
say('Were saying stuff')

#---------------------------------------------------------------



#higher order functions
#---------------------------------------------------------------
'''
higher order functions  - functions that either :  
                                1.) accepts a function as an argument
                                    or
                                2.) returns a function
'''

# 1) - accept function as argument
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):            # accepts and calls function 
    print(func('hello'))

#hello(quiet)    

# 2) - make function return function
def initNum(x):
    def multiply(y):
        return x*y
    return multiply

five = initNum(5)
#print(five(6))
 
#---------------------------------------------------------------



#lamda functions
#---------------------------------------------------------------
'''
lamda function  - a function written in one line using 'lambda' keyword
                - accepts any number of arguments, but only has one expression
                - (think of it as a shortcut)
                - (useful if needed for short period of time)
'''

double = lambda x:x*2
square = lambda x:x**2
add = lambda x,y:x+y
age_check = lambda age: True if age >10 else False

#print(age_check(0))

#---------------------------------------------------------------


