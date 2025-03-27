"""
5_Abstraction.py

This file demonstrates the concept of abstraction in Python.
Abstraction focuses on hiding complex implementation details and showing only essential features.
In Python, we achieve this using abstract base classes (ABC) from the abc module.
"""

from abc import ABC, abstractmethod

# Abstract Base Class
class Animal(ABC):
    """
    Abstract class representing an Animal.
    Cannot be instantiated directly - must be subclassed.
    """
    
    def __init__(self, name):
        """
        Constructor for Animal class.
        
        :param name: Name of the animal
        """
        self.name = name
        super().__init__()
    
    @abstractmethod
    def make_sound(self):
        """
        Abstract method that must be implemented by subclasses.
        Represents the sound the animal makes.
        """
        pass
    
    @abstractmethod
    def move(self):
        """
        Abstract method for movement behavior.
        """
        pass
    
    def describe(self):
        """
        Concrete method that uses abstract methods.
        Shows how abstraction hides implementation details.
        """
        return f"{self.name} says {self.make_sound()} while {self.move()}"

# Concrete Implementation
class Dog(Animal):
    """
    Concrete implementation of Animal for dogs.
    Must implement all abstract methods.
    """
    
    def make_sound(self):
        """
        Implementation of abstract method.
        
        :return: Dog's sound (str)
        """
        return "Woof!"
    
    def move(self):
        """
        Implementation of abstract method.
        
        :return: Dog's movement (str)
        """
        return "running on four legs"

class Bird(Animal):
    """
    Concrete implementation of Animal for birds.
    """
    
    def make_sound(self):
        """
        Implementation of abstract method.
        
        :return: Bird's sound (str)
        """
        return "Chirp!"
    
    def move(self):
        """
        Implementation of abstract method.
        
        :return: Bird's movement (str)
        """
        return "flying in the sky"

# Attempting to instantiate abstract class (will raise error)
try:
    animal = Animal("Generic")
except TypeError as e:
    print(f"Error when instantiating Animal: {e}\n")

# Usage
if __name__ == "__main__":
    # Creating concrete instances
    dog = Dog("Buddy")
    bird = Bird("Tweety")
    
    # Using abstract interface
    print(dog.describe())
    print(bird.describe())
    
    # Demonstrating polymorphism through abstraction
    animals = [dog, bird]
    for animal in animals:
        print(f"{animal.name} makes sound: {animal.make_sound()}")

# Expected Output:
# Error when instantiating Animal: Can't instantiate abstract class Animal with abstract methods make_sound, move
#
# Buddy says Woof! while running on four legs
# Tweety says Chirp! while flying in the sky
# Buddy makes sound: Woof!
# Tweety makes sound: Chirp!