"""Index, to use for gunicorn production server"""
from elevator_app import app

__AUTHOR__ = "Oscar Lundberg"

server = app.server
