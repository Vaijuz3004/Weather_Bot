from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from gpt_utils import extract_city_from_msg
from weather_utils import get_weather
from exception import CustomException
from logger import logging

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get('Body','')
    city = extract_city_from_msg(incoming_msg)
    weather = get_weather(city)

    resp = MessagingResponse()
    msg = resp.message()
    msg.body(weather)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)