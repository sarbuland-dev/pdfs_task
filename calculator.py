def sum(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def divion(a,b):
    return a/b

print("1:add\n2:subtraction\n3:multiplication\n4:divion")
while True:
    choice=int(input("enter your choice "))
    if choice>=1 and choice<=4:
        break
    else:
        print("invaild selection of option  ")

num1=float(input("enter your first number  "))
num2=float(input("enter your second number  "))
if choice==1:
    print(num1,"+",num2,"=",sum(num1,num2))
elif choice==2:
    print(num1,"-",num2,"=",subtraction(num1,num2))
elif choice==3:
    print(num1,"X",num2,"=",multiplication(num1,num2))
elif choice==4:
    print(num1,"/",num2,"=",divion(num1,num2))
