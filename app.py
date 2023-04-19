from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():

    # Create response payload and return it
    payload = {
        "candidates": [
            {
                "first_simple": {
                    "variants": [
                        {
                          "speech": "Moshe Moshe"
                        }
                    ]
                }
            }
        ]
    }

    return jsonify(payload)

if __name__ == '__main__':
    app.run(debug=True)
