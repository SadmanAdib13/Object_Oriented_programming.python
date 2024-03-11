class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def eat(self):
        print(self.color,self.name,"is eating.")
    def compare(self,c):
        if self.color==c.color:
            print("Both animals are same.")
        else:
            print("They are not the  same.")


a1=Animal("Dog","white")
a2=Animal("cat","black")
a1.eat()
a2.eat()
a1.compare(a2)


