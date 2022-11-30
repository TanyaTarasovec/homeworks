import random


def get_answers():
    answers = []
    for i in range(10000):
        num = str(i).zfill(4)

        if len(set(map(int, num))) == 4:
            answers.append(list(map(int, num)))
            return answers 


def get_1_answer(one):
    numeral = random.choice(one)
    return numeral


def input_numbers():
    while True:
        nums = input("Введите 4 неповторяющиеся цифры: ")
        if len(nums) != 4 or not nums.isdigit():
            continue
        nums = list(map(int, nums))
        if len(set(nums)) == 4:
            break
        return nums


def check(numbers, true_numbers):
    bulls, cows = 0, 0
    for i, nums in enumerate(input_numbers):
        if numbers is true_numbers:
            if numbers[i] == true_numbers[i]:
                bulls += 1
            else:
                cows += 1
                return bulls, cows
    

def delete_bad_answer(answers, enemy_try, bull, cow):
    for number in answers[:]:
        t_bull, t_cow = check(number, enemy_try)

        if t_bull != bull or t_cow != cow:
            answers.remove(number)
    return answers


all_answer = get_answers()
enemy = get_1_answer(all_answer)
player = input_numbers()
print("Игра Быки и коровы")

while True:
    print("=" * 10, "Ход игрока", "=" * 10)
    print("Угадайте число компьютера")
    number = input_numbers()
    bulls, cows = check(player, enemy)
    print("Быки", bulls, "Коровы", cows)
    if bulls == 4:
        print("Игрок выиграл")
        print("Компьютер загадал: ", enemy)
        break

print("=" * 10, "Ход компьютера", "=" * 10)
enemy_try = get_1_answer(all_answer)
print("Компьютер говорит, что вы загадали число: ", enemy_try)
bulls, cows = check(enemy_try, player)
print("Быки", bulls, "Коровы", cows)
if bulls == 4:
    print("Выиграл компьютер")
    print("Компьютер загадал: ", enemy)
    

else:
    answer = delete_bad_answer(all_answer, enemy_try, bulls, cows)