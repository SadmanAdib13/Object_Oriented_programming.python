class A:
    def __init__(self):
        pass
    def study(self):
        print("Always study.")
    def property(self):
        print("Get all of the property.")
class B(A):
    def __init__(self):
        pass

    def chill(self):
        print("Always chill.")

    def property(self):
        super().property()
        print("I will get no property.")
    def study(self):
        super().study()
        print("I will study a little")

m1=B()
m1.study()
m1.property()