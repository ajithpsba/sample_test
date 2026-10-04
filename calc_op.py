from calc import add, sub, mul, div

def calculator(a,b, opp):
    if opp == "+":
        return add(a,b)
    elif opp == "-":
        return sub(a,b)
    elif opp == "*":
        return mul(a,b)
    elif opp == "/":
        return div(a,b)
    else:
        return "Invalid operator"
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
opp = input("Enter operator (+, -, *, /): ")
c = calculator(a,b,opp)
print("output:",c)
