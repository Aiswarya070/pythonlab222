class time:
    def __init__(self):
        self.__hr=int(input("enter time in  hour:"))
        self.__m=int(input("enter time minute:"))
        self.__s=int(input("enter seconds:"))
    def __add__(self,obj2):
         hours=self.__hr+obj2.__hr
         print("sum of hours",hours)
         minutes=self.__m+obj2.__m
         print("sum of minutes",minutes)
         seconds=self.__s+obj2.__s
         print("sum of seconds",seconds)
         if minutes>=60:
             hours=hours+1
             minutes=minutes-60
         if seconds>=60:
             minutes=minutes+1
             seconds=seconds-60
         return hours,minutes,seconds
obj1=time()
obj2=time()
print("Enter the Time of first object:",obj1+obj2)






        
             
     
        
        
    