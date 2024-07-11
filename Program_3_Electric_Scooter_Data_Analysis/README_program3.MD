### 🌐 Language Selection | Выбор языка | Wybór języka

#### 📊 Программа: Анализ данных по электрическим самокатам | Electric Scooter Data Analysis | Analiza danych hulajnóg elektrycznych

<details>
<summary>Русский</summary>
Эта программа на Python анализирует и отображает различные статистические данные для разных моделей электрических самокатов. Она включает создание DataFrame из предоставленных данных, сохранение его в CSV файл и вычисление основных статистических показателей, таких как среднее значение, медиана и стандартное отклонение для каждого числового параметра.

**Возможности:**
- **Создание DataFrame**: Построение DataFrame с использованием pandas на основе данных о различных моделях электрических самокатов.
- **Экспорт в CSV**: Сохранение DataFrame в CSV файл с именем `electric_scooters.csv`.
- **Проверка данных**: Отображение первых 4 строк DataFrame для проверки данных.
- **Статистический анализ**: Вычисление и вывод средних, медианных значений и стандартного отклонения для каждого числового параметра (цена, напряжение батареи, ёмкость батареи и мощность).
- **Описательная статистика**: Вывод подробного статистического резюме для каждого параметра, включая количество, среднее, стандартное отклонение, минимальное значение, 25-й перцентиль, медиану, 75-й перцентиль и максимальное значение.

**Используемые библиотеки:**
- pandas

**Ключевые шаги:**
1. Импортирование библиотеки pandas.
2. Создание DataFrame с данными о моделях электрических самокатов.
3. Сохранение DataFrame в CSV файл.
4. Отображение первых 4 строк данных.
5. Вычисление средних значений, медиан и стандартного отклонения для каждого числового параметра.
6. Отображение подробного статистического резюме.
</details>

<details>
<summary>English</summary>
This Python program analyzes and displays various statistics for different models of electric scooters. It includes functionality to create a DataFrame from provided data, save it to a CSV file, and compute basic statistics such as mean, median, and standard deviation for each numerical parameter.

**Features:**
- **DataFrame Creation**: Constructs a DataFrame using pandas with data for different models of electric scooters.
- **CSV Export**: Saves the DataFrame to a CSV file named `electric_scooters.csv`.
- **Data Inspection**: Displays the first 4 rows of the DataFrame to verify the data.
- **Statistical Analysis**: Computes and prints the mean, median, and standard deviation for each numerical parameter (price, battery voltage, battery capacity, and power).
- **Descriptive Statistics**: Outputs a comprehensive summary of statistics for each parameter, including count, mean, standard deviation, min, 25th percentile, median, 75th percentile, and max values.

**Libraries used:**
- pandas

**Key steps:**
1. Importing the pandas library.
2. Creating a DataFrame with data on electric scooter models.
3. Saving the DataFrame to a CSV file.
4. Displaying the first 4 rows of data.
5. Calculating mean, median, and standard deviation for each numerical parameter.
6. Displaying a detailed statistical summary.
</details>

<details>
<summary>Polski</summary>
Ten program w języku Python analizuje i wyświetla różne statystyki dla różnych modeli hulajnóg elektrycznych. Zawiera funkcjonalność tworzenia DataFrame z podanych danych, zapisywania go do pliku CSV i obliczania podstawowych statystyk, takich jak średnia, mediana i odchylenie standardowe dla każdego numerycznego parametru.

**Funkcje:**
- **Tworzenie DataFrame**: Konstrukcja DataFrame przy użyciu pandas z danymi dla różnych modeli hulajnóg elektrycznych.
- **Eksport CSV**: Zapisuje DataFrame do pliku CSV o nazwie `electric_scooters.csv`.
- **Inspekcja danych**: Wyświetla pierwsze 4 wiersze DataFrame w celu weryfikacji danych.
- **Analiza statystyczna**: Oblicza i wyświetla średnią, medianę i odchylenie standardowe dla każdego numerycznego parametru (cena, napięcie baterii, pojemność baterii i moc).
- **Statystyki opisowe**: Wyświetla szczegółowe podsumowanie statystyk dla każdego parametru, w tym liczebność, średnią, odchylenie standardowe, min, 25 percentyl, medianę, 75 percentyl i wartości maksymalne.

**Używane biblioteki:**
- pandas

**Kluczowe kroki:**
1. Importowanie biblioteki pandas.
2. Tworzenie DataFrame z danymi o modelach hulajnóg elektrycznych.
3. Zapisanie DataFrame do pliku CSV.
4. Wyświetlenie pierwszych 4 wierszy danych.
5. Obliczenie średniej, mediany i odchylenia standardowego dla każdego numerycznego parametru.
6. Wyświetlenie szczegółowego podsumowania statystycznego.
</details>



### Пример кода | Code Example | Przykład kodu

```python
import pandas as pd

# Данные
data = {
    "Модель Двухколёсного Электрика": [
        "BLADE F8 Plus+", "NIU UQi GT2", "CityCoco Black Sea", "Pulse X7 Pro", "Pulse Mini-7.1",
        "Pulse X1", "CityCoCo X12 PRO NEW", "WS-LIGHT 1200W", "PULSE XC-1", "ALPHA CHAMP",
        "Ikingi CP9 3000W", "CityCoco X2 Pro", "CityCoCo X7 PRO 3000W", "CityCoCo GT X11",
        "Ikingi M6 PRO", "Ikingi M9 Pro", "CityCoCo GT X5"
    ],
    "Цена (руб)": [
        240000, 249000, 125000, 160000, 80000, 110000, 180000, 95000, 75000, 135000,
        170000, 140000, 165000, 200000, 220000, 150000, 130000
    ],
    "Батарея Вольт (V)": [
        72, 48, 60, 60, 48, 60, 60, 48, 48, 60, 72, 60, 60, 60, 72, 72, 60
    ],
    "Ёмкость батареи (Ah)": [
        50, 31, 25, 20, 12, 20, 40, 15, 10, 24, 20, 30, 40, 50, 35, 20, 30
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

# Отображение первых 4 строк
first_4_rows = df.head(4)
print("Первые 4 строки DataFrame:")
print(first_4_rows)

# Вычисление средних значений для каждого параметра
mean_values = df.mean(numeric_only=True)
print("\nСредние значения для каждого параметра:")
print(mean_values)

# Вычисление медианных значений для каждого параметра
median_values = df.median(numeric_only=True)
print("\nМедианные значения для каждого параметра:")
print(median_values)

# Вычисление стандартного отклонения для каждого параметра
std_deviation_values = df.std(numeric_only=True)
print("\nСтандартное отклонение для каждого параметра:")
print(std_deviation_values)

# Основные статистические показатели для каждого параметра
statistics_df = df.describe()
print("\nОсновные статистические показатели для каждого параметра:")
print(statistics_df)
```

