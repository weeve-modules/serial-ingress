"""
All constants specific to weeve
"""
from app.utils.env import env

WEEVE = {
    "MODULE_NAME": env("MODULE_NAME", "serial ingress"),
    "MODULE_TYPE": env("MODULE_TYPE", "INGRESS"),
    "PORT":env("Port","/dev/cu.usbserial-130"),
    "BAUD_RATE":env("Baud Rate","115200"),
    "EGRESS_URL": env("EGRESS_URL", "https://hookb.in/oXkwLNJEEjHYX7mgwq6g")
}
