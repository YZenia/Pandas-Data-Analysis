import pandas as pd

# Шаг 1: Загрузка данных из CSV файла
file_path = 'ecommerce_product_dataset.csv'
df = pd.read_csv(file_path)

# Шаг 2: Просмотр структуры данных
print(df.head())

# Шаг 3: Перевод названий колонок
translations = {
    "ProductID": "ID продукта",
    "ProductName": "Название продукта",
    "Category": "Категория",
    "Price": "Цена",
    "Rating": "Рейтинг",
    "NumReviews": "Количество отзывов",
    "StockQuantity": "Количество на складе",
    "Discount": "Скидка",
    "Sales": "Продажи",
    "DateAdded": "Дата добавления",
    "City": "Город"
}
df_translated = df.rename(columns=translations)

# Шаг 4: Перевод значений в колонках
product_name_translations = {
    "Headphones": "Наушники",
    "Smartwatch": "Смарт-часы",
    "Smartphone": "Смартфон",
    "Laptop": "Ноутбук",
    "Jacket": "Куртка",
    "Sweater": "Свитер",
    "T-Shirt": "Футболка",
    "Jeans": "Джинсы",
    "Coffee Maker": "Кофеварка",
    "Microwave": "Микроволновка",
    "Blender": "Блендер",
    "Toaster": "Тостер",
    "Biography": "Биография",
    "Fantasy Book": "Фэнтези книга",
    "Science Book": "Научная книга",
    "Novel": "Роман",
    "Board Game": "Настольная игра",
    "Puzzle": "Пазл",
    "Action Figure": "Фигурка",
    "Toy Car": "Игрушечная машина",
    "Fish Oil": "Рыбий жир",
    "Protein Powder": "Протеиновый порошок",
    "Vitamin D": "Витамин D",
    "Multivitamin": "Мультивитамины",
    "Sunscreen": "Солнцезащитный крем",
    "Cleanser": "Средство для умывания",
    "Moisturizer": "Увлажняющий крем",
    "Toner": "Тоник",
    "Mascara": "Тушь для ресниц",
    "Blush": "Румяна",
    "Lipstick": "Помада",
    "Foundation": "Тональный крем",
    "Denim Jacket": "Джинсовая куртка",
    "Rain Jacket": "Дождевик",
    "Leather Jacket": "Кожаная куртка",
    "Winter Coat": "Зимнее пальто",
    "Road Bike": "Шоссейный велосипед",
    "Mountain Bike": "Горный велосипед",
    "Hybrid Bike": "Гибридный велосипед",
    "Electric Bike": "Электровелосипед",
    "Sketchbook": "Альбом для рисования",
    "Brushes": "Кисти",
    "Paint Set": "Набор красок",
    "Canvas": "Холст",
    "Coffee Mug": "Кофейная кружка",
    "Water Bottle": "Бутылка для воды",
    "Tea Cup": "Чайная чашка",
    "Wine Glass": "Бокал для вина",
    "Eau de Toilette": "Туалетная вода",
    "Body Spray": "Спрей для тела",
    "Perfume Oil": "Парфюмерное масло",
    "Eau de Parfum": "Парфюмерная вода",
    "White Wine": "Белое вино",
    "Rose Wine": "Розовое вино",
    "Red Wine": "Красное вино",
    "Sparkling Wine": "Игристое вино",
    "Knee-High Socks": "Носки до колена",
    "Ankle Socks": "Носки до щиколотки",
    "Wool Socks": "Шерстяные носки",
    "Cotton Socks": "Хлопковые носки",
    "Silk Sheets": "Шелковые простыни",
    "Linen Sheets": "Льняные простыни",
    "Bamboo Sheets": "Бамбуковые простыни",
    "Cotton Sheets": "Хлопковые простыни",
    "Framed Poster": "Постер в рамке",
    "Canvas Print": "Печать на холсте",
    "Art Print": "Художественная печать",
    "Digital Art": "Цифровое искусство",
    "Soy Candle": "Соевая свеча",
    "Beeswax Candle": "Свеча из пчелиного воска",
    "Scented Candle": "Ароматическая свеча",
    "Pillar Candle": "Свеча-столбик",
    "Body Lotion": "Лосьон для тела",
    "Body Scrub": "Скраб для тела",
    "Bath Salts": "Соль для ванн",
    "Shower Gel": "Гель для душа",
    "Dutch Oven": "Чугунная кастрюля",
    "Frying Pan": "Сковорода",
    "Grill Pan": "Сковорода-гриль",
    "Saucepan": "Кастрюля",
    "Nail File": "Пилка для ногтей",
    "Nail Clippers": "Кусачки для ногтей",
    "Nail Polish": "Лак для ногтей",
    "Cuticle Oil": "Масло для кутикулы",
    "Thongs": "Танга",
    "Boxers": "Трусы-боксеры",
    "Briefs": "Трусы",
    "Panties": "Трусы",
    "Oil Filter": "Масляный фильтр",
    "Brake Pads": "Тормозные колодки",
    "Spark Plugs": "Свечи зажигания",
    "Car Battery": "Автомобильный аккумулятор",
    "Charger": "Зарядное устройство",
    "Screen Protector": "Защитная пленка",
    "Earbuds": "Наушники-вкладыши",
    "Phone Case": "Чехол для телефона",
    "Throw Blanket": "Плед",
    "Electric Blanket": "Электрическое одеяло",
    "Fleece Blanket": "Флисовое одеяло",
    "Weighted Blanket": "Утяжеленное одеяло"
}
category_translations = {
    "Electronics": "Электроника",
    "Clothing": "Одежда",
    "Home & Kitchen": "Дом и кухня",
    "Books": "Книги",
    "Toys & Games": "Игрушки и игры",
    "Vitamins and supplements": "Витамины и добавки",
    "Skin care": "Уход за кожей",
    "Makeup": "Косметика",
    "Coats and jackets": "Пальто и куртки",
    "Bicycles": "Велосипеды",
    "Art and crafting materials": "Материалы для искусства и рукоделия",
    "Drinkware": "Посуда для напитков",
    "Perfume and cologne": "Парфюмерия",
    "Wine": "Вино",
    "Socks": "Носки",
    "Bedsheets": "Простыни",
    "Posters and artwork": "Постеры и художественные работы",
    "Candles": "Свечи",
    "Bath and body": "Уход за телом",
    "Cookware": "Кухонная посуда",
    "Nail care": "Уход за ногтями",
    "Underwear": "Нижнее белье",
    "Motor vehicle parts": "Автозапчасти",
    "Mobile phone accessories": "Аксессуары для мобильных телефонов",
    "Blankets": "Одеяла"
}
df_translated['Название продукта'] = df_translated['Название продукта'].replace(product_name_translations)
df_translated['Категория'] = df_translated['Категория'].replace(category_translations)

# Шаг 5: Сохранение переведенного DataFrame в новый CSV файл
translated_file_path = 'translated_ecommerce_product_dataset.csv'
df_translated.to_csv(translated_file_path, index=False)

# Шаг 6: Загрузка набора данных из переведенного CSV-файла
df = pd.read_csv(translated_file_path)

# Шаг 7: Вывод первых 5 строк данных
print(df.head())

# Шаг 8: Вывод информации о данных
print(df.info())

# Шаг 9: Вывод статистического описания данных
print(df.describe())

# Шаг 10: Вывод статистического описания данных
print(df.describe())

# Шаг 11: Вывод топ-5 категорий по продажам
top_5_categories = df.groupby('Категория')['Продажи'].sum().nlargest(5).index
print("Топ-5 категорий по продажам:", top_5_categories.tolist())

# Шаг 12: Вывод топ-3 продуктов по продажам в каждой из топ-5 категорий
for category in top_5_categories:
    top_3_products_in_category = df[df['Категория'] == category].nlargest(3, 'Продажи')
    print(f"\nТоп-3 продукта в категории '{category}':")
    print(top_3_products_in_category[['Название продукта', 'Продажи']])

# Шаг 13: Вывод топ-10 продуктов по рейтингу
top_10_by_rating = df.nlargest(10, 'Рейтинг')
print("\nТоп-10 продуктов по рейтингу:")
print(top_10_by_rating[['Название продукта', 'Рейтинг']])

# Шаг 14: Вывод топ-3 самых продаваемых продуктов из самых дорогих
top_3_most_expensive = df.nlargest(10, 'Цена').nlargest(3, 'Продажи')
print("\nТоп-3 самых продаваемых продуктов из самых дорогих:")
print(top_3_most_expensive[['Название продукта', 'Цена', 'Продажи']])


# Шаг 14: Вывод топ-10 городов с наибольшим количеством продаж
def top_10_cities_by_sales(df):
    # Группировка данных по городам и суммирование продаж
    city_sales = df.groupby('Город')['Продажи'].sum().nlargest(10)

    # Вывод результата
    print("Топ-10 городов с наибольшим количеством продаж:")
    print(city_sales)


# Пример вызова функции
top_10_cities_by_sales(df)