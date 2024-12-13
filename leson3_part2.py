import random

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

# Приклад використання
print(get_numbers_ticket(1, 49, 6))
