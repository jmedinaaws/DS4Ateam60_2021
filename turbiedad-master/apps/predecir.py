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
    # Datos de entreda                          
    children=html.Div(
        [
            dac.SimpleBox(
                id="DatosEntrada",
            	style = {'height': "570px"},
                width = 4,
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
            # Genrera datos de resultado
            dac.SimpleBox(
                id="Resultados",
                width = 7,
            	style = {'height': "570px"},
                children=[
                        html.Div([
                        dac.InfoBox(id="Idturbiedad",
                                  title = "Turbiedad",
                                  style={'background-color': '#0073b7','color':'white'}, 
                                  width = 6,  
                                  icon = "water",
                                    ),
                        dac.InfoBox(id="Idcoagulante",
                                  title = "Coagulante",
                                  width = 6,
                                  style={'background-color': '#0073b7','color':'white'}, 
                                  icon = "paint-brush"
                                   ),                            
                                ], className='row'
                                ), 
                        html.Br(),
                        html.Br(),
                    
                        html.Div([
                        dac.ValueBox(
                                    value="90%",
                                    subtitle="Model Training Accuracy",
                                    color = "primary",
                                    icon = "user",
                                    width=4
                                ),
                                dac.ValueBox(
                                  elevation = 4,
                                  value = "95%",
                                  subtitle = "Model Test Accuracy",
                                  color = "info",
                                  width=4,
                                  icon = "vial"
                                ),
                                dac.ValueBox(
                                  value = "560/80",
                                  subtitle = "Train/Test Split",
                                  color = "primary",
                                  width=4,
                                  icon = "cogs"
                                ),
                            ], className='row'),
                        ],  className='row'
                        ),
        ], 
        className='row'
    )
)

