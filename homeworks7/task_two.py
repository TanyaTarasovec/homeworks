a = int(input("Введите число 1 "))
b = int(input("Введите число 2 "))
c = int(input("Введите число 3 "))

while True:

    right = {
        'result': True,
        'description': 'the triangle is right-angled'
        }

    does_not_exist = {
        'result': False,
        'description': 'no such triangle exists'
        }

    not_rectangular = {
        'result': False,
        'description': 'the triangle is not right-angled'
        }

    if a + b > c or a + c > b or b + c > a:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
            print(right)
            break

        else:
            print(does_not_exist)
            break

    else:
        print(not_rectangular)
        break
