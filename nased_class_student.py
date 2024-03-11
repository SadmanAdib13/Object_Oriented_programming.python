class student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def detail(self):
        print("Name:",self.name,"\nID:",self.id)

class cse_students(student):
    def __init__(self,name,id,labs):
        super().__init__(name,id)
        self.labs=labs
         #super().__init__(self) is used to send the arguments or objects of the nasted class to the parent or main class which are not in
                                              #the nasted class'''
    def cry(self):
        print("Cse students are crying because of",self.labs," labs.")

class bba_student(student):
    def party(self):
        print("All day Party.")

s1=cse_students("Adib",123,4,)
s2=bba_student("Akib",456)
s1.detail()
s2.detail()
s1.cry()
s2.party()


