import dash
from dash import html


if __name__ == "__main__":
	dash = dash.Dash()
	dash.layout = html.Div(children=[
		html.H1(children='Hello'),
		html.Div(children=f'''And I'm working on 5050 port''')
	])
	dash.run_server(debug=True, host='127.0.0.1', port=5050)






