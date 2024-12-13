import datetime
from datetime import datetime

def days_difference(date: str) -> int:
    # Перетворюємо рядок дати у форматі 'YYYY-MM-DD' у об'єкт datetime
    input_date = datetime.strptime(date, '%Y-%m-%d')
    
    # Отримуємо поточну дату
    current_date = datetime.today()
    
    # Обчислюємо різницю між поточною датою та заданою
    delta = current_date - input_date
    
    # Повертаємо кількість днів як ціле число
    return delta.days


