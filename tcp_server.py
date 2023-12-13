import socket
import time
import sys
import select

HOST = '192.168.0.128'  # 监听的主机IP地址
PORT = 8080  # 监听的端口号

# 创建TCP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP地址和端口号
server_socket.bind((HOST, PORT))

# 监听客户端连接请求
server_socket.listen(1)
print(f"Server started and listening on {HOST}:{PORT}")

# 等待客户端连接
client_socket, client_address = server_socket.accept()
print(f"Client {client_address[0]}:{client_address[1]} connected")

# 根据当前时间生成文件名
current_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
file_name = f"data_{current_time}.txt"
file_path = f"D:/pythonwpace/tcp_client/{file_name}"  # 替换为实际文件路径
try:
    with open(file_path,"w") as file:
        while True:
            try:
                # 接收客户端数据
                data = client_socket.recv(1024)
                received_data = data.decode('utf-8')
                print(f"Received data from client: {received_data}")

                #将数据写入文件
                file.write(received_data)
                file.flush() #立即将数据写入文件

                # 发送响应给客户端
                response = "Hello, client!"
                client_socket.send(response.encode('utf-8'))
            except KeyboardInterrupt:
                #捕捉Ctrl+C的中断信号，保存文件并关闭系统
                print("Keyboard interrupt detected. Saving file and exiting...")
                break
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    #关闭客户端连接和服务器套接字
    # 关闭客户端连接
    client_socket.close()    
    server_socket.close()                

