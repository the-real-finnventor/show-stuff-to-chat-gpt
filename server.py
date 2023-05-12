import http.server
import socketserver

PORT = 6543

Handler = http.server.SimpleHTTPRequestHandler

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:6543')
        super().end_headers()

with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
    print("serving at port", PORT)
    # Add the --cors flag to enable cross-origin resource sharing
    httpd.allow_reuse_address = True
    httpd.RequestHandlerClass = CORSRequestHandler
    httpd.RequestHandlerClass.extensions_map['.wasm'] = 'application/wasm'
    httpd.serve_forever(poll_interval=0.5)
