import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from chatgpt import get_chatgpt_response
 
app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    
    incoming_msg = request.values.get('Body', '').lower()
    
    print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    chatgpt = get_chatgpt_response(incoming_msg)
    
    msg.body(chatgpt)
    responded = True

    return str(resp)

 
if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=9293)
