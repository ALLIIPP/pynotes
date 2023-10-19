#!/usr/bin/python3

#Variable Types
#---------------------------------------------------------------
#string type
astring = "Word "
#integer type
age = 4
#float type
afloat = 1.2 
#boolean type
aboolean = True
#---------------------------------------------------------------



#multiple assignment
#---------------------------------------------------------------
thing1,thing2,thing3 = "thing1", "thing2","thing3"
var1 = var2 = var3 = 85
#---------------------------------------------------------------



#String Methods
#---------------------------------------------------------------
name = "A Name"
len(name) #returns the length of the string
name.find('A  ') #returns the position of the first occurance of a character/s
name.capitalize() #capitalize the first letter of the string
name.upper() #returns the conents of string in all Upper Case
name.lower() #returns the conents of string in all Lower Case
name.isdigit() #returns true if string is all 0-9, false otherwise
name.isalpha() #returns true iz only a-zA-Z in string, false otherwise
name.count("s") #returns the number of times a character/s appears in a string
name.replace('A',"K") #returns a string with a character/s replaced
#---------------------------------------------------------------



#Type Casting
#---------------------------------------------------------------
a_string = "string"
a_int = 5
a_float = 8.9
a_tuple = ('a','b','c')

int(a_float) #returns value converted to integer // always rounds down
str(a_float) #returns value converted to string
float(a_int) #returns value converted to float
list(a_tuple) #returns value converted to list
#---------------------------------------------------------------



#User Input
#---------------------------------------------------------------
    #value1 = input("Enter a number : ") # accept user input and save to variable
#---------------------------------------------------------------


#Number Methods
#---------------------------------------------------------------
import math

num = 3.5

math.ceil(num)  #round UP to nearest int
math.floor(num)  #round DOWN to nearest int
math.sqrt(25) #square root
abs(num)    #absolute value
pow(num,2)  #raise number to a power
round(num)  #round number to nearest integer
max(3,4,5,6,7)  #returns the largest out of a set of numbers
min(3,4,5,6,7)  #returns the smallest out of a set of numbers

#---------------------------------------------------------------


#String slicing
#---------------------------------------------------------------
a_string = "This is a String"

#[START:STOP:COUNT] // count default == 1
a_slice = a_string[0:6] #return a string slice [inclusive, exclusive]
a_slice = a_string[6:] #return a string slice from 6 to END
a_slice = a_string[0::2] # return a string made up of every other character
a_slice = a_string[::-1] #return the string reversed

#slice command
b_string = "https://google.com"

b_slice = slice(8,-4) #returns word starting at index 8 and ending at index -4
                      # negitive indexes begin counting at -1 then ..-2..-3 etc.
                      #slices are reusable and MUST BE APPLIED to the string
b_string[b_slice] #returns the sliced word (ie. 'google' )
#---------------------------------------------------------------



# if statements
#---------------------------------------------------------------
age = 9
if(age == 9): 
    print('')
elif(age > 5):
    print('')
else:
    print('')
#---------------------------------------------------------------



#logical operators
#---------------------------------------------------------------
    # and - AND operator
    # or - OR operator
    # not - ! operator

if(True and False):
    print('shit')
if(False or False):
    print('shit')
if not (True or True):
    print('shit')

#---------------------------------------------------------------


#while loops
#---------------------------------------------------------------
x = 1
while x < 10:
    #do stuff
    x=x+1


#---------------------------------------------------------------



#for loops
#---------------------------------------------------------------
#can iterate through anything iterable (ie. strings, arrays, range)
# range(START:END:COUNT)
a_string = "word word word"
for i in range(1):     
    #for x in range(80,100):
    for char in a_string:
        pass
#---------------------------------------------------------------


#sleep
#---------------------------------------------------------------
import time

time.sleep(0.1) # sleep for 1 second
#---------------------------------------------------------------


#print
#---------------------------------------------------------------
print() #print string then go to new line
print("",end="") #print string without going to new line
#---------------------------------------------------------------



#Loop Control
#---------------------------------------------------------------
#break - break out of loop
#continue - continue to next iteration
#pass - placeholder
#---------------------------------------------------------------


#Lists
#---------------------------------------------------------------
array = ["word1","word2","word3","word1"]
array.append("word4")
array.remove("word1") # removes the first occurance of element
shit = array.pop() # removes and returns last item in array 
array.insert(1,"word?") #inserts an element at a given position
array.sort() #sorts array alphabetically
array.clear() #removes contents of an array

if "word3" in array:
    pass
#---------------------------------------------------------------



#Tuples
#---------------------------------------------------------------
a_tuple = ("Name",359,"Thing")

a_tuple[0] #access an element of a tuple
a_tuple.count("Name") #count the number of times a value appears in a tuple
a_tuple.index('Name') #return the index of the first occurance of a value


#---------------------------------------------------------------



#Set
#---------------------------------------------------------------

'''a set is an unordered, unindexed, collection w/ no duplicate
values '''

utensils = {"knife","fork","spoon",1}
dishes = {"bowl","plate","cup",1}

utensils.add("napkin") # add item to a set
utensils.remove("fork") #remove item from a set
#utensils.clear() # removes all items from set
dishes.update(utensils) # add set:utensils to set:dishes
dinner_table = utensils.union(dishes) #return the combination of 2 sets

dishes.difference(utensils) # return a set containing the difference between two sets
dishes.intersection(utensils) # return a set containing the intersection of two sets
 
#---------------------------------------------------------------



#Dictionary
#---------------------------------------------------------------
''' 
dictionary - a changeable unordered colection of unique key:value pairs

'''

dictionary = {
    "key1":"value1",
    "key2":"value2",
    "key3":"value3",
}
dictionary["key1"] # get a value from the dictionary (unsafe if value not in dict)
dictionary.get('asd') # get a value from the dictionary (safe as it returns 'None')
dictionary.keys() # print keys
dictionary.values() # print values
dictionary.items() # print all - > [('key':'value')]

dictionary.update({'key4':'value4'}) #update dictionary
dictionary.pop('key4') #remove entry from dictionary (by key)
dictionary.clear() #wipe dictionary

#---------------------------------------------------------------



#indexing //substring - subarray
#---------------------------------------------------------------
a_string = "This is a String"
a_array = ["a","b","c","d","e"]

a_array[0:4]
a_string[0:4]
a_string[-1] #return last element
#---------------------------------------------------------------



#string format
#---------------------------------------------------------------
formatted = "Format 1 : {} // Format 2 :{}".format("cat",'dog')
formatted_1 = "Format 1 : {1} // Format 2 :{0}".format("cat",'dog')
formatted_2 = "Format 1 : {f1} // Format 2 :{f2}".format(f1="cat",f2='dog')
#---------------------------------------------------------------



#random
#---------------------------------------------------------------
import random

random.randint(1,6) #generate a random int between 1-6 (inclusive,inclusive)
random.random() #random number between 0 and 1

list_1 = ["cat","dog","mouse","turtle","bird"]
random.choice(list_1)   #get a random element from a list
random.shuffle(list_1) #takes list and shuffles it (changes list object , doesnt return anything)

#---------------------------------------------------------------



#walrus operator  (Python 3.8 < )
#---------------------------------------------------------------
''' 
:=  ->  the walrus operator assigns values to variables as part of a 
        larger expression
'''

'''
#without walrus

foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
            break
    foods.append(food)
'''

#with walrus
foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)

#---------------------------------------------------------------



#sort 
#---------------------------------------------------------------
student = ['Mike',"Jerry","Stewart","Greg"]
shoes = ("sneakers",'fancy','running','sandals')
nums = [1,2,3,4,5,6,7]
orders = [
    ("burger",'L',5),
    ("shrimp",'M',6),
    ("hotdog",'S',2),
    ("pizza",'S',1),
    ("cake",'L',10),
    ("taco",'L',92),
]
 
student.sort()                      #sort array alphabetically
student.sort(reverse=True)          #sort array alphabetically (reversed)

sorted_shoes = sorted(shoes)        # sorted() accepts a tuple and returns a sorted function
 
orders.sort()                       #sort array by first element by default

size = lambda size:size[1]          #sort by specific element in 2x array
orders.sort(key =size)
 
#---------------------------------------------------------------



#map (list)
#---------------------------------------------------------------
thing = [
    ("thing1",1,5),
    ("thing2",2,6),
    ("thing3",3,7),
    ("thing4",4,8),
]
square = lambda obj: (obj[0],obj[1],obj[2]**2)

thing2 = list(map(square,thing))        # map function requires a function 
                                        # to apply and a list to apply it to

#---------------------------------------------------------------



#filter (list)
#---------------------------------------------------------------
lisst = [
    ('thing',1,10),
    ('thing',2,20),
    ('thing',3,30),
    ('thing',4,40),
]

filt = lambda x: x[1] > 2

new_list = list(filter(filt,lisst))
#print(new_list)

#---------------------------------------------------------------



#reduce
#---------------------------------------------------------------
'''
reduce() - apply a function to an iterable and reduce it to a single cumulative
         - value. 
         - performs function on first two elements and repeats process until
         - one value remains
'''
import functools

letters = ["A","B","C","D","E"]

result = functools.reduce(lambda x,y:x+y,letters)

#print(result)

#---------------------------------------------------------------



#list comprehension
#---------------------------------------------------------------
'''
    a way to create a new list with less syntax can mimic certain lambda
    functions, easier to read

    1. list = [expression for item in iterable]
    2. list = [expression for item in iterable if conditional]
    3. list = [expression if/else for item in iterable]

'''
nums = [1,2,3,4,5,6,7,8,9]

list1 = [i**2 for i in nums]
list2 = [i**2 for i in nums if i > 5]
list3 = [i**2 if i >5 else "nope" for i in nums]

#---------------------------------------------------------------



#dictionary comprehension
#---------------------------------------------------------------
'''
dictionary comprehension - create dictionaries using an expression 
                         - can replace for loops and certain lambda functions
'''
names = {'name':"asd",'car':"asdasd",'color':'red'}

names_upper = {key.upper():value.upper() for (key,value) in names.items()}
names_p1 = {key+'1':value+'1' for (key,value) in names.items() if key == 'car'}
names_p2 = {key:"uhh" if value == "red" else "umm" for (key,value) in names.items()}

#print(names_p2)
#---------------------------------------------------------------



#zip function
#---------------------------------------------------------------
'''
zip(*iterables) - aggregate elements from two or more iterables 
                - (list, tuples, sets, etc)
                - creates a zip object with paired elements stored in tuples
'''

usernames = ['username1','username2','username3']
password = ['password1','password2','password3']

users = list(zip(usernames, password))

#print(users)

#---------------------------------------------------------------



# __name__ == 'main'
#---------------------------------------------------------------
'''
used to check if the calling program is a module or a standalone program 
an then do things based on that (one program can function as both)
'''

#print(__name__)

#---------------------------------------------------------------



#time
#---------------------------------------------------------------
import time

time.ctime(0)                       #accepts seconds since unix time and converts to date
time.time()                         #seconds since unix time
time_object = time.localtime()      # creates time object which has a bunch of info 
                                    # about current date (month, day, year, seconds, daylight savings, etc.)

#---------------------------------------------------------------



#threading
#---------------------------------------------------------------
'''
GIL (Global Interpreter Lock) : only allows one thread to hold the control 
                                of the Python interpreter at one time

cpu bound - program/task spends most of its time waiting for internal events
          - (CPU intensive -> multiprocessing)

io bound - program/task spends most of its time waiting for EXTERNAL event
         - ie. user input, web scraping (CPU is waiting -> multithreading)

# default only one thread running ca
'''

import threading
import time




def test_1():
    time.sleep(3)
    print('Doing test_1')

def test_2():
    time.sleep(4)
    print('Doing test_2')

def test_3():
    time.sleep(5)
    print('Doing test_3')

x = threading.Thread(target=test_1, args = ())      # define  process 'target' in a seperate thread and pass in 'args' to function
y = threading.Thread(target=test_2, args = ()) 
z = threading.Thread(target=test_3, args = ()) 

x.start()                                           # begin the process
y.start()
z.start()


x.join()                                            # force calling thread (MAIN) to wait until process finishes 
y.join()                                            # to continue
z.join()



#print(threading.active_count())         # displays # of active threads
#print(threading.enumerate())            # displays active thread names
#print(time.perf_counter())              # time it takes Main Thread to complete program

#---------------------------------------------------------------



#daemon threads
#---------------------------------------------------------------
'''
daemon thread  - a thread that runs in the background, not important
               - for program to run. The program will not wait for daemon
               - threads to finish before exiting.
               - Non-Daemon threads cannot normally be killed, they stay alive
               - until the task  is complete
        
                - ex. background tasks, garbage collection, waiting for input, 
                      long running processes
'''

def count():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print('Logged in for {} seconds'.format(count))

x = threading.Thread(target = count, daemon=True)           # create a daemon 

#x.setDaemon()                                               # can set thread to daemon like this
#x.start()                                                   # start daemon

x.isDaemon()                                                # return True id thread is Daemon
answer = input("Do you want to exit ?")


#---------------------------------------------------------------




#multiprocessing
#---------------------------------------------------------------
'''
multiprocessing - running tasks in parallel on different cpu cores, bypasses GIL
                - used for threading
'''

from multiprocessing import Process, cpu_count

def counter(num):
    counter = 0
    while counter <num:
        counter +=1


def main():
    a = Process(target=counter, args=(1_000_000_000))
    a.start()
    a.join()

    print('finished in {}'.format(time.perf_counter()))

if __name__ == '__main__':
    main()

#---------------------------------------------------------------


#get the type of a variable
print(type(age))

#type casting
print(astring + str(age)+'  '+str(afloat)+' '+str(aboolean))