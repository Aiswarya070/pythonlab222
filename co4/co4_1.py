class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b  
    def get_perimeter(self,p):
        return 2*(self.l+self.b)
    def get_area(self):
        return self.l*self.b
    def compare(self,x):
        try:
            if obj1.get_area()==obj2.get_area():
                print("Both areas are equal")
            elif obj1.get_area() > obj2.get_area():
                print("Area of rectangle obj1 is greater:")
            else:
                print("Area of rectangle obj1 is lower:")
        except:
            print("Objects cannot be comparable")
   
l1=int(input("Enter the first length of Rect1:"))
b1=int(input("Enter the first breadth of Rect1:"))
l2=int(input("Enter the second length of Rect2:"))
b2=int(input("Enter the second breadth of Rect2:"))
obj1=rectangle(l1,b1)
obj2=rectangle(l2,b2)
obj1.compare(obj2)
