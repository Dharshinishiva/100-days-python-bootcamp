#creating an calculator

def add(n1,n2):
    return n1 + n2
def sub(n1, n2):
    return n1-n2
def multi(n1, n2):
    return n1*n2
def div(n1, n2):
    return n1/n2

def calculator(first_number, last_number,what_to_do):
    

    if what_to_do == "add":
        print("Addition value: ",add(first_number,last_number))
    elif what_to_do == "sub":
        subtraction=sub(first_number,last_number)
        print("subtraction: ", subtraction)
    elif what_to_do == "multi":
        print(f"Multiplication: {multi(first_number,last_number)}")
    elif what_to_do == "div":
        division=div(first_number,last_number)
        print(f"division: {division}")
    elif what_to_do =="all":
        print("Addition value: ",add(first_number,last_number))
        print("subtraction value: ",sub(first_number,last_number))
        print("Multiplication value: ",multi(first_number,last_number))
        print("division value: ",div(first_number,last_number))

    else:
        print("invalid operation")



first_number = int(input("enter the first number:"))
last_number= int(input("enter the last_number:"))
what_to_do = input("enter the operation:")

calculator(first_number,last_number, what_to_do)
