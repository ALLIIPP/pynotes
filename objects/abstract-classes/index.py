#!/usr/bin/python3

#abstract class
#---------------------------------------------------------------
'''
abstract - prevents a user from creating an object of that class
         - compels a user to override abstract methods in a child class

abstract class - a class which contains one or more abstract methods
abstract method - a method that has a declaration but does not have an 
                  implementation
'''

from abc import ABC, abstractmethod     # abc - Abstract Based Class

class Vehicle(ABC):     #define an abstract class
    
    @abstractmethod     #define an abstract method
    def go(self):
        pass

    def vroom(self):
        print('VROOM')

class Car(Vehicle):

    def go(self):                       #child class must implement abs. method
        print('You drive the car')

class Motorcycle(Vehicle):

    def go(self):                       #child class must implement abs. method
        print('You drive the motorcycle')

 

car_1 = Car()
car_1.go()

moto_1 = Motorcycle()
moto_1.go()


#---------------------------------------------------------------
