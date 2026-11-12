def calculator(num1,num2,operation):
    if operation.lower() == "add"or operation.lower() == "+":
        return num1 + num2
    elif operation.lower() == "sub" or operation.lower() == "-":
        return num1 - num2
    elif operation.lower() == "mul" or operation.lower() == "*":
        return num1 * num2 
    elif operation.lower() == "div" or operation.lower() == "/":
        if num2 != 0 :
            return num1 / num2
        else:
            return "divisibility Error"
        
    else :
        return "Invalid Operation"
    

print(calculator(1,2,"*"))