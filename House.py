class house:
    def __init__(self):
        self.door=2
        self.window=4
    def view(self):
        print("Window:",self.window,"Door:",self.door)
house1=house()
house2=house()
house1.window=5
house2.door=5
house1.view()
house2.view()
