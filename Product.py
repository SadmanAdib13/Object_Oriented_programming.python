class calculation:
    def product(self,num1,num2=None,num3=None):
        if num1!=None and num2!=None and num3!=None:
            print("Sum=",num1*num2*num3)
        elif num1!=None and num2!=None:
            print("Sum=",num1*num2)
        else:
            print("Sum=",num1*1)
c1=calculation()
c1.product(1,2)
c1.product(1)
c1.product(1,2,3)

#___________________________________________________________________________________________________________________


class calculation:
    def product(self,*num):
        sum=1

        print(num)
        for i in num:
            sum=sum*i
        print(sum)
c1=calculation()
c1.product(1,2,3,4,5,6,7,8)

#_________________________________________________________________________________________________________________________

from multipledispatch import dispatch
class calculation :
    @dispatch(int,int,int)
    def product(self,one,two,three):
        print("Product=",one*two*three)
    @dispatch(int,int)
    def product(self,one,two):
        print("product=",one*two)
    @dispatch(int)
    def product9(self,one):
        print(one)
    @dispatch(str,int)
    def product(self,one,two):
        print("product=",int(one)*two)
s1=calculation()
s1.product(1,2,3)
s1.product("4",4)






'''def num (one,two=None,three=None):
    print(one,two,three)
num(1,2,3,)'''
