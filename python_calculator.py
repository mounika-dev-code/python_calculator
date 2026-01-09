
n1=float(input("Enter number1 : "))
n2=float(input("Enter number2 : "))
op =input("Enter the operator : ")
if op=='+':
    print("the result is : ",n1+n2)
elif op=='-':
    print("the result is : ",n1-n2)
elif op=='*':
    print("the result is : ",n1*n2)
elif op=='/':
    if n2!=0:
        print("the result is : ",n1/n2)
    else:
        print("Error: Division by zero is invalid")
else:
    print(" Opertor not supported")

