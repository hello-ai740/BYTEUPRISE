def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def division(num1,num2):
    
    if num2!=0:
        return num1/num2
    else:
        return "error:division by zero"

print("select operation")   
print("select operation")
print("1.Addition")
print("2.subtract")
print("3.multiply")
print("4.divide")

operator = input("Enter your operator choice: ")

if operator in['1','2','3','4']:
    num1 =int(input("Enter the first number: "))
    
    num2 =int(input("Enter the second number: "))
    

    if operator == "1":
        print(num1+num2);

    elif operator == "2":
        print(num1-num2);

    elif operator == "3":
        print(num1*num2);

    elif operator == "4":
        print(num1/num2);

    else :
        print("invalid");
else:
    print("Invalid Operation Entered")           

    

