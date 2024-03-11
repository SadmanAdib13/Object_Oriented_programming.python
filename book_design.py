class book:
    def __init__(self,book_name,author):
        self.name=book_name
        self.author=author
        self.price=0
    def set_price(self,price):
        self.price=price
    def get_price(self):
        return self.price
    def detail(self,):
        print("Book Name:",self.name,"\nAuthor Name:",self.author,"\nPrice",self.price)


#___________________________________________________________________________________________________


"""b1=book("Amar Chelebela","Humayun Ahmed")
b1.detail()
b1.set_price(200)
x=b1.get_price()
print("The price of the book is "+str(x))
b1.detail()"""
