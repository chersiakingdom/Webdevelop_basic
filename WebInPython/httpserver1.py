from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
os.chdir("C:/downloads/coding_study/Webpython/Webserver")

port = 8090
server_address = ('', port)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()
