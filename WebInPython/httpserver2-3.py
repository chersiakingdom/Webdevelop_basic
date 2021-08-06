# Name: httpserver2.py
# Client: http://localhost:8096

from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import parse_qs, urlparse#자르는거
#핸들러 변형.. 
class testHTTPServer_RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self): #오버라이드
        url = self.path
        form = parse_qs(urlparse(url).query)  #딕셔너리로 나옴.
        # if form!={}:
        self.process_form(form)
       
        super().do_GET()
        print("do_get")
        
    def process_form(self,form):
        if 'food' in form:
            if form['food'][0] == 'Pizza': #리스트였으니까 몇번째인지 정하기
                print(form['firstname'][0] + ", call Dominos tonight!")
            elif form['food'][0] == 'Tacos':
                print(form['firstname'][0] + ", go to TacoBell tonight!")
            elif form['food'][0] == 'Salad':
                print(form['firstname'][0] + ", have a Caesar Salad tonight!")

port = 8095
httpd = HTTPServer(('', port), testHTTPServer_RequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()