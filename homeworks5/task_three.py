words = input("Введите букву:")

with open("three.txt", "r") as file:
    context = file.read()
    print(context)

    num_of_word = context.count(words)
    print(f"Результат: {num_of_word}")
