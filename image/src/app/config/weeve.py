"""
All constants specific to weeve
"""
from app.utils.env import env

WEEVE = {
    "MODULE_NAME": env("MODULE_NAME", "python-ingress-boilerplate"),
    "MODULE_TYPE": env("MODULE_TYPE", "INGRESS"),
    "Port":env("Port","/dev/cu.usbserial-1130"),
    "Baud_rate":env("Baud_rate","115200"),
    "EGRESS_URL": env("EGRESS_URL", "https://hookb.in/oXkwLNJEEjHYX7mgwq6g")

}
