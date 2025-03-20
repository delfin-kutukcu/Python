"""
2_Method_Overriding.py

This file demonstrates method overriding in Python.
Method overriding allows a subclass to provide a specific implementation
of a method already defined in its parent class.
"""

# Base class
class Animal:
    """
    Base class for all animals. Defines common properties and behaviors.
    """
    def __init__(self, name, number_of_feet):
        """
        Constructor method for the Animal class.
        
        :param name: Name of the animal
        :param number_of_feet: Number of feet the animal has
        """
        self.name = name
        self.number_of_feet = number_of_feet    
    
    def make_sound(self):
        """
        Default sound method, meant to be overridden in subclasses.
        
        :return: Sound of the animal (str)
        """
        return "Animal is making a noise."

# Subclass with method overriding
class Dog(Animal):
    """
    Dog class, inherits from the Animal class.
    Demonstrates method overriding.
    """
    def __init__(self, name):
        """
        Constructor method for the Dog class.
        
        :param name: Name of the dog
        """
        super().__init__(name, number_of_feet=4)
    
    def make_sound(self):
        """
        Overriding the make_sound method of the Animal class.
        
        :return: Sound of the dog (str)
        """
        return "Woof woof!"

# Another subclass with method overriding
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
        Overriding the make_sound method of the Animal class.
        
        :return: Sound of the cat (str)
        """
        return "Meow meow!"
class MuteAnimal(Animal):
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
        pass
    """ 'pass' is a placeholder statement in Python that does nothing when executed.
        It is used when a statement is syntactically required but no action is needed.
        Typically, it is used for defining empty functions, classes, or loops that will be implemented later.
        # Since `make_sound` is overridden in the Dog class with `pass`, 
        # it does not return anything, which results in `None` when printed.

    """


# Usage
dog = Dog('Rocky')
cat = Cat('Fluffy')
mute_animal = MuteAnimal('Mute')
pegasus_animal = Animal('Pegasus', 4)
print(f'{dog.name} : {dog.make_sound()}')
print(f'{cat.name} : {cat.make_sound()}')
print(f'{mute_animal.name} : {mute_animal.make_sound()}')
print(f'{pegasus_animal.name} : {pegasus_animal.make_sound()}')

# Expected Output:
# Rocky : Woof woof!
# Fluffy : Meow meow!
# Mute : None
# Pegasus : Animal is making a noise.