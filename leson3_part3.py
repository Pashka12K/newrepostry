import random
import re

def get_numbers_ticket(min_val, max_val, quantity):
    # Перевірка коректності параметрів
    if not (1 <= min_val <= max_val <= 1000):
        return []
    if not (0 < quantity <= (max_val - min_val + 1)):
        return []

    # Генерація унікальних випадкових чисел
    numbers = random.sample(range(min_val, max_val + 1), quantity)

    # Сортування списку перед поверненням
    return sorted(numbers)

def normalize_phone(phone_number):
    # Видалення всіх символів, крім цифр та знака "+"
    phone_number = re.sub(r"[^\d+]", "", phone_number)

    # Додавання міжнародного коду, якщо потрібно
    if not phone_number.startswith("+"):
        if phone_number.startswith("380"):
            phone_number = "+" + phone_number
        else:
            phone_number = "+38" + phone_number

    return phone_number

# Приклад використання
print(get_numbers_ticket(1, 49, 6))
print(normalize_phone("    +38(050)123-32-34"))  # +380501233234
print(normalize_phone("     0503451234"))       # +380503451234
print(normalize_phone("(050)8889900"))          # +380508889900
print(normalize_phone("38050-111-22-22"))       # +380501112222
print(normalize_phone("38050 111 22 11   "))   # +380501112211
