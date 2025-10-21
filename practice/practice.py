def add(a,b):
    return a + b
def subtract(a,b):
    return a - b            
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Error: division by zero"
    return a / b

def getnumber(prompt):
    """Get a valid number from user input."""
    while True:
        s = input(prompt).strip()
        try:#try to convert the input to float
            return float(s)#if successful, return the float value
        except ValueError:
            print("Invalid number, try again.")#if conversion fails, prompt again

def printmenu():
    """Display the operation menu."""
    print(
        "Please select operation:\n"
        "1. addition\n"
        "2.subtraction\n"
        "3.multiplication\n"
        "4.didvision\n"
        "5.history\n"
        "6.quit\n")

def formatresult(a,op,b,res):
    """Format the result string."""
    return f"{a} {op} {b} = {res}"

def main():
    """Main function to run the calculator."""
    history =[]
    while True:
        printmenu() #display the menu
        choice = input("select operations(1-6): ").strip() #.strp() to remove extra spaces
        if choice == "6":
            print("goodbye.")
            break
        if choice == "5":
            if not history:
                print("no history yet.")
            else:
                print("history:")
                for item in history:#iterate through history list
                    print(" ",item)#print each history item
            continue
        if choice not in {"1","2","3","4"}:
            print("invalid selection, try again.")
            continue
        a = getnumber("enter first number:")
        b = getnumber("enter second number:")
        if choice =="1":
            res = add(a,b)
            entry = formatresult(a,"+",b , res)
        elif choice =="2":
            res = subtract(a,b)
            entry = formatresult(a,"-",b , res)
        elif choice =="3":
            res = multiply(a,b)
            entry = formatresult(a,"*",b , res)
        elif choice =="4":
            res = divide(a,b)
            entry = formatresult(a,"/",b , res)
        print(entry)
        history.append(entry)

if __name__ == "__main__": #make sure main() runs only when this file is executed directly
    main()     
    


    
