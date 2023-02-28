"""
1) Напишите программу, которая бы определяла, является ли введённая буква
(символ) гласной (постарайтесь сделать данное задание всеми возможными и
невозможными способами; не обращайте внимание на запреты требования).
"""


def is_char_vowel(char):
    return any([
        char == "a", char == "e", char == "i", char == "o", char == "u", char == "y",
        char == "A", char == "E", char == "I", char == "O", char == "U", char == "Y"
    ])


def build_msg(is_vowel):
    if is_vowel:
        return "Это гласная буква."
    else:
        return "Это не гласная буква."


def main():
    char = input("Введите букву: ")

    is_vowel = is_char_vowel(char)
    msg = build_msg(is_vowel)
    print(msg)


def test_1_a():
    char = "a"
    is_vowel = is_char_vowel(char)
    return is_vowel == True


def test_2_A():
    char = "A"
    is_vowel = is_char_vowel(char)
    return is_vowel == True


def test_3_B():
    char = "B"
    is_vowel = is_char_vowel(char)
    return is_vowel == False


def test_suite():
    msg = f"test_1_a = {test_1_a()}"
    msg += f"\ntest_2_A = {test_2_A()}"
    msg += f"\ntest_3_B = {test_3_B()}"

    print(msg)


test_suite()
main()
