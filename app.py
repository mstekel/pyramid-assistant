from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    # Extract intent and parameters from the request
    intent = req['queryResult']['intent']['displayName']
    params = req['queryResult']['parameters']

    # Generate response based on the intent
    if intent == 'greet':
        name = params['name'] if 'name' in params else 'there'
        response = f'Hello, {name}!'
    elif intent == 'goodbye':
        response = 'Goodbye, have a nice day!'
    else:
        response = 'I am Pyramid. Your intent was ' + intent

    # Create response payload and return it
    payload = {
        'fulfillmentText': response
    }
    return jsonify(payload)

if __name__ == '__main__':
    app.run(debug=True)
