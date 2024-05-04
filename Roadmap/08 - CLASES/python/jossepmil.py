"""Ejercicios """

class Programador:

    surname: str = None

    def __init__(self, name: str, age: int, lenguajes: list) -> None:
        self.name = name
        self.age = age
        self.lenguajes = lenguajes

    def print(self):
        print(f"Nombre: {self.name}|Apellido: {self.surname}| Edad:{self.age} | Lenguajes:{self.lenguajes}")
        


my_programmer = Programador("Juan", 25, ["Python", "C++", "Java"])
my_programmer.print()
my_programmer.surname = "Perez"
my_programmer.print()
my_programmer.age = 26

Extra
LIFO

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()
        
    def count(self):
        return len(self.stack)
    
    def print(self):
        for item in reversed(self.stack):
            print(item)

my_stack = Stack()
my_stack.push(1)
my_stack.push("Emiliano")
my_stack.push("Ana")
my_stack.push("Tejo")
my_stack.push("Teuhorn")
print(my_stack.count())
print(my_stack.print())
my_stack.pop()
print(my_stack.print())
my_stack.pop()
print(my_stack.print())
my_stack.pop()


#FiFo
class queue:

    def __init__(queue):
        queue.queue = []

    def equeue(self, item):
        self.queue.append(item)
        
    def deequeue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)
        
    def count(self):
        return len(self.queue)
    
    def print(self):
        for item in reversed(self.queue):
            print(item)

my_queue = queue()
my_queue.equeue(1)
my_queue.equeue("Emiliano")
my_queue.equeue("Ana")
my_queue.equeue("Tejo")
my_queue.equeue("Teuhorn")
print(my_queue.count())
print(my_queue.print())
my_queue.deequeue()
print(my_queue.print())
my_queue.deequeue()
print(my_queue.print())
my_queue.deequeue()
