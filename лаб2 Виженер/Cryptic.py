# Определение константы - алфавита
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Функция для генерации нового алфавита на основе сдвига индекса
def generate_new_alphabet(start_index):
    new_alphabet = ""
    for i in range(len(ALPHABET)):
        if i + start_index < len(ALPHABET):
            new_alphabet += ALPHABET[i + start_index]
        else:
            new_alphabet += ALPHABET[i - (len(ALPHABET) - start_index)]
    return new_alphabet


# Шифрование текста с помощью метода шифра Виженера
def encrypt_text(text_input: str, secret_key: str):
    encrypted_text_output = ""
    secret_key_iterator = 0  # Отслеживание позиции в секретном слове
    # Перебор каждого символа в тексте
    for i in range(len(text_input)):
        if text_input[i].isalpha():
            letter_position = ALPHABET.find(text_input[i].upper())
            new_alphabet = generate_new_alphabet(ALPHABET.find(secret_key[secret_key_iterator].upper()))

            if text_input[i].isupper():
                encrypted_text_output += new_alphabet[letter_position]
            else:
                encrypted_text_output += new_alphabet[letter_position].lower()
            secret_key_iterator += 1

            if secret_key_iterator >= len(secret_key):
                secret_key_iterator = 0
        else:
            encrypted_text_output += text_input[i]
    return encrypted_text_output


# Расшифровка текста
def decrypt_text(encrypted_text_output: str, secret_key: str):
    decrypted_text_output = ""
    secret_key_iterator = 0
    for i in range(len(encrypted_text_output)):
        if encrypted_text_output[i].isalpha():
            new_alphabet = generate_new_alphabet(ALPHABET.find(secret_key[secret_key_iterator].upper()))
            letter_position = new_alphabet.find(encrypted_text_output[i].upper())

            if encrypted_text_output[i].isupper():
                decrypted_text_output += ALPHABET[letter_position]
            else:
                decrypted_text_output += ALPHABET[letter_position].lower()
            secret_key_iterator += 1

            if secret_key_iterator >= len(secret_key):
                secret_key_iterator = 0
        else:
            decrypted_text_output += encrypted_text_output[i]
    return decrypted_text_output
