
var http = require('http'); //모듈이름으로 이름만듬
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.end('Hello World!');
}).listen(8080); //함수를 파라미터로 받는 함수. 
// 어떤 요청이 오든 hello world 보냄.