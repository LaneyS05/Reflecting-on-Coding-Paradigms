# Functional
def flatten_and_sort(arr):
    def flatten(lst):
        return [item for sublist in lst for item in (flatten(sublist) if isinstance(sublist, list) else [sublist])]

    return sorted(flatten(arr))

print(flatten_and_sort([[1, 5, 8, 9, 4, 7]]))

#1 

#2 yes it is pure function because arr never changes its value 

#3 no it is not a higher-order function because It takes only one argument.

#4 not sure

#5  provides a way to solve problems involving nested data structures like nested lists


#Object Oriented 

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        if self.condition == 'trashed':
            print("has been repaired")
        else:
            print("looking good")

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def boost(self): 
        self.max_speed *= 2  
        print("this is were the fun Begins")

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self, other):
        if isinstance(other, Podracer):
            other.condition = 'trashed'
            print("crashed")
        else:
            print("Invalid target for flame jet")



podracer1 = Podracer(500, 'perfect', 10000)
podracer2 = Podracer(400, 'trashed', 5000)
podracer3 = AnakinsPod(800, 'perfect', 0)
podracer4 = SebulbasPod(700, 'perfect', 12000)
podracer4.flame_jet(podracer1)
podracer3.boost()
podracer1.repair()
podracer2.repair()

"""
#1 Encapsulation: max_speed, condition, and price are encapsulated within the class
Abstraction: Podracer class does not need to know the internal details of how the class is implemented
Inheritance: AnakinsPod and SebulbasPod inherit from the Podracer class
Polymorphism: flame_jet method takes an argument other, which can be any object that is an instance of the Podracer 
"""

#2 do not know

#3 like mentioned above it uses all of the 4 pillars of OOP


#Reflection

"""
I personly like OOP better because we can use objects instead of 
using a bunch variables that makes our code longer.
I also prefer this way because OOP makes the code more reusable ans flexable.
"""

"""
functional programming
   function purity
   declarative programing
   high-order function
"""

# Object Oriented Programming 4 pillars

"""
for me OOP is a little harder but im getting there
after some more practice I shoild understand more.