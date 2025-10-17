def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

def average(a, b):
    return (a + b) / 2

def get_number(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("Invalid number, try again.")

def print_menu():
    print(
        "Please select operation:\n"
        "1. addition\n"
        "2. subtraction\n"
        "3. multiplication\n"
        "4. division\n"
        "5. average\n"
        "6. show history\n"
        "7. quit\n"
    )

def format_result(a, op, b, res):
    return f"{a} {op} {b} = {res}"

def main():
    history = []
    while True:
        print_menu()
        choice = input("Select operation (1-7): ").strip()
        if choice == "7":
            print("Goodbye.")
            break
        if choice == "6":
            if not history:
                print("No history yet.")
            else:
                print("History:")
                for item in history:
                    print(" ", item)
            continue
        if choice not in {"1","2","3","4","5"}:
            print("Invalid selection, try again.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            res = add(num1, num2)
            entry = format_result(num1, "+", num2, res)
        elif choice == "2":
            res = subtract(num1, num2)
            entry = format_result(num1, "-", num2, res)
        elif choice == "3":
            res = multiply(num1, num2)
            entry = format_result(num1, "*", num2, res)
        elif choice == "4":
            res = divide(num1, num2)
            entry = format_result(num1, "/", num2, res)
        elif choice == "5":
            res = average(num1, num2)
            entry = format_result(num1, "avg", num2, res)

        print(entry)
        history.append(entry)

if __name__ == "__main__":
    main()