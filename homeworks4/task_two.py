list = []
for num in range(1, 101):
    if num % 15 == 0:
        list.append('FizzBuzz')
    elif num % 3 == 0:
        list.append('Fizz')
    elif num % 5 == 0:
        list.append('Buzz')
    else:
        list.append(num)
        print(list)