class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
    
    def product_info(self):
        print('\nProduct Information:')
        print('⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
        print(f'Name: {self.name}')
        print(f'Price: ${self.price}')
        print(f'Product ID: {self.product_id}')

class Book(Product):    #---subclass
    def __init__(self, product_id, name, price, author):    #---sets everything that will be used in this subclass
        super().__init__(product_id, name, price)   #---borrows/inherits these initiated objects from Product
        self.author = author    #---adds the additional object of 'author', unique to he 'Book' subclass

    def product_info(self):
        super().product_info()  #--- Calls the existing product_info setup
        print(f'Author: {self.author}') #---only when calling the subclass Book will we be able to use the author category

tool = Product('0431F', 'Emergency Flaslight', 13)
tool.product_info()

book = Book('9945B', 'Catcher In The Rye', 11, 'J.D Salinger')
book.product_info()