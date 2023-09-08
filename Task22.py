#Calculator
print("Calculator CODSOFT")
print("Enter a Number :")
n1=float(input())
print("Enter another Number :")
n2=float(input())


print()
while True:
    op = input("Enter Operator (+,-,*,/,%,e(exit)) : ")
    print()

    match op:
    
        case '+':
      
            result=n1+n2
            print("Addition is :",n1, "+" ,n2,"=", result)
            print()

        case '-':
            result=n1-n2
            print("Subtraction is :",n1, "+" ,n2,"=", result)
            print()
        
        case '*':
            result=n1*n2
            print("Multiplication is :",n1, "+" ,n2,"=", result)
            #print("Enter e to Exit")
            print()

        case '/':
            result=n1/n2
            print("Division is :",n1, "+" ,n2,"=", result)
            #print("Enter e to Exit")
            print()

        case '%':
            result=n1%n2
            print("Modulus is :",n1, "+" ,n2,"=", result)
            #print("Enter e to Exit")
            print()

        case "e":
            break
