import socket
import os
#os.chdir("C:/downloads/coding_study/Webpython/Webserver")
#print(os.getcwd())
#print(os.path.exists("C:/downloads/coding_study/Webpython/Webserver/html6.html"))

HOST, PORT = '', 9090 #호스트네임 지정안함, 포트번호 이 문으로만 들어올 수 있음.

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 소켓 종류(현재 IPv4 ( IP 어드레스 종류 )), 소켓 타입

listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 소켓 옵션 설정

listen_socket.bind((HOST, PORT))
#바인딩. 

listen_socket.listen(1)
# 1 주면 리슨 후 대기..
print ('Serving HTTP on port', PORT, '...')

while True:
    client_connection, client_address = listen_socket.accept()
    request = str(client_connection.recv(1024),'utf-8') #바이트로 온걸 str 로 만들어줌
    print (request)
    
# 보내기 ( 미리 만들어둔 html 파일 보내기)
    http_response = "HTTP/1.1 200 OK\n\n"
    file = open("C:/downloads/coding_study/Webpython/Webserver/html6.html", "r+b") #read & binary  로 읽혀라.
    # 바이트로인코딩해서 보내ㅣ
    client_connection.sendall(bytes(http_response, 'utf-8'))
    client_connection.sendfile(file) 

    file.close()
    client_connection.close()
    
    # 총 과정...
    #소켓 만들기 -> 바인딩 -> 리슨상태 -> 무한정 기다림 -> 요청들어오면 승인 ->
    # 리퀘스트에 맞게 보내주기 -> 연결 끊기
