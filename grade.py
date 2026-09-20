grade = int(input("What is your score: "))

if grade>=90:
    print("your grade is A")

elif grade>=80 and grade<=90:
     print("your grade is B")

elif grade>=70 and grade<=80:
     print("Your grade is c")

elif grade>=60 and grade<=70:
     print("Your grade is d")

elif grade<=60:
     print("Your need to study more")

else:
     print("error")