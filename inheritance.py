#Parent class/Super class/Base class
class Animal:
    def speak(self):
        print("Animal is speaking")

#Child Class/Sub class/DErived class
class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

class Dog(Cat):
    def bark(self):
        print("Dog is barking")

a = Animal()
c = Cat()
c.speak()
d = Dog()
d.speak()

