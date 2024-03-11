class car:
    def __init__(self,name,year):
        self.name=name
        self.year=year
        self.wheles="Four"
    def view(self):
        print("Car name:",self.name,".Car year:",self.year)
        print("it is a ",self.wheles,"wheled car.")
c1=car("Audi",2015)
c2=car("BMW",2011)
c2.name="Mustang"
c1.view()
c2.view()

