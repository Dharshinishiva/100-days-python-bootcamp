# creatung four function 

def add(n1,n2):
    return n1 + n2
def sub(n1, n2):
    return n1-n2
def multi(n1, n2):
    return n1*n2
def div(n1, n2):
    return n1/n2

    # adding these 4 function into a dictionary as value and keys are + _ * /
    
operations = {"+" : add, "-": sub, "*" : multi, "/": div}  # its a dictionary with a key and value

    # create a calculator using the operators inside the dictionary 

n1 = int(input("enter the first number:"))

for symbol in operations:  # using for loop because user can what symbols can be given 
        print(symbol)
what_to_do = input("enter the operation:")

n2 =  int(input("enter the second number:"))

answer = (operations[what_to_do](n1, n2))

print(f"{n1} {what_to_do} {n2} = {answer}") 




    