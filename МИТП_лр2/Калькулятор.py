def calculator():
    print("Calculator")
    print("Available operations:")
    print("+ - addition")
    print("- - subtraction")
    print("* - multiplication")
    print("/ - division")
    print("** - power")
    print("% - modulus")
    print("Enter 'exit' to quit")
    
    while True:
        try:
            num1_input = input("First number (or 'exit'): ")
            if num1_input.lower() == 'exit':
                print("Goodbye!")
                break
            num1 = float(num1_input)
            
            operation = input("Operation (+, -, *, /, **, %): ")
            if operation.lower() == 'exit':
                print("Goodbye!")
                break
            
            num2_input = input("Second number (or 'exit'): ")
            if num2_input.lower() == 'exit':
                print("Goodbye!")
                break
            num2 = float(num2_input)
            
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: division by zero!")
                    continue
                result = num1 / num2
            elif operation == '**':
                result = num1 ** num2
            elif operation == '%':
                if num2 == 0:
                    print("Error: division by zero!")
                    continue
                result = num1 % num2
            else:
                print("Invalid operation!")
                continue
            
            print(f"Result: {num1} {operation} {num2} = {result}")
            print("-" * 30)
            
        except ValueError:
            print("Error: please enter a valid number!")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()