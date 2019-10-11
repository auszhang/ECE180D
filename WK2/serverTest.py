import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(('0.0.0.0',12345))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    print("here2")
    from_client = ''
    while True:
        print("here")
        data = conn.recv(4096)
        print(data)
        if not data: break
        from_client += data.decode()
        print(from_client)
        
        conn.send("I am SERVER\n".encode())
    conn.close()
    print('client disconnected')