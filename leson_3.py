import datetime
from datetime import datetime

def days_difference(date: str) -> int:
        try:
                # Перетворюємо рядок дати у форматі 'YYYY-MM-DD' у об'єкт datetime
                input_date = datetime.strptime(date, '%Y-%m-%d')
        
                # Отримуємо поточну дату
                current_date = datetime.today()
        
                # Обчислюємо різницю між поточною датою та заданою
                delta = current_date - input_date
        
                # Повертаємо кількість днів як ціле число
                return delta.days
        except ValueError:
        # Обробка помилок у випадку неправильного формату дати
                raise ValueError("Некоректний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")


