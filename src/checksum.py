def modulo_11_checksum(isbn_number: str):

    digits = [int(char) for char in isbn_number if char.isdigit()]
    check_digit = digits[-1]

    total = 0
    weight = 10
    for i in range(len(digits) - 1):
        digit = digits[i]
        total += digit * weight
        weight -= 1

    checksum = total + check_digit

    return checksum % 11 == 0

def menu():
    
    isbn_number = input("Введите номер ISBN: ")
    
    if isbn_number == "-1":
        return

    for i in range(len(isbn_number)):
        if not isbn_number[i].isdigit() and isbn_number[i] != "-":
            if i in [1,5,11]:
                print(f"Ожидалось: -, Введено: {isbn_number[i]}")
            else:
                print(f"Ожидалось: цифра, Введено: {isbn_number[i]}")
            menu()

        if i in [1,5,11] and isbn_number[i] != "-":
            print(f"Ожидалось: -, Введено: {isbn_number[i]}")
            menu()
        
        if i not in [1,5,11] and isbn_number[i] == "-":
            print(f"Ожидалось: цифра, Введено: -")
            menu()

    if len(isbn_number) != 13:
        print(f"Введено символов: {len(isbn_number)}, Ожидалось: 13")
        menu()

    print(modulo_11_checksum(isbn_number))
    menu()
    
menu()
