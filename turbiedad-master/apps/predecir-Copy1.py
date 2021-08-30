import dash_html_components as html
import dash_admin_components as dac
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from apps.app_plots import plot_scatter

controls = dbc.Card(
    [
    dbc.FormGroup([
            dbc.Label("pH:", width=6,),
            dbc.Col(
                dbc.Input(id="pH", type="number", value=0),
#                width=10,
                ),
            ],
            row=True,
        ),
    dbc.FormGroup([
            dbc.Label("Temp(C):", width=6,),
            dbc.Col(
                  dbc.Input(id="Temp", type="number", value=0),
#                width=10,
                ),
            ],
            row=True,
        ),
    dbc.FormGroup([
            dbc.Label("Conductividad:", width=6,),
            dbc.Col(
                  dbc.Input(id="Conduct", type="number", value=0),
                  ),
            ],
            row=True,
        ),
    dbc.FormGroup([
            dbc.Label("Oxi Reducción:", width=6,),
            dbc.Col(
                  dbc.Input(id="OxiRed", type="number", value=0),
                  ),
            ],
            row=True,
        ),
    dbc.Button("Predecir", color="info", className="mr-1",id="boton",n_clicks=0),
    ],
    body=True,
)



predecir_tab = dac.TabItem(id='content_predecir', 
                              
    children=html.Div(
        [
#            html.H4("Módulo de Predicción"),
            dac.SimpleBox(
                id="DatosEntrada",
            	style = {'height': "560px"},
                width = 4,
#                title = "Box 1",
                children=[
                    dbc.Container(
                                  [
                                  html.H6("Ingrese los valores requeridos:"),
                                  dbc.Row(
                                         [
                                         dbc.Col(controls,md=12),
                                         ],
                                         align="center",
                                        )
                                 ]
                               )
                         ]
                    ),
            dac.SimpleBox(
                id="Resultados",
                width = 7,
            	style = {'height': "550px"},
 #               title = "Box 2",
                children=[
            #            html.H4('Modulo de Predicción - Turbiedad'),
                        html.Div([
                        dac.InfoBox(id="Idturbiedad",
                                  title = "Turbiedad",
                                  style={'background-color': '#0073b7'}, 
                                 #className="bg-blue",  
                                  width = 5,  
                            #      value = 0,
                                  icon = "water",
                                    ),
                        dac.InfoBox(id="Idcoagulante",
                                  title = "Coagulante",
                                  width = 5,
                                  style={'background-color': '#0073b7'}, 
#                                  className="bg-blue",  
                             #     value = 0,
                                  icon = "paint-brush"
                                   ),
                                ], className='row'
                                ),
             #           html.H4(''),
                        html.Div([
                        dcc.Graph(
                                figure=plot_scatter(),
                                config=dict(displayModeBar=False),
                                style={'width': '40vw'}
                                )
                                ]
                                ),
                        ],  className='row'
                        ),
        ], 
        className='row'
    )
)

