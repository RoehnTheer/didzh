from typing import Optional


def numbers_to_text(numbers: str) -> Optional[str]:
    command = numbers.split(" ")
    result = []
    alphabet = {
        1: ".,?!:;",
        2: "абвг",
        3: "дежз",
        4: "ийкл",
        5: "мноп",
        6: "рсту",
        7: "фхцч",
        8: "шщъы",
        9: "ьэюя",
        0: " ",
    }

    for i in command:
        for digit, letter in alphabet.items():
            if len(set(i)) == 1 and len(i) <= len(alphabet[int(i[0])]):
                if digit == int(i[0]):
                    result.append(letter[len(i) - 1])
            else:
                return None
    return ''.join(result)
