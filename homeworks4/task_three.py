import random

digits = list(range(10))
computer_choice = []

for _ in range(4):
    digit = random.choice(digits)
    digits.remove(digit)
    computer_choice.append(str(digit))

computer_choice = "".join(computer_choice)
print(f"Computer_choice: {computer_choice}")

while True:
    user_choice = input("Enter your number: ")

    if user_choice == computer_choice:
        print("You are win!")
        break

    cows_counter = 0
    bulls_counter = 0

    for computer_digit, user_digit in zip(computer_choice, user_choice):
        if computer_digit == user_digit:
            bulls_counter += 1

        elif user_digit in computer_choice:
            cows_counter += 1
    
    print(f"{cows_counter} cows, {bulls_counter} bulls. ")
