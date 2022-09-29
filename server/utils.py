import json
import pickle
import numpy as np


__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, total_sqft, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1    
    x = np.zeros(len(__data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = bhk
    if loc_index > 0:
        x[loc_index] = 1
    
    prediction = __model.predict([x])[0]
    return round(prediction, 2)


def get_location_names():
    return __locations

def load_saved_tokens():
    print('Loading saved tokens..... Start!!!')
    global __data_columns
    global __locations

    with open(r"C:/Users/ifunanyaScript/Everything/House_price_prediction_repository/server/tokens/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    
    global __model
    with open(r"C:/Users/ifunanyaScript/Everything/House_price_prediction_repository/server/tokens/house_price_model.pickle", "rb") as f:
        __model = pickle.load(f)
    print("Loading saved tokens...... Done!!!")

if __name__ == "__main__":
    load_saved_tokens()
    print(get_estimated_price("WhiteField", 1500, 4, 4), "Lakh")
    print(get_estimated_price("1st Phase JP Nagar", 1000, 3, 4), "Lakh")
    print(get_estimated_price("Yelachenahalli", 2500, 8, 7), "Lakh")
    print(get_estimated_price("Kalhalli", 1000, 2, 2), "Lakh")

# ifunanyaScript