from random import randint

numbers = [randint(-100, 100) for i in range(10)]
print(numbers)


replace = numbers.insert(2, 70)
delete = numbers.pop(6)

print(numbers)
