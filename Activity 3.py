print("Enter  marks obtained in 5 subjects....")
marks1=int(input())
marks2=int(input())
marks3=int(input())
marks4=int(input())
marks5=int(input())

tot=marks1+marks2+marks3+marks4+marks5
avg=tot/5 

if avg>=91 and avg<=100:
    print("your grade is O+")
elif avg>=81 and avg<=91:
    print("your grade is A++")
elif avg>=71 and avg<=81:
    print("your grade  A+")
elif avg>=61 and avg<=71:
    print("your grade  A")
elif avg>=51 and avg<=61:
    print("your grade  B+")
elif avg>=41 and avg<=51:
    print("your grade  B")
elif avg>=31 and avg<=41:
    print("your grade  C+")
elif avg>=21 and avg<=31:
    print("your grade  C")
elif avg>=11 and avg<=21:
    print("your grade  C")
elif avg>=6 and avg<=11:
    print("your grade  D+")
elif avg>=0 and avg<=6:
    print("your grade  D")
else:
    print(" 404!! ERROR INVAILD INPUT PAGE NOT FOUND")
    

