##############This Code is not secured#############

# def a(name):
#     return name
# def b(name):
#     return name
# print(a('Nandakumar'))
# print(b('Menaka'))

##############################################
# class student:
#     name=None
#     age=None
#     city=None
#
# person1=student()
# person1.name="Nanda"
# person1.age=18
# person1.city="Toronto"
#
# person2=student()
# person2.name="Menaka"
# person2.age=17
# person2.city="Ottava"
#
# person3=student()
# person3.name="Prajay"
# person3.age=11
# person3.city="Quebec"
#
# print(person3.name)
# print(person2.age)
# print(person1.city)
############Another Example for Class#############
# class Dog:      # Creates a basic blueprint called Dog.
#     def bark(self): # Inside it, bark() is a function that says "Woof!"
#         print("Woof!")
# class Cat:
#     def meow(self):
#         print("Meow!")
# # Create the animals
# my_dog = Dog()  # creates one dog.
# my_cat = Cat()
#
# # Make them talk
# my_dog.bark() # makes it bark
# my_cat.meow()
#####################################################
# class Car:
#     def drive(self):
#         print("Vroom! The car is moving.")
#
# my_car = Car()
# my_car.drive()
########################################################
# class Fan:
#     def __init__(self, fan_type, brand, speed_levels, is_remote_controlled):
#         self.fan_type = fan_type
#         self.brand = brand
#         self.speed_levels = speed_levels
#         self.is_remote_controlled = is_remote_controlled
#
#     def show_details(self):
#         remote = "Yes" if self.is_remote_controlled else "No"
#         print(f"{self.fan_type.capitalize()} Fan by {self.brand}")
#         print(f"Speed Levels: {self.speed_levels}")
#         print(f"Remote Controlled: {remote}")
#
# # Creating different types of fan objects
# ceiling_fan = Fan("ceiling", "Bajaj", 5, True)
# tower_fan = Fan("tower", "Hawells", 3, True)
# table_fan = Fan("table", "Wipro", 2, False)
#
# # Showing their details
# ceiling_fan.show_details()
# tower_fan.show_details()
# table_fan.show_details()

###################Inheritance######################
####################with out inheritance###########
# class Parent:
#     def Sing(self):
#         print("Parent is singling")
# class Child:
#     def Dance(self):
#         print("Child is Dancing")
#     def Sing(self):
#         print("Child is singing")
# talent = Child()
# talent.Sing()
####################with inheritance################

# class Father:
#    def Sing(self):
#        return("Singing talent is available")
#
# class Mother:
#     def Cook(self):
#         return "Cooking talent is available"
#
# class Child(Father,Mother):
#    def Dance(self):
#        return("Dancing talent is available")
#
# # Create object
# talent = Child()
#
# print(talent.Sing())
# print(talent.Dance())
# print(talent.Cook())

#######################################################################
# class Father:
#    def Sing(self):
#        return "Singing talent is available"
#    def __init__(self):
#        self.networth=1000000
#
# class Mother:
#     def Cook(self):
#         return "Cooking talent is available"
#
# class Child(Father,Mother):
#    def Dance(self):
#        return "Dancing talent is available"
#
# # Create object
# talent = Child()
#
# print("Please find all the talents of children below")
# print(talent.Sing())
# print(talent.Dance())
# print(talent.Cook())
# print(talent.networth)
#
# #################################################################
# ###############Types of Inheritance:
# #################################Single level inheritance
#
# class Parent:
#
#    def __init__(self):
#        self.networth = 1000000
#
#    def Sing(self):
#        print("Parent is singing")
#
# class Child(Parent):
#    def Dance(self):
#        print("Child is Dancing")
#
# child1 = Child()
# child1.Sing()
# print((child1.networth))
#
#
# ####################Multi level inheritance (more than 1 level is multi level)
#
#
# class Grandparent:
#    def Swim(self):
#        print("He can swim")
#
# class Parent:
#    def __init__(self):
#        self.networth = 1000000
#
#    def Sing(self):
#        print("Parent is singing")
#
# class Child(Grandparent):
#    def Dance(self):
#        print("Child is Dancing")
#
# child1 = Child()
# child1.Swim()
#
#
# ################Multiple - To access both classes in chile we need multiple
#
# class Grandparent:
#    def Swim(self):
#        print("He can swim")
#
# class Parent:
#    def __init__(self):
#        self.networth = 1000000
#
#    def Sing(self):
#        print("Parent is singing")
#
# class Child(Grandparent,Parent):
#    def Dance(self):
#        print("Child is Dancing")
#
# child1 = Child()
# child1.Swim()
# child1.Sing()
#
#
#
# ########################Hierarchical Inheritance:
#
# class Grandparent:
#    def Swim(self):
#        print("He can swim")
#
# class Parent(Grandparent):
#    def __init__(self):
#        self.networth = 1000000
#
#    def Sing(self):
#        print("Parent is singing")
#
# class Child(Grandparent):
#    def Dance(self):
#        print("Child is Dancing")
#
# child1 = Child()
# child1.Swim()
#
#
#
# ##################Hybrid Inheritance:
#
# class Grandparent:
#    def Swim(self):
#        print("He can swim")
#
# class Relative(Grandparent):
#    def Drive(self):
#        print("Driving")
#
# class Parent(Grandparent):
#    def __init__(self):
#        self.networth = 1000000
#
#    def Sing(self):
#        print("Parent is singing")
#
# class Child(Parent,Relative):
#    def Dance(self):
#        print("Child is Dancing")
#
# child1 = Child()
# child1.Drive()

################Encapsulation##################
###########Public##############################
# class Education:
#    def __init__(self):
#        self.Name = "Nandakumar"
#        self.Place = "Toronto"
#        self.Revenue = "$5000"
#
# school = Education()
# print(school.Name)
# print(school.Place)
# print(school.Revenue)

#############Private##############################
# class Education:
#    def __init__(self):
#        self.Name = "Nandakumar"
#        self.Place = "Toronto"
#        self.__Revenue = "$5000"
#
# school = Education()
# print(school.Name)
# print(school.Place)
# #print(school.__Revenue)

###################Protected##########################
# class Education:
#    def __init__(self):
#        self.Name = "Nandakumar"
#        self.Place = "Toronto"
#        self._Revenue = "$5000"
#
#
# class Faculty(Education):
#    def Revenue1(self):
#        print(self._Revenue)
#
#
# faculty = Faculty()
# print(faculty._Revenue)

#####################################################
##########Polymorphism#############################
# #####without Polymorphism############################
# class Person:
#     def __init__(self,name,age):
#         self.Name=name
#         self.Age=age
#     def sleep(self, sleepinghours):
#         print("sleeping duration is", sleepinghours)
#
# person1=Person("Nanda", 10)
# person1.sleep(8)
###############With Polymorphism####################
# class Person:
#     def __init__(self,name,age):
#         self.Name=name
#         self.Age=age
#     def sleep(self, sleepinghours):
#         print("sleeping duration is", sleepinghours)
#     def sleep(self, start, end):
#         print("Sleeping Duration is", end-start)
# person1=Person("Nanda", 10)
# person1.sleep(1,8)

##########Another Way with proper code####################
###############Compile time Polymorphism###################
# class Person:
#     def __init__(self,name,age):
#         self.Name=name
#         self.Age=age
#     def sleep(self, sleepinghours=None, start=None, end=None):
#         if start is not None and end is not None:
#             print("Sleeping duration is", end-start)
#         else:
#             print("Sleeping Duration is", sleepinghours)
#
# person1=Person("Nanda", 10)
# person1.sleep(8)
# person1.sleep(start=10, end=16)

#################Runtime Polymorphism####################
# class Parent:
#     def Drive(self):
#         print("Parent is Driving")
# class Child:
#     def Drive(self):
#         print("Child is Driving")
# obj=None
# name=input()
# if name=="Parent":
#     obj=Parent()
# else:
#     obj=Child()
# obj.Drive()
################################################################
#######################Abstraction################################
# from abc import ABC,abstractmethod       # C:\Users\User\AppData\Local\Programs\Python\Python313\Lib
# from calendar import IllegalMonthError
# from copy import deepcopy
# class Bank(ABC):                #abstract class
#     @abstractmethod    #you should not share this
#     def withdraw(self):
#         pass
#
# class account(Bank):
#     def withdraw(self):
#         print("Withdraw amount 5000")
#
# bank1=account()
# bank1.withdraw()

#############More precise on Abstraction###########################

from abc import ABC,abstractmethod

class Bank(ABC):          #abstract class

   @abstractmethod
   def withdraw(self):    ##name changes will impact!!!
       pass

   def senquiry(self):   #name changes will not impact
       print("The balance is 2000")

class account(Bank):
   def withdraw(self):
       print("withdraw amount 50000")

   def enquiry(self):
       print("The balance is 4000")

bank1 = account()
bank1.withdraw()
bank1.enquiry()
#################################################