class Rectangle:
    def __init__(self):
        self.__l=int(input("enter the length of rectangle:"))
        self.__w=int(input("enter the width of rectangle:"))
    def __lt__(self,obj2):
        area1=self.__l*self.__w
        area2=obj2.__l*obj2.__w
        print("area of rectangle1 is:",area1)
        print("area of rectangle2 is:",area2)
        return area1<area2
print("enter the length and width of first object:")
obj1=Rectangle()
print("enter the length and width of second object:",)
obj2=Rectangle()
if obj1<obj2:
    print("obj1<obj2")
else:
    print("obj1>obj2")
       
        