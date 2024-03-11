class animal:
    def __init__(self,name):
        self.name=name
    def specis(self):
        print("I have a ",self.name)
    def eat(self,food):
        self.food=food
        print(self.name,"eats",self.food,"everyday.")

class dog(animal):
    def nam(self):
        print("His name is",self.name,".")

a1=animal("cat")
a1.name="Dog"
a1.specis()
a1.eat("meat")
d1=dog("lufy")
d1.nam()