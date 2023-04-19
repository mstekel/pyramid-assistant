from flask import Flask, request, jsonify
from google.protobuf.json_format import MessageToJson
from google.cloud import dialogflow

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Convert the request to JSON format
    request_json = request.get_json(silent=True, force=True)
    request_proto = dialogflow.types.WebhookRequest()
    dialogflow.json_format.ParseDict(request_json, request_proto)

    # Parse the JSON request to extract the intent and parameters
    intent = request_proto.query_result.intent.display_name
    parameters = request_proto.query_result.parameters.fields

    # Handle the intent and generate a response
    if intent == 'Default Welcome Intent':
        response_text = 'Welcome to my Google Action!'
    else:
        response_text = 'I don\'t understand that command.'

    # Create a response object and set the text response
    response = dialogflow.types.WebhookResponse()
    response.fulfillment_text = response_text

    # Convert the response object to JSON format
    response_json = MessageToJson(response)

    # Return the response as JSON
    return jsonify(response_json)

if __name__ == '__main__':
    app.run()
