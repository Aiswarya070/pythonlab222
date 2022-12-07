l=int(input("enter the lenth of the rectangle:"))
b=int(input("enter the breadth of the rectangle:"))
h=int(input("enter the height of the triangle:"))
ar=lambda x,y:x*y
asq=lambda x:x*x
at=lambda x,y:0.5*x*y
print("area of rectangle:",ar(l,b))
print("area of square:",asq(l))
print("area of triangle:",at(b,h))