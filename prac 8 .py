# Semantic Network using Predicate Logic

# Base class: Animal
class Animal:
    def has_cells(self):
        return True


# Bird ISA Animal
class Bird(Animal):
    def can_fly(self):
        return True


# Dog ISA Animal
class Dog(Animal):
    def can_bark(self):
        return True


# Sparrow ISA Bird
class Sparrow(Bird):
    pass


# Creating objects
animal = Animal()
bird = Bird()
dog = Dog()
sparrow = Sparrow()


# Demonstrating inheritance (Inference)

print("Animal has cells:", animal.has_cells())

print("Bird has cells (inherited from Animal):", bird.has_cells())
print("Bird can fly:", bird.can_fly())

print("Dog has cells (inherited from Animal):", dog.has_cells())
print("Dog can bark:", dog.can_bark())

print("Sparrow has cells (inherited from Animal):", sparrow.has_cells())
print("Sparrow can fly (inherited from Bird):", sparrow.can_fly())