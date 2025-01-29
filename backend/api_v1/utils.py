import random
import string


def generate_random_string(length: int) -> str:
    """
    Генерирует и возвращает случайную строку.
    :param length: int: Необходимая длина случайной строки.
    :return: str
    """
    text = [
        random.choice(
            string.ascii_lowercase + string.digits if (
                i != 5
            ) else string.ascii_uppercase
        ) for i in range(length)
    ]
    return ''.join(text)
