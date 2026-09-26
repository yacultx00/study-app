import os
from http.server import BaseHTTPRequestHandler, HTTPServer

def response(path):
	if path == "/health":
		return 200, "ok\n"
	if path == "/":
		return 200, os.getenv("MESSAGE", "Hello DevOps") + "\n"
	return 404, "not found\n"

class Handler(BaseHTTPRequestHandler):
	def do_GET(self):
		status, body = response(self.path)
		data = body.encode()
		self.send_response(status)
		self.send_header("Content-Type", "text/plain")
		self.send_header("Content-Length", str(len(data)))
		self.end_headers()
		self.wfile.write(data)
if __name__ == "__main__":
	HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
