# lst = [3, 5, -23, 0]
# print(min(lst))
# print(max(lst))
# print(sorted(lst))  # sorted() - сортировка

# word_1 = input("Введи первое из двух слов:")
# word_2 = input("Введи второе из двух слов:")
#
# word_1 = word_1.lower()  # уменьшить текст
# word_2 = word_2.lower()  # уменьшить текст
#
# word_1_sorted = sorted(word_1)  # сортировка по алфавиту
# word_2_sorted = sorted(word_1)  # сортировка по алфавиту
#
# if word_1_sorted == word_2_sorted:
#     print("Это анаграммы 😊")
# else:
#     print("Это не анаграммы ☹")

q1 = input("Сколько хромосом у человека?\n"
           "а) 23, б) 45, в) 46, г) 47\n"
           "--> ")
if q1 == "в":
    print("Балдёж! 😎")
else:
    print("Одна ошибка и ты ошибся 🐺")
    quit()

q2 = input("Когда был представлен первый Iphone? 🍎\n"
           "а) 2003, б) 2005, в) 2004, г) 2007\n"
           "--> ")
if q2 == "г":
    print("Балдёж! 😎")
else:
    print("Одна ошибка и ты ошибся 🐺")
    quit()

q3 = input("Кто основатель компании Microsoft?\n"
           "а) Стив Джобс, б) Билл Гейтс, в) Криштиану Рональдо, г) Мухаммед Али")
if q3 == "б":
    print("Балдёж! 😎")
else:
    print("Одна ошибка и ты ошибся 🐺")
    quit()

print("*Звуки аплодисментов*")
print("Твой ICQ очень высокий")