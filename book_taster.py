import book_design
b1=book_design.book("Amar Chelebela","Humayun Ahmed")
b1.detail()
b1.set_price(200)
x=b1.get_price()
print("The price of the book is "+str(x))
b1.detail()