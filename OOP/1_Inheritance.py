"""
1_Inheritance.py

This file demonstrates the concept of inheritance in Python.
It explains multiple inheritance and the built-in `object` class.
"""

# The base class from which all other classes inherit
class Animal:
    """
    Base class for all animals. Defines common properties and behaviors.
    """
    def __init__(self, name, number_of_feet):
        """
        Constructor method for the Animal class.

        #***************************************

        #__init__ :
        The __init__ method is called when an instance of the class is created.
        It initializes the object's attributes with the values provided during instantiation.
        These attributes are specific to the instance (object) and can be modified later.


        Example:
        pegasus_animal = Animal('Pegasus', 4)
        Here, 'Pegasus' and 4 are the name and number_of_feet attributes of the pegasus_animal object.
        These attributes are assigned to the object during runtime.

        #*****************************************
        
        :param name: Name of the animal
        :param number_of_feet: Number of feet the animal has
        """
        self.name = name
        self.number_of_feet = number_of_feet    
    
    def make_sound(self):
        """
        Represents the sound the animal makes.
        
        :return: Sound of the animal (str)
        """
        return "Animal is making a noise."

# The Dog class inherits from the Animal class
class Dog(Animal):
    """
    Dog class, inherits from the Animal class.
    """
    def __init__(self, name):
        """
        Constructor method for the Dog class.
        
        :param name: Name of the dog
        """
        super().__init__(name, number_of_feet=4)


# The Cat class inherits from the Animal class
class Cat(Animal):
    """
    Cat class, inherits from the Animal class.
    """
    def __init__(self, name):
        """
        Constructor method for the Cat class.
        
        :param name: Name of the cat
        """
        super().__init__(name, number_of_feet=4)
    
# Multiple Inheritance Example
class Walker:
    """
    A separate class that represents walking behavior.
    """
    def walk(self):
        return "This animal can walk!"

# The Bird class now inherits from both Animal and Walker (Multiple Inheritance)
class Bird(Animal, Walker):
    """
    Bird class, inherits from both Animal and Walker classes.
    Demonstrates multiple inheritance in Python.
    """
    def __init__(self, name):
        """
        Constructor method for the Bird class.
        
        :param name: Name of the bird
        """
        super().__init__(name, number_of_feet=2)
    

# Understanding Built-in Inheritance
class CustomObject:
    """
    This class implicitly inherits from Python’s built-in `object` class.
    In Python, all classes inherit from `object`, which provides built-in methods like `__str__`, `__repr__`, etc.
    """
    pass

# Usage
dog = Dog('Cakil')
cat = Cat('Boncuk')
bird = Bird('Mavis')
pegasus_animal = Animal('Pegasus', 4)


print(f'{dog.name} number of feet: {dog.number_of_feet}')
print(f'{dog.name} : {dog.make_sound()}')
print(f'{cat.name} number of feet: {cat.number_of_feet}')
print(f'{cat.name} : {cat.make_sound()}')
print(f'{bird.name} number of feet: {bird.number_of_feet}')
print(f'{bird.name} : {bird.make_sound()}')
print(bird.walk())
print(f'{pegasus_animal.name} number of feet: {pegasus_animal.number_of_feet}')
print(f'{pegasus_animal.name} : {pegasus_animal.make_sound()}')

# Expected Output:
# Cakil number of feet: 4
# Cakil : Animal is making a noise.
# Boncuk number of feet: 4
# Boncuk : Animal is making a noise.
# Mavis number of feet: 2
# Mavis : Animal is making a noise.
# This animal can walk!
# Pegasus number of feet: 4
# Pegasus : Animal is making a noise.
