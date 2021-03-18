def add(a,b):
    return (a+b)

def sub(a,b):
    return abs(a-b)

def mul(a,b):
    return (a*b)

def div(a,b):
    return (a/b)

print("This is a calculator application")
n=0
while (True):
    print("Options:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    n=int(input("Enter your choice: "))
    if (n==5):
        break
    if (n<1 or n>5):
        print("Enter correct choice!\n")
    else:
        n1=int(input("Enter first number: "))
        n2=int(input("Enter second number: "))
        r=0
        if (n==1):
            r=add(n1,n2)
        elif (n==2):
            r=sub(n1,n2)
        elif (n==3):
            r=mul(n1,n2)
        elif (n==4 and n2!=0):
            r=div(n1,n2)
        if (n==4 and n2==0):
            print("Division by zero is not possible!\n")
        else:
            print("Result = ",r)
            print()
print("Thanks for using the application!")
