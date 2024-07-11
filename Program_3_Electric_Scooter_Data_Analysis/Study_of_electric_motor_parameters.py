import pandas as pd

# Data provided
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

# Creating the DataFrame
df = pd.DataFrame(data)

# Saving the DataFrame as a CSV file
file_path_csv = "electric_scooters.csv"
df.to_csv(file_path_csv, index=False)

# Display the first 4 rows
first_4_rows = df.head(4)
print(first_4_rows)

# Calculating mean for each parameter
mean_values = df.mean(numeric_only=True)
print(mean_values)

# Calculating median for each parameter
median_values = df.median(numeric_only=True)
print(median_values)

first_4_rows, mean_values, median_values

# Generating statistics for each electric scooter

# Basic statistics for each scooter
statistics_df = df.describe()

import ace_tools as tools; tools.display_dataframe_to_user(name="Electric Scooter Statistics", dataframe=statistics_df)

statistics_df