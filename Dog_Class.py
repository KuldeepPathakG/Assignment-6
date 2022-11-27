class Dog:
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
    
    def description(self):
        return "Hi This Dog's Name is {}".format(self.name) + " and Age is {}".format(self.age)
    
    def get_info(self):
        return "Dog's color is {}".format(self.color)
    
animal=Dog("German_Shephard",11,"Brown")
print(animal.description())
print(animal.get_info())



class JackRussellTerrier(Dog):
    def demo1(self,speed):
        self.speed=speed
        return "{} has {} color, and it runs {} km per hour".format(self.name,self.color,self.speed)
    
class Bulldog(Dog):
    def demo2(self,speed):
        self.speed=speed
        return "{} has {} color, and it runs {} km per hour".format(self.name,self.color,self.speed)
    
obj1=JackRussellTerrier("JackRussellTerrier",7,"White")
print(obj1.demo1(70))
obj2=Bulldog("Bulldog",10,"Grey")
print(obj2.demo2(60))
