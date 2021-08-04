# Name: httpserver2.py
# Client: http://localhost:8096

from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import parse_qs, urlparse#자르는거
#핸들러 변형.. 
class testHTTPServer_RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self): #오버라이드
        url = self.path
        form = parse_qs(urlparse(url).query)
        print(form) #딕셔너리로 나옴.
       
        super().do_GET()
        print("do_get")
        
 
port = 8095
httpd = HTTPServer(('', port), testHTTPServer_RequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()