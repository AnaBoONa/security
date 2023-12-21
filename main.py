# Реализует шифровку, расшифровку и взлом Шифра Цезаря(сдвиг)

# Зашифровка
def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char == " ":
            result += " "
        elif ord(char) > 127:
            result += chr((ord(char) + shift - 1072) % 32 + 1072)
        elif char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result


# Расшифровка
def decrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char == " ":
            result += " "
        elif ord(char) > 127:
            result += chr((ord(char) - shift - 1072) % 32 + 1072)
        elif char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) - shift - 97) % 26 + 97)
    return result


# Взлом латиница
def crack_caesar(message, symbols):
    for key in range(len(symbols)):
        translated = ''
        for symbol in message:
            if symbol in symbols:
                symbol_index = symbols.find(symbol)
                translated_index = symbol_index - key
                if translated_index < 0:
                    translated_index = translated_index + len(symbols)
                translated = translated + symbols[translated_index]
            else:
                translated = translated + symbol
        print('Key #%s: %s' % (key, translated))


# Взлом кириллица
def crack_cyrillic(message, symbols):
    for key in range(len(symbols)):
        translated = ''
        for symbol in message:
            if symbol in symbols:
                symbol_index = symbols.find(symbol)
                translated_index = symbol_index - key
                if translated_index < 0:
                    translated_index = translated_index + len(symbols)
                translated = translated + symbols[translated_index]
            else:
                translated = translated + symbol
        print('Key #%s: %s' % (key, translated))


# Почти UI
while True:
    print("1. Зашифровать текст")
    print("2. Дешифровать текст")
    print("3. Взломать шифр")
    print("4. Выйти")

    print()
    choice = int(input("Выберите операцию: "))
    print()

    if choice == 1:
        print()
        text = input("Введите текст для шифрования: ")
        shift = int(input("Введите сдвиг: "))
        encrypted_text = encrypt(text, shift)
        print(f"Зашифрованный текст: {encrypted_text}")
        print()
    elif choice == 2:
        print()
        text = input("Введите текст для дешифрования: ")
        shift = int(input("Введите сдвиг: "))
        decrypted_text = decrypt(text, shift)
        print(f"Дешифрованный текст: {decrypted_text}")
        print()
    elif choice == 3:
        print()
        message = input("Введите текст для взлома: ")
        language = input("Выберите язык (1 - латиница, 2 - кириллица): ")
        if language == "1":
            SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?. '
            crack_caesar(message, SYMBOLS)
        elif language == "2":
            SYMBOLS1 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890!?. '
            crack_cyrillic(message, SYMBOLS1)
        else:
            print("Неверный выбор")
    elif choice == 4:
        break
    else:
        print("Неверный выбор")
