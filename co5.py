n=int(input("enter the number of elements:"))
list2=[]
for i in range(n):
    number=int(input("enter the number:"))
if number>=100:
        list2.append('over')
else:
     list2.append(number)
print("the output is:",list2)        
