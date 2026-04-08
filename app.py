from http.server import *

PORT = 5020

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Docker Python Container")

HTTPServer(("0.0.0.0", PORT), MyHandler).serve_forever()



## Dockerfile for app.py (Web Server):

FROM python:3.9-slim

WORKDIR /app

COPY app.py .

EXPOSE 5020

CMD ["python", "app.py"]
