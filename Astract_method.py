from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def method_1(self):
        print("Method_1 is working.")
class B(A):
    def method_1(self):
        print("Method_1 is working.")
    def method_2(self):
        print("Method_2 is working.")
class C(B):
    def method_1(self):
        print("Method_1 is working.")
    def method_2(self):
        print("Method_2 is working.")
    def method_3(self):j
        print("Method_3 is working.")
m1=C()

