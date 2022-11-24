recv_data = b'GET /index.html HTTP/1.1\r\nHost: localhost:8000\r\nConnection: keep-alive\r\nsec-ch-ua: "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"\r\nsec-ch-ua-mobile: ?0\r\nsec-ch-ua-platform: "Windows"\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n'

recv_content = recv_data.decode("utf-8")
print(recv_content)

# 对数据按照空格进行分割
# request_list = recv_content.split(" ", maxsplit=2)
request_list = recv_content.split(" ")
# 获取请求的资源路径
print(request_list)
request_path = request_list[1]
print(request_path)