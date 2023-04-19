from flask import Flask, request, jsonify
from google.protobuf.json_format import MessageToJson
from google.cloud.dialogflowcx_v3.types import WebhookRequest, WebhookResponse, Intent, ResponseMessage

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Convert the request to JSON format
    request_json = request.get_json(silent=True, force=True)
    request_proto = WebhookRequest()
    WebhookRequest.FromJsonString(request_json, request_proto)

    # Parse the JSON request to extract the intent and parameters
    intent = request_proto.intent.display_name
    parameters = request_proto.parameters.fields

    # Handle the intent and generate a response
    if intent == 'Default Welcome Intent':
        response_text = 'Welcome to my Google Action!'
    else:
        response_text = 'I don\'t understand that command.'

    # Create a response object and set the text response
    response = WebhookResponse()
    text_response = ResponseMessage(text=Intent.Message.Text(text=[response_text]))
    response.payload = {"response_messages": [text_response]}

    # Convert the response object to JSON format
    response_json = MessageToJson(response)

    # Return the response as JSON
    return jsonify(response_json)

if __name__ == '__main__':
    app.run()
