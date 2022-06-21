#  Create a Flask App (app.py)
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# Simply Instantiated Flask App 
app = Flask(__name__)

# Simply Prints Hello World When Instantiating an Application 
@app.route("/")
def hello():
    return "Hello, World!"

# Only Receives Posts Requests 
@app.route("/sms", methods=['POST'])

# Setting Up Call Back Url 
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    resp.message("You said: {}".format(msg))

# returning that response 
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)