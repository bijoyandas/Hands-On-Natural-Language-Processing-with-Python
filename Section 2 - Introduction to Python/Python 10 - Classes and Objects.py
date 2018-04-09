# Introduction to Python

# Classes and Objects

# Simple Class
class Fish:
    def swim(self):
        print("Fish is swimming")
    def eat(self):
        print("Fish is eating")

fish = Fish()
fish.swim()
fish.eat()


# Overriding constructor
class Game:
    def __init__(self,name):
        self.name = name
    def start(self):
        print(self.name,"has started")
    def stop(self):
        print(self.name,"has stopped")
        
game = Game("Counter Strike")
game.start()
game.stop()