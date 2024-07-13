import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import Dash, dcc, html, Input, Output, State
import plotly.io as pio
import os

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

app = Dash(__name__)

# Цвета для каждой модели
colors = {
    "BLADE F8 Plus+": "red", "NIU UQi GT2": "green", "CityCoco Black Sea": "blue",
    "Pulse X7 Pro": "orange", "Pulse Mini-7.1": "purple", "Pulse X1": "cyan",
    "CityCoCo X12 PRO NEW": "magenta", "WS-LIGHT 1200W": "lime", "PULSE XC-1": "brown",
    "ALPHA CHAMP": "pink", "Ikingi CP9 3000W": "yellow", "CityCoco X2 Pro": "teal",
    "CityCoCo X7 PRO 3000W": "coral", "CityCoCo GT X11": "navy", "Ikingi M6 PRO": "gold",
    "Ikingi M9 Pro": "salmon", "CityCoCo GT X5": "olive"
}

# Функция для создания интерактивных графиков с возможностью фиксирования точек
def create_figure(selected_models=[]):
    fig = make_subplots(
        rows=2, cols=2,
        specs=[[{"type": "box"}, {"type": "xy"}], [{"type": "xy"}, {"type": "xy"}]],
        subplot_titles=("Вольтаж", "Цена vs Ёмкость батареи", "Цена vs Мощность", "Boxplot для Цена")
    )

    # Создание boxplot для вольтажа
    for voltage in sorted(df['Батарея Вольт (V)'].unique()):
        filtered_df = df[df['Батарея Вольт (V)'] == voltage]
        unselected_df = filtered_df[~filtered_df['Модель Двухколёсного Электрика'].isin(selected_models)]

        # Unselected points
        box_volt_unselected = go.Box(
            x=unselected_df['Цена (руб)'],
            y=[f"{voltage}V" for _ in range(len(unselected_df))],
            text=unselected_df['Модель Двухколёсного Электрика'],
            name=f'{voltage}V',
            boxpoints='all',
            jitter=0.3,
            pointpos=-1.8,
            orientation='h',
            marker=dict(color='#7FDBFF'),
            hoverinfo='text+name',
            hovertext=[f"{model}: {price} руб." for model, price in
                       zip(unselected_df['Модель Двухколёсного Электрика'], unselected_df['Цена (руб)'])]
        )
        fig.add_trace(box_volt_unselected, row=1, col=1)

        # Selected points
        for model in selected_models:
            selected_model_df = filtered_df[filtered_df['Модель Двухколёсного Электрика'] == model]
            box_volt_selected = go.Box(
                x=selected_model_df['Цена (руб)'],
                y=[f"{voltage}V" for _ in range(len(selected_model_df))],
                text=selected_model_df['Модель Двухколёсного Электрика'],
                name=f'{voltage}V',
                boxpoints='all',
                jitter=0.3,
                pointpos=-1.8,
                orientation='h',
                marker=dict(color=colors[model]),
                hoverinfo='text+name',
                hovertext=[f"{model}: {price} руб." for model, price in
                           zip(selected_model_df['Модель Двухколёсного Электрика'], selected_model_df['Цена (руб)'])]
            )
            fig.add_trace(box_volt_selected, row=1, col=1)

    # Создание scatter-графика Цена vs Ёмкость батареи
    scatter2 = go.Scatter(
        x=df['Цена (руб)'],
        y=df['Ёмкость батареи (Ah)'],
        mode='markers+text',
        marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey'),
                    color=[colors[model] if model in selected_models else '#7FDBFF' for model in
                           df['Модель Двухколёсного Электрика']]),
        text=[model if model in selected_models else '' for model in df['Модель Двухколёсного Электрика']],
        textposition='top center',
        hoverinfo='text',
        hovertext=[f"{model}" for model in df['Модель Двухколёсного Электрика']],
        customdata=df['Модель Двухколёсного Электрика'],
        name='Ёмкость батареи (Ah) vs Цена (руб)',
        selectedpoints=[i for i, model in enumerate(df['Модель Двухколёсного Электрика']) if
                        model in selected_models],
        selected=dict(marker=dict(size=14))
    )
    fig.add_trace(scatter2, row=1, col=2)

    # Создание scatter-графика Цена vs Мощность
    scatter3 = go.Scatter(
        x=df['Цена (руб)'],
        y=df['Мощность (W)'],
        mode='markers+text',
        marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey'),
                    color=[colors[model] if model in selected_models else '#7FDBFF' for model in
                           df['Модель Двухколёсного Электрика']]),
        text=[model if model in selected_models else '' for model in df['Модель Двухколёсного Электрика']],
        textposition='top center',
        hoverinfo='text',
        hovertext=[f"{model}" for model in df['Модель Двухколёсного Электрика']],
        customdata=df['Модель Двухколёсного Электрика'],
        name='Мощность (W) vs Цена (руб)',
        selectedpoints=[i for i, model in enumerate(df['Модель Двухколёсного Электрика']) if
                        model in selected_models],
        selected=dict(marker=dict(size=14))
    )
    fig.add_trace(scatter3, row=2, col=1)

    # Создание boxplot для цены
    unselected_df = df[~df['Модель Двухколёсного Электрика'].isin(selected_models)]

    # Unselected points
    box_price_unselected = go.Box(
        y=unselected_df['Цена (руб)'],
        text=unselected_df['Модель Двухколёсного Электрика'],
        name='Цена (руб)',
        boxpoints='all',
        jitter=0.3,
        pointpos=-1.8,
        marker=dict(color='#7FDBFF'),
        hoverinfo='text+name',
        hovertext=[f"{model}: {price} руб." for model, price in
                   zip(unselected_df['Модель Двухколёсного Электрика'], unselected_df['Цена (руб)'])]
    )
    fig.add_trace(box_price_unselected, row=2, col=2)

    # Selected points
    for model in selected_models:
        selected_model_df = df[df['Модель Двухколёсного Электрика'] == model]
        box_price_selected = go.Box(
            y=selected_model_df['Цена (руб)'],
            text=selected_model_df['Модель Двухколёсного Электрика'],
            name='Цена (руб)',
            boxpoints='all',
            jitter=0.3,
            pointpos=-1.8,
            marker=dict(color=colors[model]),
            hoverinfo='text+name',
            hovertext=[f"{model}: {price} руб." for model, price in
                       zip(selected_model_df['Модель Двухколёсного Электрика'], selected_model_df['Цена (руб)'])]
        )
        fig.add_trace(box_price_selected, row=2, col=2)

    fig.update_layout(
        height=800,
        width=1200,
        title_text="Сложный комбинированный анализ электроскутеров",
        template='plotly_dark',
        showlegend=False
    )
    return fig


# Функция для создания отдельных графиков для мобильных устройств
def create_individual_figures():
    mean_values = df.mean(numeric_only=True)
    median_values = df.median(numeric_only=True)
    std_deviation = df.std(numeric_only=True)
    q1 = df.quantile(0.25, numeric_only=True)
    q3 = df.quantile(0.75, numeric_only=True)

    statistics = pd.DataFrame({
        "Среднее значение": mean_values,
        "Медиана": median_values,
        "Стандартное отклонение": std_deviation,
        "Q1": q1,
        "Q3": q3
    })

    figures = []

    statistics_columns = ["Цена (руб)", "Ёмкость батареи (Ah)", "Мощность (W)", "Батарея Вольт (V)"]
    statistics_names = ["Среднее значение", "Медиана", "Стандартное отклонение", "Q1", "Q3"]
    colors_statistics = ["blue", "green", "red", "orange", "purple"]

    for column in statistics_columns:
        fig = go.Figure()
        for j, stat in enumerate(statistics_names):
            fig.add_trace(
                go.Bar(
                    x=[stat],
                    y=[statistics.loc[column, stat]],
                    name=stat,
                    marker_color=colors_statistics[j]
                )
            )
        fig.update_layout(
            title=f"Статистический анализ {column}",
            template='plotly_dark',
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.3,
                xanchor="center",
                x=0.5,
                font=dict(size=10)
            )
        )
        figures.append(fig)
    return figures


app.layout = html.Div([
    html.Div([
        html.H4('Выберите модели:', style={'color': 'white'}),
        dcc.Checklist(
            id='model-selector',
            options=[
                {'label': html.Span(model, style={'color': colors[model]}), 'value': model} for model in
                df['Модель Двухколёсного Электрика']
            ],
            value=[],
            labelStyle={'display': 'block', 'backgroundColor': 'black', 'padding': '5px'}
        ),
        html.Button('Сохранить графики как HTML', id='save-html-button', n_clicks=0)
    ], style={'width': '20%', 'display': 'inline-block', 'verticalAlign': 'top', 'backgroundColor': 'black',
              'padding': '20px'}),
    html.Div([
        dcc.Graph(id='scatter-plot', figure=create_figure(), className='desktop-layout'),
        dcc.Store(id='selected-models', data=[])
    ], style={'width': '75%', 'display': 'inline-block'}),
    html.Div([
        dcc.Tabs([
            dcc.Tab(label='Цена (руб)', children=[
                dcc.Graph(figure=create_individual_figures()[0])
            ]),
            dcc.Tab(label='Ёмкость батареи (Ah)', children=[
                dcc.Graph(figure=create_individual_figures()[1])
            ]),
            dcc.Tab(label='Мощность (W)', children=[
                dcc.Graph(figure=create_individual_figures()[2])
            ]),
            dcc.Tab(label='Батарея Вольт (V)', children=[
                dcc.Graph(figure=create_individual_figures()[3])
            ])
        ], className='mobile-layout')
    ])
], style={'backgroundColor': 'black'})  # Изменение фона всего приложения


@app.callback(
    [Output('scatter-plot', 'figure'),
     Output('model-selector', 'value')],
    [Input('scatter-plot', 'clickData'),
     Input('model-selector', 'value')],
    [State('selected-models', 'data')]
)
def update_figure(clickData, model_selector, selected_models):
    if model_selector is not None:
        selected_models = model_selector

    if clickData and 'customdata' in clickData['points'][0]:
        selected_model = clickData['points'][0]['customdata']
        if selected_model in selected_models:
            selected_models.remove(selected_model)
        else:
            if len(selected_models) < 10:
                selected_models.append(selected_model)

    return create_figure(selected_models), selected_models

@app.callback(
    Output('save-html-button', 'n_clicks'),
    [Input('save-html-button', 'n_clicks')],
    [State('scatter-plot', 'figure')]
)
def save_figure_as_html(n_clicks, figure):
    if n_clicks > 0:
        if not os.path.exists('saved_graphs'):
            os.makedirs('saved_graphs')
        file_path = os.path.join('saved_graphs', f'combined_plot_{n_clicks}.html')
        pio.write_html(figure, file=file_path)
        print(f"Графики сохранены как {file_path}")
    return 0

if __name__ == '__main__':
    app.run_server(debug=True)
