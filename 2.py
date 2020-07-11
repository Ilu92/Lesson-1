# Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input("Enter your local time in sec: "))
hours = time // 3600
minutes = (time // 60) - (hours * 60)
sec = time % 60

print(f"Now is {hours:02}:{minutes:02}:{sec:02} ")
