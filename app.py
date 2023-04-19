from flask import Flask, request, jsonify
from google.protobuf.json_format import MessageToJson
from google.cloud.dialogflowcx_v3.types import webhook

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Convert the request to JSON format
    request_json = request.get_json(silent=True, force=True)
    request_proto = webhook.WebhookRequest()
    webhook.JsonFormat.Parse(request_json, request_proto)

    # Parse the JSON request to extract the intent and parameters
    intent = request_proto.intent_info.display_name
    parameters = request_proto.parameters

    # Handle the intent and generate a response
    if intent == 'Default Welcome Intent':
        response_text = 'Welcome to my Google Action!'
    else:
        response_text = 'I don\'t understand that command.'

    # Create a response object and set the text response
    response = webhook.WebhookResponse()
    response.fulfillment_response.messages.add(text=webhook.Intent.Message(text= [response_text]))

    # Convert the response object to JSON format
    response_json = MessageToJson(response)

    # Return the response as JSON
    return jsonify(response_json)

if __name__ == '__main__':
    app.run()
