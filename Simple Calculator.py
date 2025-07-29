def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter the operator (+,-,*,/): ")
    num2 = float(input("Enter second number: "))
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Cannot divide by zero.")
            
    else:
        print("Invalid operator.")
        
        
    if result == int(result):
        print("Result: ",int(result))
    else:
        print("Result: ",result)
        
calculator()