import dash
from dash import html


if __name__ == "__main__":
	dash = dash.Dash()
	dash.layout = html.Div(childrenpwd=[
		html.H1(children='Hello'),
		html.Div(children=f'''I'm working on 4050 port''')
		])
	dash.run_server(debug=True, host='127.0.0.1', port=4050)






