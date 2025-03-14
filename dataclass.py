from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p = Person("Alice", 25)
print(p)  # Person(name='Alice', age=25)