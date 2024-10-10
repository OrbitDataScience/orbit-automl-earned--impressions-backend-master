import ssl
import os
import json
import urllib.request
import pandas as pd

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context


def makeRequest(data):
    # this line is needed if you use self-signed certificate in your scoring service.
    allowSelfSignedHttps(True)

    # Request data goes here
    body = str.encode(json.dumps(data))

    url = 'https://radar-automl-wajkc.eastus2.inference.ml.azure.com/score'

    # Replace this with the primary/secondary key or AMLToken for the endpoint
    api_key = "2cDm0MTK9bxjtdo1o1CpRd6stmkRb63M"
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")

    # The azureml-model-deployment header will force the request to go to a specific deployment.
    # Remove this header to have the request observe the endpoint traffic rules
    headers = {'Content-Type': 'application/json', 'Authorization': (
        'Bearer ' + api_key), 'azureml-model-deployment': 'automl9dbe8796940-1'}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        print(result)
        # Convert bytes to string type and string type to dict
        string = result.decode('utf-8')
        json_obj = json.loads(string)
        return (json_obj)

    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))

        error_message = "The request failed with status code: " + \
            str(error.code)
        json_obj = json.dumps({"Error": error_message})
        return (json_obj)
