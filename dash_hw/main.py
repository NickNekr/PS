import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

data = {
    'OS': ['Android', 'Windows', 'IOS', 'MacOS', 'Linux', 'Other'],
    'Процент пользователей (%)': [41.61, 29.02, 18.18, 6.1, 1.51, 2.21]
}

df = pd.DataFrame(data)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Процент пользователей различных операционных систем"),
    dcc.Graph(
        id='os-users-graph',
        figure=px.pie(df, values='Процент пользователей (%)', names='OS')
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

