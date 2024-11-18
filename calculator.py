def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error division by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operation"
def main():
    print("normal Calculator")
    num1 = float(input ("Enter The First Number "))
    num2 = float(input("Enter The Second  Number "))
    print("\nchoose an  operations")
    print("add")
    print("subtract")
    print("multiply")
    print("divide ")
    operation = input("\nyour operation  is ").lower()
    answer = calculate(num1, num2, operation)
    print( "\nanswer ", answer)
if __name__ == "__main__":
    main()