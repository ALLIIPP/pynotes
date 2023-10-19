#!/usr/bin/python3

# Classes and Inheritance
# Multi-Level Inheritance                                                                                                                                                                                                                              \

class Vehicle:

    def __init__(self, name ,color,speed,size,occupancy):
        self.name = name
        self.color = color
        self.speed = speed
        self.size = size
        self.occupancy = occupancy

    def start(self):
        print('The vehicle is moving')

    def stop(self):
        print('The vehicle is stopped')

    def getStats(self):
        print("Name : "+self.name)
        print("Color : "+self.color)
        print("Speed : "+self.speed)
        print("Size : "+self.size)
        print("Occupancy : "+self.occupancy)


class Automobile:

    def __init__(self, type):
        self.type = type
    
    def autoType(self):
        print('this is a '+self.type+' type automobile')


class Car(Vehicle, Automobile):     #class can inherit from multiple classes

    def __init__(self, name, color, speed, size, occupancy, carstuff):
        Vehicle.__init__(self, name, color, speed, size, occupancy)      #provide inputs to super class
        Automobile.__init__(self, 'Car')                                 #provide inputs to super class
        self.carstuff = carstuff
    

    def doSomething(self):
        print('do car stuff '+ self.carstuff )