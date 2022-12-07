def success_number(result, operator, bel_number):
    operators = {"a1": "A1", "mts": "МТС", "life": "Life:)"}
    result["success"] = True
    result["phone"] = bel_number
    result["operator"] = operators[operator]
    return result


while True:
    result = {}
    bel_number = input("Введите номер телефона в международном формате: ")

    if len(bel_number) != 13:
        result["success"] = False
        result["description"] = "Номер телефона должен состоять из 13 символов"
        print(result)

    for char in bel_number[1::]:
        if not char.isdigit():
            result["success"] = False
            result["description"] = "Номер телефона должен состоять из цифр"
            print(result)
            break

        if bel_number[0] not in ("+"):
            result["success"] = False
            result["description"] = "Неизвестный номер"
            print(result)
            break

        if bel_number[1:3:] not in "375":
            result["success"] = False
            result["description"] = "Неверный код страны"
            print(result)
            break

        if bel_number[4:6:] not in ("25", "29", "33", "44"):
            result["success"] = False
            result["description"] = "Неизвестный код оператора"
            print(result)
            break
        elif bel_number[4:6:] in "29":
            if bel_number[6] in ("1", "3", "6", "9"):
                print(success_number(result, "a1", bel_number))
                break
            elif bel_number[6] in ("2", "5", "7", "8"):
                print(success_number(result, "mts", bel_number))
                break
            else:
                result["success"] = False
                result["description"] = "Неизвестный номер"
                print(result)
                break
        elif bel_number[4:6:] in "33":
            print(success_number(result, "mts", bel_number))
            break
        elif bel_number[4:6:] in "25":
            print(success_number(result, "life", bel_number))
            break
        elif bel_number[4:6:] in "44":
            print(success_number(result, "a1", bel_number))
            break

    exit_program = input("Хотите выйти из программы (да/нет) :")
    if exit_program == "да":
        break

    elif exit_program == "нет":
        continue
