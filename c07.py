list=[4,7,3,78,46,50,42]
list1=[78,50,3,68,65,42,7]
s=int(0)
c=int(0)
if len(list)==len(list1):
    print("same length")
else:
    print("different length")
for i in range(0,len(list) and len(list1)):
    s=s+list[i]
    c=c+list1[i]
if(s==c):
    print("equal sum")
else:
     print("not same sum")
print("elements in same:")     
l=[]
for i in range(0,len(list)):
    for j in range(0,len(list1)):
        if list[i]==list1[j]:
             l.append(list[i] and list1[j])
    else:
        continue
print(l)
          