class dog:
    def __init__(self,name,color):
        self.color=color
        self.name=name
    def update_color(self,color):
        self.color=color
    def show(self):
        print('The',self.color,'colored dog named',self.name,"is baking.")
d1=dog("Jack","black")
d2=dog("Tom","red")
d1.update_color("white")
d1.show()
d2.show()
print(dir(d1))
print(d1.__dict__)