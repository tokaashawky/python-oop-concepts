# Python-OOP-Concepts

# Composition Concept in Python

Composition is an object-oriented programming concept where one class contains an instance of another class as a field. This allows for code reusability and better modularity.

In this example, we demonstrate composition by creating an Engine class and a Car class. The Car class has an Engine object as an attribute, illustrating a "has-a" relationship.

**Code Explanation**

**Engine Class**

Represents a car engine with attributes for fuel_type and horsepower.

Implements the __str__ method to return a readable string representation.

**Car Class**

Represents a car with attributes make, model, year, and an Engine object.

Implements a display_info method to return the car details, including its engine specifications.


# DataClass in Python

A dataclass in Python is a decorator (@dataclass) that simplifies class creation by automatically generating special methods like __init__, __repr__, and __eq__. It reduces boilerplate code and provides built-in immutability (optional with frozen=True).


# Multiple Inheritance & MRO (Method Resolution Order)

Multiple inheritance allows a class to inherit from more than one parent class. MRO determines the order in which classes are searched for methods or attributes. Python uses the C3 linearization (MRO) to resolve conflicts and ensure a consistent order. You can check MRO using ClassName.__mro__ or help(ClassName).

# Dictionary Comprehension Example

Dictionary comprehension provides a concise way to create dictionaries.

Example

squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
