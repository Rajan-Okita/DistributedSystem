from http.server import BaseHTTPRequestHandler
from typing import Callable
from flask import Flask # type: ignore

class RequestHandler(BaseHTTPRequestHandler):

    def __init__(self, app, forward_fn, add_fn, remove_fn, get_fn) -> None:
        self.app: Flask = app
        self.forward_fn: Callable = forward_fn
        self.remove_fn: Callable = remove_fn
        self.get_fn: Callable = get_fn
        self.add_fn: Callable = add_fn 

    class YourClass:
        def handle_GET(self, response=b"") -> None:
            """
            Responds to a get request
            """
            if not isinstance(response, bytes):
                response = response.encode()

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(response)
