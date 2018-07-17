class Animals: 
    def eat(self): 
        print("I can eat")
    def talk(self): 
        print("I can talk")


class Cat(Animals): 
    def talk(self): 
        print("I can meow")
    
    def move(self):
        print("I can move")

muffin = Cat() 

muffin.talk()

