import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0) #1. Cемейство протоколов 'Интернет' (INET), 
                                                                           #2. Тип передачи "потоковый" (TCP),
                                                                           #3. Протокол по умолчанию для TCP, т.е. IP (proto=0)
server_socket.bind(('127.0.0.1', 53210)) #IP и порт на котором сервер будет ожидать подключения клиентов
server_socket.listen(10) #Состояние ожидания подключения, 10 - размер очереди входящих подключений

while True:
    #Бесконечная обработка входящих соединений
    client_sock, client_addr = server_socket.accept()
    print('Подключено', client_addr)

    while True:
        #Пока клиент не отключился, читаются передаваемые данные и отправляются обратно
        data = client_sock.recv(1024)
        if not data:
            #Отключение клиента
            break
        client_sock.sendall(data)

    client_sock.close()