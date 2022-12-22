a = float(input("Enter first number: \n"))
b = float(input("Ënter second number: \n"))
action = str(input("Chose your action: add '+' subtract '-' multiply '*' or divide '/'  \n"))

if action == "+":
    print(f"Your addition result is {a+b}")
elif action == "-":
    print(f"Your subtraction result is {a-b}")
elif action == "*":
    print(f"Your mutiplication result is {a*b}")
elif action == "/":
    print(f"Your division result is {a/b}")