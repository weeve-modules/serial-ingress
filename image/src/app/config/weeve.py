"""
All constants specific to weeve
"""
from app.utils.env import env

WEEVE = {
    "MODULE_NAME": env("MODULE_NAME", "serial-ingress"),
    "MODULE_TYPE": env("MODULE_TYPE", "INGRESS"),
    "EGRESS_URL": env("EGRESS_URL", "http://0.0.0.0:80")
}
