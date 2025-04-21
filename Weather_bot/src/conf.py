from dotenv import load_dotenv
import os
load_dotenv()

apis= {
"OPENAI_API_KEY" : os.getenv("OPENAI_API_KEY"),
"WEATHER_API_KEY" : os.getenv("WEATHER_API_KEY")}