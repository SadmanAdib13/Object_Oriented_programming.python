class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
         print("Hello",self.name,".","He is ",self.age,"years old.")
    def detail(self):
         print("Name:",self.name,". Age:",self.age)
student1=student("Rakib",11)
student2=student("Raju",11)
student1.age=99
student1.display()
student2.display()
student1.detail()
student2.detail()
print(student1.name)
print(student1.age)