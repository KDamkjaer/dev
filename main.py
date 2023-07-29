import dash
from dash import html, dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server
app.title = 'Dash app with pure Altair HTML'

html = html.Div([
    html.H1('Dash app')
])

app.layout = html

if __name__ == '__main__':
    app.run_server(debug=True)