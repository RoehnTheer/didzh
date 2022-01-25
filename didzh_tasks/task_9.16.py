import string
import random


class User:
    """Юзер - он и в Африке юзер."""

    def __init__(self, name: str, age: int):
        """Конструктор принимает имя и возраст"""
        self.age = age
        self.name = name
    
    def is_adult(self) -> bool:
        """Проверяет на совершеннолетие"""
        if self.age >= 18:
            return True
        return False
    
    @staticmethod
    def generate_password(self, password_length: int) -> str:
        """Генерирует пароль"""
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for i in range(password_length))
        """
        Другой вариант:
        available_symbols = string.ascii_letters + string.digits
        return ''.join(choices(available_symbols, k=pass_len))
        
        Немного странный, но тоже вариант:
        D = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        password = "".join([D[randint(0, len(D)-1)] for i in range(password_length)])
        return password
        """

    def get_name(self) -> str:
        """Возвращает имя"""
        return self.name
