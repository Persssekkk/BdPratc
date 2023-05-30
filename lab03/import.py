# Александрова Екатерина 305
import psycopg2
import csv
 
# Подключение к базе данных
conn = psycopg2.connect(
    host="192.168.122.30",
    database="lab02",
    user="postgres",
    port=5432,
    password='1'
)
cursor = conn.cursor()
"""
# Путь к CSV-файлу
/home/persek/Csv/region.csv
/home/persek/Csv/country.csv
/home/persek/Csv/city.csv
/home/persek/lab3/coastline/output_convert
"""
 
csv_file_path = "/home/persek/lab3/coastline/output_convert/ne_10m_coastline.csv"
 
# Открытие CSV-файла
with open(csv_file_path, 'r') as file:
    # Создание объекта csv.reader
    csv_data = csv.reader(file)
  
    # Итерирование по строкам CSV-файла
    for row in csv_data:
        shape = float(row[0].replace(',', '.'))  
        segment = float(row[1].replace(',', '.'))  
        latitude = float(row[2].replace(',', '.'))  
        longitude = float(row[3].replace(',', '.'))  
 
        # SQL-запрос для вставки данных
        query = "INSERT INTO data.coastilne (shape, segment, latitude, longitude) " \
                "VALUES (%s, %s, %s, %s)"
 
    # Выполнение SQL-запроса с передачей параметров
        cursor.execute(query, (shape, segment, latitude, longitude))
# Фиксирование изменений в БД
conn.commit()
 
# Закрытие соединения
cursor.close()
conn.close()
