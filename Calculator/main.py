def get_number():
    while True:
        num = input("Enter a number: ")
        if num.isdigit():
            num = int(num)
            break
        else:
            print("Not a valid number!")
    return num

def check_valid_operator(operator):
    if operator == "*" or operator == "/" or operator == "+" or operator == "-" or operator == "quit":
        return True
    return False

def main():
    x = get_number()
    while True:
        while True:
            operator = input("Enter an operator (* / + -) or type \'quit\': ")
            if check_valid_operator(operator):
                break
            print("Operation unrecognised. Operator does not exist...")
            
        if operator == "quit":
            break
        y = get_number()
        
        if operator == "*":
            print(f"multiplying {x} and {y}...")
            x = x * y
        elif operator == "/":
            print(f"dividing {x} and {y}...")
            try:
                x = round(x / y, 2)
            except ZeroDivisionError:
                print("Division failed. Cannot divide by 0...")
        elif operator == "+":
            print(f"adding {x} and {y}...")
            x = x + y
        elif operator == "-":
            print(f"subtracting {x} and {y}...")
            x = x - y
            
        print("---------------RESULT-----------------")
        print(x)

if __name__ == "__main__":
    main()

