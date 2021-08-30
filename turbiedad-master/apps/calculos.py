# Calls the model to calculate the turbidity

import pickle
import tpot
import pandas as pd

# load the model from disk
loaded_model = pickle.load(open('model/model_Other_RF.sav', 'rb'))


def calcule_turbiedad(ph,temp,conduct,OxiRed):
    data = {'pH': ph,         ## Puede crearse 
        'conductividad': conduct,
        'potOxiReduccion': OxiRed,
        'T': temp,
        'HR': 121,
        'PV': 1.24,
        'PA': 92,
        'VV': 1.45,
        'Rad': 9.2,
        'P': 12,
         'La Sierra': 0,
        'Santander': 1,
        'Timbio': 0}
    input_data = pd.DataFrame(data, index = [0])
    turbiedad = loaded_model.predict(input_data.to_numpy())
    return turbiedad[0]

def calcule_turbiedad1(ph,temp,conduct,):
    return ph+temp+conduct

def calcule_coagulante(ph,temp,conduct):
    return ph+temp+conduct
