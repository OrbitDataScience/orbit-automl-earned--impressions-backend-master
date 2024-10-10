"""
Author: Flávio Tomé - flavio.tome@orbitdatascience.com
Date: 2023-09-18

This is a basic template for a web app backend.
It runs using a Flask framework, executing within a Docker Container
configurated to run on port 5000.



"""
from flask import Flask, jsonify, request
from flask_cors import CORS
import io
from scripts import makeRequest

# The CORS extension is applied to the Flask app.
# This is important for handling cross-origin requests,
# allowing the frontend, hosted on a different domain,
# to interact with this backend.
app = Flask(__name__)
CORS(app)


#  An endpoint is defined at the root URL ("/")
#  using the @app.route decorator.
#  This route only handles HTTP GET requests
#  and responds with a JSON message saying,
#  "Orbit Web Template says: Backend here!".
@app.route("/", methods=['GET'])
def index():

    return jsonify("Orbit Web Template says: Backend here!")


@app.route("/postValues", methods=['POST'])
def test2():
    
    data = request.get_json()
    print(data)
    
    result = makeRequest(data)
    
    return jsonify(result)


# the Flask app is started with the host set to '0.0.0.0'
# (meaning it listens on all available network interfaces)
# and port 5000.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)



