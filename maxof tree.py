def max(num1,num2,num3):
    if num1 > num2:
        if num1 > num3:
            print(num1,"is max")
        else:
            print(num3,"is max")
    elif num2 > num3:
        print(num2,"is max")
    else:
        print(num3,"is max")

n1=int(input("please enter your first number="))
n2=int(input("please enter your second number="))
n3=int(input("please enter your second number="))
max(n1,n2,n3)
