import random

life = 10
length = 3

answer = random.randint(100, 999)
answer = str(answer)  # число -> строчку

while life:  # то же самое, что и while life != 0
    is_guessed = False  # отгадано?
    print("=" * 10)

    print("Жизней:", life)

    guess = input("Предположение: ")
    if len(guess) != length or guess.isdigit():  # если длина != 3 или не число
        print("Число от 100 до 999, пожалуйста!")
        continue
