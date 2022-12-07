one_num = 0
two_num = 1
index = 1

user_index = int(input("Введите индекс: "))

if user_index == 0:
    print("Результат: 0")
elif user_index == 1:
    print("Результат: 1")

else:
    while True:
        index += 1
        new_num = one_num + two_num
        one_num = two_num
        two_num = new_num

        if user_index == index:
            print(f"Результат: {new_num}")
