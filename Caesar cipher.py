def caesar(text: str, k: int, alphabet=None) -> str:
    encrypted_text: str = ""

    if alphabet is None:
        alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in text:
        # проверка регистра и приведение к нижнему
        uppercase: bool = char.isupper()
        char = char.lower()
        # если символ это буква
        if char in alphabet:
            letter_index = alphabet.index(char)  # индекс буквы в алфавите

            encrypted_letter = alphabet[(letter_index + k) % len(alphabet)]  # зашифрованная буква

            # лишние проверки "чтоб работало"
            if uppercase:
                encrypted_text += encrypted_letter.upper()
            else:
                encrypted_text += encrypted_letter
        else:
            # это для "небукв"
            encrypted_text += char

    return encrypted_text


encrypted = caesar("Hello world!", 3)
decrypted = caesar(encrypted, -3)
print(encrypted)
print(decrypted)

print('-' * 10)

rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
encrypted = caesar("Привет мир!", 3, alphabet=rus)
decrypted = caesar(encrypted, -3, alphabet=rus)
print(encrypted)
print(decrypted)

""" Ниже будет приведена реализация на основе ASCI без использования вспомогательного алфавита"""
print('-' * 10)


def caesar_encrypt(_text: str, _shift: int) -> str:
    encrypted_text: str = ""
    for char in _text:
        if char.isalpha():
            ascii_offset: int = ord('a') if char.islower() else ord('A')  # это так относительно буквы А считать можно
            encrypted_text += chr((ord(char) - ascii_offset + _shift) % 26 + ascii_offset)
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(_text, _shift):
    return caesar_encrypt(_text, -_shift)


# Пример использования:
text = "Hello world!"
shift = 3
encrypted = caesar_encrypt(text, shift)
print(encrypted)
decrypted = caesar_decrypt(encrypted, shift)
print(decrypted)
