a = float(input("Введи число a: "))
b = float(input("Введи число b: "))
op = input("Введи дію (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("Ділення на нуль!")
    else:
        print(a / b)
else:
    print("Невідома дія!")
