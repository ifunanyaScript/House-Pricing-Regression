from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

@app.route('/locations')
def get_location_names():
    response = jsonify({
        'locations': utils.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/house_pricing', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])

    response = jsonify({
        'estimated_price': utils.get_estimated_price(location, total_sqft, bathrooms, bedrooms)
    })

    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server House Price Prediction")
    utils.load_saved_tokens()
    app.run()

# ifunanyaScript