from art import logo
# addition

def add(n1,n2):
    """give arguments you will get addition"""
    return n1 + n2

def subtract(n1,n2):
    """give a arguments you will get subtraction"""
    return n1 - n2

# multiplecation

def multi(n1,n2):
    """give a arguments you will get multiplecation"""
    return n1 * n2


# division

def division(n1,n2):
    """give a arguments you will get division"""
    return n1 // n2

# creating a dict

operation = {
    "+": add,
    "-" : subtract,
    "*" : multi,
    "/" : division
}
def calculator():
    print(logo)
    num1 = float(input("What is your first number?: "))
    for symbol in operation:
        print(symbol)

    should_continue = True

    while should_continue == True:
        operation_symbol = input("pick a operation from the line above: ")
        num2 = float(input("What is your second number?: "))
        function = operation[operation_symbol]
        answer = function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        in_put = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") 

        if in_put == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()







