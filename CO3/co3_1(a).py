import random
Mylist=['Ammu','Ben','Ciril','Malu','Domenic']
print(random.choice(Mylist))
print(random.choices(Mylist,k=4))
print(random.sample(Mylist,k=1))
random.shuffle(Mylist)
print(Mylist)
print(random.randrange(3,9))