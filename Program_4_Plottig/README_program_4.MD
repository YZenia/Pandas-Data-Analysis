# Электроскутеры Анализ - Dash Приложение

Это приложение Dash позволяет анализировать данные различных моделей двухколёсных электроскутеров. Приложение предоставляет интерактивные графики, которые можно сохранять как HTML и изображения.

## Установка

1. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/ваш_пользователь_на_github/electric-scooter-analysis.git
    ```

2. Перейдите в директорию проекта:

    ```sh
    cd electric-scooter-analysis
    ```

3. Создайте виртуальное окружение и активируйте его:

    ```sh
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```

4. Установите необходимые зависимости:

    ```sh
    pip install -r requirements.txt
    ```

## Запуск приложения

Для запуска приложения выполните следующую команду:

```sh
python app.py

To include an interactive example of your graph in the description of your GitHub repository, you can provide a link to the saved HTML file. Unfortunately, GitHub's Markdown does not support rendering HTML files directly within the README. However, you can upload the HTML file to a publicly accessible location (such as GitHub Pages) and link to it.

Here's how you can do it:

1. **Upload the HTML file to your repository**:
   - Place the `combined_plot_1.html` file in your repository. You might put it in a directory like `examples/`.

2. **Create a GitHub Pages site**:
   - Enable GitHub Pages for your repository by going to the repository settings.
   - Under the "GitHub Pages" section, select the branch you want to serve the pages from (typically `main` or `gh-pages`).
   - Choose the root directory or a specific directory (e.g., `/docs`) to serve the content.

3. **Link to the HTML file in your README**:
   - Update your `README.md` to include a link to the HTML file. If you have enabled GitHub Pages and placed the file in the `examples/` directory, the link might look something like this: `https://username.github.io/repository-name/examples/combined_plot_1.html`.

Here's an example of what your `README.md` might look like:

```markdown
# Электроскутеры Анализ - Dash Приложение

Это приложение Dash позволяет анализировать данные различных моделей двухколёсных электроскутеров. Приложение предоставляет интерактивные графики, которые можно сохранять как HTML и изображения.

## Установка

1. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/Program_4_Plottig/saved_graphs/combined_plot_1.html
    ```

2. Перейдите в директорию проекта:

    ```sh
    cd electric-scooter-analysis
    ```

3. Создайте виртуальное окружение и активируйте его:

    ```sh
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```

4. Установите необходимые зависимости:

    ```sh
    pip install -r requirements.txt
    ```

## Запуск приложения

Для запуска приложения выполните следующую команду:

```sh
python app.py
```

Приложение будет доступно по адресу `http://127.0.0.1:8050/`.

## Использование

1. **Выбор моделей**: Выберите модели скутеров с помощью чекбоксов в левой части экрана.
2. **Интерактивные графики**: Исследуйте различные графики, такие как вольтаж, цена против ёмкости батареи, цена против мощности и boxplot для цены.
3. **Сохранение графиков**:
    - Нажмите кнопку "Сохранить графики как HTML" для сохранения текущего графика в виде HTML-файла.
    - Нажмите кнопку "Сохранить графики как изображение" для сохранения текущего графика в виде PNG-изображения.

## Примеры графиков

### Пример сохраненного HTML графика

[Посмотреть интерактивный график](https://github.com/YZenia/Pandas-Data-Analysis/main/Program_4_Plottig/saved_graphs/combined_plot_1.html)

### Пример сохраненного PNG графика
![PNG Example](saved_graphs/combined_plot_1.png)

## Зависимости

- pandas
- plotly
- dash
- kaleido
- pillow

Эти зависимости указаны в файле `requirements.txt`.

## Лицензия

Этот проект лицензируется под лицензией MIT.
```

Replace `https://username.github.io/repository-name/examples/combined_plot_1.html` with the actual URL where your HTML file is hosted. 

By following these steps, you provide a clear and interactive example of your graph directly in the repository's README.
