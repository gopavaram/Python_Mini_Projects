# import random
# Primitives = immutable 
# Complex Objects = mutable and are stored by reference
# name=['A','B','C','D',['E','F','G']]
# numbers=[500,300,250,150,600,700,650]

# print(dir(numbers))

# print(name[::-1])

# name.append(['H','I','J'])
# print(name)
# print(name.index('B'))

# name.reverse()
# name.reverse()
# print(name)
# numbers.sort(reverse=True)
# print(numbers)

# for index, item in enumerate(name):
#     print(index,item)

# # list concatination and list replication

# list_zeros=[]
# # list_zeros.append(0)
# # print(list_zeros)


# for i in range (10):
#     list_zeros.append(i)

# print(list_zeros)

# zeros=['A','B']*10

# print(zeros)

# class Person:
#     species = "Human"  # Class attribute (shared by all instances)

#     def __init__(self, name):
#         self.name = name  # Instance attribute

# person1 = Person("Varun")
# person2 = Person("Himaja")

# print(person1.species)  # Output: Human
# print(person2.species)  # Output: Human
# print(person1.species)

# class Dog:
#     def __init__(self, name, age):  # Constructor method (an instance method)
#         self.name = name  # Instance attribute
#         self.age = age    # Instance attribute

#     def bark(self):  # Instance method
#         print(f"{self.name} barks!")  # Accesses the 'name' attribute

#     def get_age(self):  # Instance method
#         return self.age  # Returns the age of the dog

# # Creating instances
# dog1 = Dog("Buddy", 5)
# dog2 = Dog("Max", 3)

# # Calling instance methods
# dog1.bark()  # Output: Buddy barks!
# print(dog2.get_age())  # Output: 3

# #Instance is an object of a class
# #Instance attribute, Class attribute
# #Instance method (slef), class method(cls)
# # Defining the attributes right while instantiating the object

# class complex_add:

#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
    
#     def add_complex_num(self, a):
#         original=self.real+a.real
#         dummy=self.img+a.img
#         result=complex(original,dummy)
#         return result
#         # print(f"{self.real}+{self.img}i")


# n1= complex_add(1,5) #we are instantiating an object of class complex_add
# n2= complex_add(4,3)
# res = n1.add_complex_num(n2)

# print("Real ",res.real)
# print("Img ", res.imag)

# class Triangle: # Creating a class
#     #Defining the init method
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
    
#     #Defining the perimeter method to calculate the perimeter
#     def perimeter(self):
#         perimeter=self.a+self.b+self.c
#         return perimeter
    
# t1=Triangle(10,11,12) #instinciating the object of class Triangle
# perimeter=t1.perimeter() #calling the instance method
# print("Perimeter of the triangle is:",perimeter) # printing the perimeter of the triangle

# # Code to create a single linked list
# #First creating the node


# class Node:

#     def __init__(self, data):
#         self.data=data
#         self.ref= None

# class Linked_List:

#     def __init__(self):
#         self.head = None

#     def add_begin(self, data):
#         new_node = Node(data)
#         new_node.ref = self.head
#         self.head = new_node
    
#     def add_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             n = self.head
#             while n.ref is not None:
#                 n=n.ref
#             n.ref = new_node
    
#     def after_node(self, data, x):
        
#         n=self.head
#         while n is not None:
#             if x == n.data:
#                 break
#             n=n.ref
#         if n is None:
#             print("Item is not present")
#         else:
#             new_node = Node(data)
#             new_node.ref = n.ref
#             n.ref = new_node
    
#     def add_before(self, data, x):

#         new_node = Node(data)
#         n=self.head
#         if n is None:
#             print("The list is empty")
#             return
#         if n.data == x:
#             new_node.ref = self.head
#             self.head = new_node
#             return
        
#         while n.ref is not None:
#             if n.ref.data == x:
#                 break
#             n=n.ref
#         if n.ref is None:
#             print("The Item list is empty")
#         else:
#             new_node.ref = n.ref
#             n.ref = new_node
                            
#     def print_ll(self):
#         n=self.head
#         while n is not None:
#             print(n.data, "--->", end=" ")
#             n=n.ref

# ll1=Linked_List()
# ll1.add_end(8)
# ll1.add_begin(10)
# ll1.add_begin(20)
# ll1.add_end(50)
# ll1.after_node(17,8)
# ll1.add_before(100,50)
# ll1.add_before(150,20)
# ll1.print_ll()


# # Adding two complex numbers

# class Comp_Number:
#     def __init__(self, real, comp):
#         self.real = real
#         self.comp = comp
    
#     def add_num(self,n):
#         real =self.real + n.real
#         comp = self.comp + n.comp
#         result = complex(real, comp)
#         return result
    
# x1 = Comp_Number(1,2)
# x2 = Comp_Number(10,20)
# print("\n",x1.add_num(x2))


# Creating a Class for Mirocwave

class Microwave:
    
    def __init__(self,brand, power_rating):
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on = False
    
    def turn_on(self):
        if self.turned_on == True:
            print(f"The microwave {self.brand} is alredy turned on")

        else:
            self.turned_on = True
            print(f"The microwave {self.brand} is now turned on")

    def turn_off(self):
        if self.turned_on == True:
            self.turned_on = False
            print(f"The microwave {self.brand} is now turned off")
        else:
            print(f"The microwave {self.brand} is already turned off")

    def run(self, seconds):
        if self.turned_on == True:
            print(f"Running the microwave {self.brand} for {seconds} seconds")
        else:
            print(f"Please turn on the microwave {self.brand} to run")

    # Dunder methods
    def __add__(self, other):
        return (f"{self.brand} + {other.brand}")


samsung = Microwave("Samsung", "B")
bosch = Microwave("Bosch", "A")

print(samsung + bosch)


# smg.turn_on()
# smg.turn_on()
# smg.run(30)
# smg.turn_off()
# smg.run(10)

        

        



    
            
        
    
    



