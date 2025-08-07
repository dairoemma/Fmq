import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    Host = os.getenv('HOST')
    Port = os.getenv('PORT')
    

