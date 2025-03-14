"""
1_inheritance.py

This file demonstrates the concept of inheritance in Python.
It shows how a child class can inherit properties and methods from a parent class.
"""

class Animal:
    """
    Base class for all animals. Defines common properties and behaviors.
    """
    def __init__(self, name, number_of_feet):
        """
        Constructor method for the Animal class.

        #__init__ : 
        The __init__ method is called when an instance of the class is created.
        It initializes the object's attributes with the values provided during instantiation.
        These attributes are specific to the instance (object) and can be modified later.

        Example:
        pegasus_animal = Animal('Pegasus', 4)
        Here, 'Pegasus' and 4 are the name and number_of_feet attributes of the pegasus_animal object.
        These attributes are assigned to the object during runtime.
        
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
    
    def make_sound(self):
        """
        Represents the sound a dog makes.
        
        :return: Sound of the dog (str)
        """
        return "Woof woof!"


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
    
    def make_sound(self):
        """
        Represents the sound a cat makes.
        
        :return: Sound of the cat (str)
        """
        return "Meow meow!"


class Bird(Animal):
    """
    Bird class, inherits from the Animal class.
    """
    def __init__(self, name):
        """
        Constructor method for the Bird class.
        
        :param name: Name of the bird
        """
        super().__init__(name, number_of_feet=2)
    
    def make_sound(self):
        """
        Represents the sound a bird makes.
        
        :return: Sound of the bird (str)
        """
        return "Chirp chirp!"


# Usage
dog = Dog('Rocky')
cat = Cat('Fluffy')
bird = Bird('Blue')
pegasus_animal = Animal('Pegasus', 4)

print(f'{dog.name} : {dog.make_sound()}')
print(f'{dog.name} number of feet: {dog.number_of_feet}')
print(f'{cat.name} : {cat.make_sound()}')
print(f'{cat.name} number of feet: {cat.number_of_feet}')
print(f'{bird.name} : {bird.make_sound()}')
print(f'{bird.name} number of feet: {bird.number_of_feet}')
print(f'{pegasus_animal.name} : {pegasus_animal.make_sound()}')
print(f'{pegasus_animal.name} number of feet: {pegasus_animal.number_of_feet}')

# 1_inheritance.py outputs:

#Rocky : Woof woof!
#Rocky number of feet: 4
#Fluffy : Meow meow!
#Fluffy number of feet: 4
#Blue : Chirp chirp!
#Blue number of feet: 2
#Pegasus : Animal is making a noise.
#Pegasus number of feet: 4
