# Александрова Екатерина 305
import os
import csv
import psycopg2
 
conn = psycopg2.connect(host='192.168.124.127', port='5432', dbname='lab02', user='postgres', password='password')
cursor = conn.cursor()
 
# Путь к каталогу, содержащему файлы
files_directory = '/home/persek/lab03/academic.udayton.edu/kissock/http/Weather/gsod95-current'
files_directory_saves = '/home/persek/MyPython/import/output'
 
# Получение списка файлов в каталоге
files = [f for f in os.listdir(files_directory) if f.endswith('.txt')]
 
# Выбор названий файлов из базы данных
cursor.execute("SELECT dataset FROM data.city")
dataset_names = [row[0] for row in cursor.fetchall()]
 
# Преобразование файлов в формат CSV
for file in files:
    file_name = os.path.splitext(file)[0]
    if file_name in dataset_names:
        # Чтение данных из файла TXT
        with open(os.path.join(files_directory, file), 'r') as txt_file:
            data = txt_file.readlines()
 
        # Путь к файлу CSV для сохранения
        csv_file_path = os.path.join(files_directory_saves, f'{file_name}.csv')
 
        # Запись данных в CSV файл
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for line in data:
                values = line.strip().split()  # Значения будут разделены пробелами
                writer.writerow(values)
 
# Закрытие соединения с БД
cursor.close()
conn.close()
