import pandas as pd

# Загрузка данных
file_path = 'path_to_your/dz.csv'
data = pd.read_csv(file_path)

# Удаление строк с пустыми значениями в столбце City
data_cleaned = data.dropna(subset=['City'])

# Расчет средней зарплаты по городам
average_salary_by_city = data_cleaned.groupby('City')['Salary'].mean().reset_index()

# Сохранение результатов
output_path = 'Program_1_average_salary_by_city.csv'
average_salary_by_city.to_csv(output_path, index=False)
