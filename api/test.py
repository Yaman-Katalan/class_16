# Implementing Serverless Function:

from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        msg = "test message."
        self.wfile.write(msg.encode())

        return