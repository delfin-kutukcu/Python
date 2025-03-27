"""
4_Polymorphism.py

This file demonstrates the concept of polymorphism in Python.
Polymorphism allows objects of different classes to be treated as objects of a common superclass.
It enables methods to behave differently based on the object that calls them.
"""

# Base class
class Animal:
    """
    Base class for all animals. Defines common interface for animal behaviors.
    """
    def __init__(self, name):
        """
        Constructor method for the Animal class.
        
        :param name: Name of the animal
        """
        self.name = name
    
    def make_sound(self):
        """
        Abstract method meant to be overridden by subclasses.
        
        :return: Sound of the animal (str)
        """
        raise NotImplementedError("Subclasses must implement this method")

# Subclass implementations
class Dog(Animal):
    """
    Dog class that implements the Animal interface.
    """
    def make_sound(self):
        """
        Concrete implementation of make_sound for Dog.
        
        :return: Dog's sound (str)
        """
        return "Woof woof!"

class Cat(Animal):
    """
    Cat class that implements the Animal interface.
    """
    def make_sound(self):
        """
        Concrete implementation of make_sound for Cat.
        
        :return: Cat's sound (str)
        """
        return "Meow meow!"

class Bird(Animal):
    """
    Bird class that implements the Animal interface.
    """
    def make_sound(self):
        """
        Concrete implementation of make_sound for Bird.
        
        :return: Bird's sound (str)
        """
        return "Chirp chirp!"

# Function demonstrating polymorphism
def animal_sounds(animals):
    """
    Accepts a list of Animal objects and calls their make_sound methods.
    This function demonstrates polymorphism by working with any Animal subclass.
    
    :param animals: List of Animal objects
    """
    for animal in animals:
        print(f"{animal.name}: {animal.make_sound()}")

# Duck typing example (another form of polymorphism)
class Car:
    """
    A class that isn't an Animal but has a similar interface.
    Demonstrates duck typing - "if it quacks like a duck, it's a duck".
    """
    def __init__(self, model):
        self.name = model
    
    def make_sound(self):
        return "Vroom vroom!"

# Usage
if __name__ == "__main__":
    # Create instances of different animals
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    bird = Bird("Tweety")
    
    # Polymorphism in action - all treated as Animal objects
    animals = [dog, cat, bird]
    animal_sounds(animals)
    
    # Duck typing example
    car = Car("Mustang")
    print(f"\n{car.name}: {car.make_sound()}")
    
    # This works because Car has the expected interface (make_sound method)
    print("\nDuck typing example:")
    animal_sounds([dog, car, bird])

# Expected Output:
# Buddy: Woof woof!
# Whiskers: Meow meow!
# Tweety: Chirp chirp!
#
# Mustang: Vroom vroom!
#
# Duck typing example:
# Buddy: Woof woof!
# Mustang: Vroom vroom!
# Tweety: Chirp chirp!