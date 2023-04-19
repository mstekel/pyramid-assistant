from flask import Flask, request, jsonify
from google.protobuf.json_format import MessageToJson
from google.cloud import dialogflowcx_v3beta1 as dialogflow

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Convert the request to JSON format
    request_json = request.get_json(silent=True, force=True)
    request_proto = dialogflow.DetectIntentRequest()
    MessageToJson(request_proto, request_json)

    # Parse the JSON request to extract the intent and parameters
    intent = request_proto.query_params.parameters.display_name
    parameters = request_proto.query_params.parameters.fields

    # Handle the intent and generate a response
    if intent == 'Default Welcome Intent':
        response_text = 'Welcome to Moshe\'s Google Action!'
    else:
        response_text = 'I\'m Moshe. I don\'t understand that command.'

    # Create a response object and set the text response
    response = dialogflow.DetectIntentResponse()
    response.query_result.fulfillment_text = response_text

    # Convert the response object to JSON format
    response_json = MessageToJson(response)

    # Return the response as JSON
    return jsonify(response_json)

if __name__ == '__main__':
    app.run()
