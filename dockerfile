# Используйте официальный образ Python
FROM python:3.9

# Установите рабочий каталог в /app
WORKDIR /app

# Копируйте файлы в рабочий каталог
COPY . /app

# Установите необходимые пакеты
RUN pip install flask requests python-dotenv 

# Укажите порт, на котором будет работать приложение
EXPOSE 5010

# Запустите приложение
CMD ["python", "app.py"]
