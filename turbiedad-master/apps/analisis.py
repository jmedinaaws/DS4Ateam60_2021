import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac


from apps.app_plots import plot_scatter

analisis_tab = dac.TabItem(id='content_analisis', 
                              
    children=html.Div(
        [
            dac.SimpleBox(
            	style = {'height': "600px"},
                title = "Box 1",
                children=[
                    dcc.Graph(
                        id='box-graph',
                        config=dict(displayModeBar=False),
                        style={'width': '38vw'}
                    )
                ]
            ),
            dac.SimpleBox(
            	style = {'height': "600px"},
                title = "Box 2",
                children=[
                    dcc.Graph(
                        figure=plot_scatter(),
                        config=dict(displayModeBar=False),
                        style={'width': '38vw'}
                    )
                ]
            )
        ], 
        className='row'
    )
)
