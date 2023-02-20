class publisher:
    def __init__(self,name):
        self.name=input("enter the name")
    def display(self):
       print("name of the publisher is:",self.name)
class book(publisher):
    def __init__(self,name,title,author):
        publisher.__init__(self,name)
        self
class python(book):
    def __init__(self,name,title,author,price,noofpages):
        book.__init__(self,name,title,author)
        self.price=price
        self.noofpages=noofpages
    def display(self):
        publisher.display(self)
s.display()