import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import Dash, dcc, html, Input, Output, State

# Данные, предоставленные пользователем
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

app = Dash(__name__)

# Функция для создания интерактивных графиков с возможностью фиксирования точек
def create_figure(selected_models=[]):
    fig = make_subplots(
        rows=2, cols=2,
        specs=[[{"type": "box"}, {"type": "xy"}], [{"type": "xy"}, {"type": "xy"}]],
        subplot_titles=("Вольтаж", "Цена vs Ёмкость батареи", "Цена vs Мощность", "Boxplot для Цена")
    )

    # Создание boxplot для вольтажа
    box_volt = go.Box(
        x=df['Батарея Вольт (V)'],
        text=df['Модель Двухколёсного Электрика'],
        name='Вольтаж',
        boxpoints='all',
        jitter=0.3,
        pointpos=-1.8,
        orientation='h',
        marker_color='#7FDBFF',
        selectedpoints=[i for i, model in enumerate(df['Модель Двухколёсного Электрика']) if model in selected_models],
        selected=dict(marker=dict(size=14, color='#FF4136')),
        hovertext=[f"{model}: {volt} V" for model, volt in zip(df['Модель Двухколёсного Электрика'], df['Батарея Вольт (V)'])]
    )
    fig.add_trace(box_volt, row=1, col=1)

    # Создание scatter-графика Цена vs Ёмкость батареи
    scatter2 = go.Scatter(
        x=df['Цена (руб)'],
        y=df['Ёмкость батареи (Ah)'],
        mode='markers+text',
        marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey')),
        text=[name if name in selected_models else '' for name in df['Модель Двухколёсного Электрика']],
        hoverinfo='text',
        customdata=df['Модель Двухколёсного Электрика'],
        name='Ёмкость батареи (Ah) vs Цена (руб)',
        selectedpoints=[i for i, model in enumerate(df['Модель Двухколёсного Электрика']) if model in selected_models],
        selected=dict(marker=dict(size=14, color='#FF4136'))
    )
    fig.add_trace(scatter2, row=1, col=2)

    # Создание scatter-графика Цена vs Мощность
    scatter3 = go.Scatter(
        x=df['Цена (руб)'],
        y=df['Мощность (W)'],
        mode='markers+text',
        marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey')),
        text=[name if name in selected_models else '' for name in df['Модель Двухколёсного Электрика']],
        hoverinfo='text',
        customdata=df['Модель Двухколёсного Электрика'],
        name='Мощность (W) vs Цена (руб)',
        selectedpoints=[i for i, model in enumerate(df['Модель Двухколёсного Электрика']) if model in selected_models],
        selected=dict(marker=dict(size=14, color='#FF4136'))
    )
    fig.add_trace(scatter3, row=2, col=1)

    # Создание boxplot для цены
    box_price = go.Box(
        y=df['Цена (руб)'],
        text=df['Модель Двухколёсного Электрика'],
        name='Цена (руб)',
        boxpoints='all',
        jitter=0.3,
        pointpos=-1.8,
        marker_color='#7FDBFF',
        hoverinfo='text',
        selectedpoints=[i for i, model in enumerate(df['Модель Двухколёсного Электрика']) if model in selected_models],
        selected=dict(marker=dict(size=14, color='#FF4136')),
        hovertext=[f"{model}: {price} руб." for model, price in zip(df['Модель Двухколёсного Электрика'], df['Цена (руб)'])]
    )
    fig.add_trace(box_price, row=2, col=2)

    fig.update_layout(
        height=800,
        width=1200,
        title_text="Сложный комбинированный анализ электроскутеров",
        template='plotly_dark',
        showlegend=False
    )
    return fig

app.layout = html.Div([
    dcc.Graph(id='scatter-plot', figure=create_figure()),
    dcc.Store(id='selected-models', data=[])
])

@app.callback(
    Output('scatter-plot', 'figure'),
    Output('selected-models', 'data'),
    Input('scatter-plot', 'clickData'),
    State('selected-models', 'data')
)
def update_figure(clickData, selected_models):
    if clickData and 'customdata' in clickData['points'][0]:
        selected_model = clickData['points'][0]['customdata']
        if selected_model in selected_models:
            selected_models.remove(selected_model)
        else:
            if len(selected_models) < 10:
                selected_models.append(selected_model)
    return create_figure(selected_models), selected_models

if __name__ == '__main__':
    app.run_server(debug=True)
