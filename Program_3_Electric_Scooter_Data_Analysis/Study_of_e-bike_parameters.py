import pandas as pd

# Данные, предоставленные пользователем
data = {
    "Модель Двухколёсного Электрика": [
        "BLADE F8 Plus+", "NIU UQi GT2", "CityCoco Black Sea", "Pulse X7 Pro", "Pulse Mini-7.1",
        "Pulse X1", "CityCoCo X12 PRO NEW", "WS-LIGHT 1200W", "PULSE XC-1", "ALPHA CHAMP",
        "Ikingi CP9 3000W", "CityCoco X2 Pro", "CityCoCo X7 PRO 3000W", "CityCoCo GT X11",
        "Ikingi M6 PRO", "Ikingi M9 Pro", "CityCoCo GT X5"
    ],
    "Цена (руб)": [
        240000, 97000, 125000, 160000, 80000, 110000, 180000, 95000, 75000, 135000,
        170000, 140000, 165000, 200000, 220000, 150000, 130000
    ],
    "Батарея Вольт (V)": [
        72, 48, 60, 60, 48, 60, 60, 48, 48, 60, 72, 60, 60, 60, 72, 72, 60
    ],
    "Ёмкость батареи (Ah)": [
        50, 31, 25, 20, 12, 20, 40, 15, 10, 24, 20, 30, 40, 20, 35, 20, 30
    ],
    "Мощность (W)": [
        3500, 1500, 2000, 2000, 1000, 2000, 3000, 1200, 500, 1000, 3000, 1000, 3000, 3000, 4000, 2000, 1200
    ]
}

# Создание DataFrame
df = pd.DataFrame(data)

# Сохранение DataFrame в CSV файл
file_path_csv = "electric_scooters.csv"
df.to_csv(file_path_csv, index=False)

# Вывод первых 4 строк DataFrame
first_4_rows = df.head(4)
print("Первые 4 строки:")
print(first_4_rows)

# Вычисление среднего значения для каждого параметра
mean_values = df.mean(numeric_only=True)
print("\nСредние значения:")
print(mean_values)

# Вычисление медианного значения для каждого параметра
median_values = df.median(numeric_only=True)
print("\nМедианные значения:")
print(median_values)

# Вычисление стандартного отклонения для каждого параметра
std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение:")
print(std_deviation)

# Вычисление первого (Q1) и третьего (Q3) квартилей для каждого параметра
q1 = df.quantile(0.25, numeric_only=True)
q3 = df.quantile(0.75, numeric_only=True)
print("\nQ1 (Первый квартиль):")
print(q1)
print("\nQ3 (Третий квартиль):")
print(q3)

# Создание DataFrame для хранения статистических данных
statistics = pd.DataFrame({
    "Среднее значение": mean_values,
    "Медиана": median_values,
    "Стандартное отклонение": std_deviation,
    "Q1": q1,
    "Q3": q3
})

# Сохранение статистических данных в CSV файл
statistics_file_path_csv = "electric_scooters_statistics.csv"
statistics.to_csv(statistics_file_path_csv)

# Вывод путей к сохранённым CSV файлам
print("\nCSV файл с данными сохранён как:", file_path_csv)
print("CSV файл со статистикой сохранён как:", statistics_file_path_csv)
