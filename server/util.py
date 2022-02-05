import pickle
import json
import numpy as np
from tkinter.messagebox import NO


__locations = None
__data_columns = None
__model = None



def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __locations
    
    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    global __model
    if __model is None: 
        with open("./artifacts/banglore_home_prices_model.pickle",'rb') as f:
            
            __model = pickle.load(f)
    print("loading artifacts done")  

def get_location_names():
    return __locations          
    

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())