"""
All constants specific to the application
"""
from app.utils.env import env


APPLICATION = {
    "PORT": env("PORT","/dev/cu.usbserial-130"),
    "BAUD_RATE": env("BAUD_RATE","115200"),
}
