"""
All constants specific to the application
"""
from app.utils.env import env


APPLICATION = {
    "PORT": env("PORT","/dev/ttyUSB0"),
    "BAUD_RATE": env("BAUD_RATE","115200"),
}
