from openai import OpenAI
import os
from conf import apis
from exception import CustomException
from logger import logging
client = OpenAI()
def extract_city_from_msg(msg):
    prompt = f"extract the city name from the message:{msg}."
    try:
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [{"role": "user", "content": prompt}],
        )
        print(response.choices[0].message.content)
        return response.choices[0].message.content
    except CustomException as e:
        logging.error(f"Error in extract_city_from_msg: {e}")
        print(f"Error in extract_city_from_msg: {e}")
        return "unknown"

# if __name__ == "__main__":
#     city = extract_city_from_msg(msg)
    # print(extract_city_from_msg("What is the weather in New York?")) # should return "New York"
    # print(extract_city_from_msg("What is the weather in New York City?")) # should return "New York City"
    # print(extract_city_from_msg("What is the weather in New York City, NY?")) # should return "New York City, NY"
    # print(extract_city_from_msg("What is the weather in New York, NY?")) # should return "New York, NY"

