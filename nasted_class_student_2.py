class student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def detail(self):
        print("Name:",self.name,"\nId:",self.id)

#-----------------------------------------------------------------
class cse_student(student):
    def __init__(self,name,id,labs):
        super().__init__(name,id)
        self.lab=labs
    def cry(self):
        print("CSE students are crying because of ",self.lab,"lab classes.")

#---------------------------------------------------------------------------------

class cse_fresher(cse_student):
    def course(self):
        print(self.name,"enrolled CSE 110.")

s1=cse_student("Adib",234,6)
s2=cse_fresher("Bob",44,1)
s1.detail()
s1.cry()
s2.detail()
s2.course()
s2.cry()

