import dash
from dash import html


if __name__ == "__main__":
	dash = dash.Dash()
	host = '127.0.0.1'
	dash.layout = html.Div(children=[
		html.H1(children='Hello'),
		html.Div(children=f'''And I'm working on {host}''')
	])
	dash.run_server(debug=True, host={host}, port=5050)






