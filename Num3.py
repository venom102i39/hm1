import random

secret = random.randint(1, 10)
attempts = 3

print("Я загадав число від 1 до 10. Спробуй вгадати!")

for i in range(attempts):
    guess = int(input("Введи число: "))

    if guess == secret:
        print("Вітаю! Ти вгадав!")
        break
    elif guess > secret:
        print("Менше!")
    else:
        print("Більше!")

if guess != secret:
    print(f"Ти програв! Загадане число було: {secret}")
