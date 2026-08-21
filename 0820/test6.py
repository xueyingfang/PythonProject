# import requests
#
# # GET 请求
# response = requests.get("https://httpbin.org/get", params={"key": "value"})
#
# # POST 请求
# response = requests.post("https://httpbin.org/post", data={"key": "value"})
#
# # 响应内容
# print(response.status_code)   # 状态码 200
# print(response.text)          # 文本内容
# print(response.content)       # 二进制内容（图片等）
# print(response.json())        # JSON 解析
# print(response.headers)       # 响应头
# print(response.encoding)      # 编码

# from bs4 import BeautifulSoup
#
# html = """
# <html>
#   <body>
#     <div class="book">
#       <h2 id="title">Python编程</h2>
#       <p class="price">59.9元</p>
#       <a href="/detail/1">详情</a>
#     </div>
#     <ul class="list">
#       <li>第一项</li>
#       <li>第二项</li>
#     </ul>
#   </body>
# </html>
# """
#
# soup = BeautifulSoup(html2, "lxml")  # 或 "html.parser"
#
# # 按标签查找
# print(soup.find("h2").text)              # Python编程
# print(soup.find_all("li"))               # 所有 li 标签
#
# # 按属性查找
# print(soup.find("p", class_="price").text)  # 59.9元
# print(soup.find(id="title").text)            # Python编程
#
# # CSS 选择器
# print(soup.select_one(".book .price").text)  # 59.9元
# print(soup.select("ul.list li"))              # 所有列表项
#
# # 获取属性
# print(soup.find("a")["href"])             # /detail/1
# print(soup.find("a").get("href"))         # 同上，更安全

import requests
from requests.exceptions import (
    RequestException,
    ConnectionError,
    HTTPError,
    Timeout,
    TooManyRedirects,
)

# url = "https://www.baidu.com/"
url = "https://this-domain-does-not-exist-12345.com"  # ConnectionError
# url = "https://httpbin.org/delay/10"                     # Timeout（timeout设为2时）
# url = "https://httpbin.org/status/404"                   # HTTPError（404）
# url = "https://httpbin.org/status/500"                   # HTTPError（500）


try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # 状态码非200时抛出 HTTPError
except ConnectionError:
    print("网络连接失败")
except Timeout:
    print("请求超时")
except HTTPError as e:
    print(f"HTTP错误：{e}")
except TooManyRedirects:
    print("重定向次数过多")
except RequestException as e:
    print(f"请求异常：{e}")
