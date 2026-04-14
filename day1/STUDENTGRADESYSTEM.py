print("HI")
mark1=int(input("enter your mark1"))
mark2=int(input("enter your mark2"))
mark3=int(input("enter your mark3"))
total=mark1+mark2+mark3
avg=total/3
print("total marks obtained",total)
print("average of student",avg)
if(avg>=90):
    print("GRADE OBTAINED IS A")
elif(avg>=75):
    print("GRADE OBTAINED IS B")
elif(avg>=50):
    print("GRADE OBTAINED IS C")
else:
    print("FAIL")
