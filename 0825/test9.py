import time
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError


class HttpClient:
    """健壮HTTP客户端，基于requests.Session，支持重试、超时、异常处理"""
    def __init__(self, max_retry: int = 2, connect_timeout=3, read_timeout=10):
        self.max_retry = max_retry
        self.timeout = (connect_timeout, read_timeout)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

    def request(self, method: str, url: str, params=None, json_data=None, data=None):
        """
        通用请求方法
        :param method: GET / POST
        :param url: 请求地址
        :param params: get查询参数
        :param json_data: post json体
        :param data: post表单数据
        :return: 成功返回response，失败返回None
        """
        # 使用Session上下文，请求结束自动关闭连接
        with requests.Session() as session:
            session.headers.update(self.headers)

            for attempt in range(1, self.max_retry + 1):
                try:
                    resp = session.request(
                        method=method,
                        url=url,
                        params=params,
                        json=json_data,
                        data=data,
                        timeout=self.timeout
                    )
                    # 4xx、5xx抛出HTTPError异常
                    resp.raise_for_status()
                    return resp

                except Timeout:
                    print(f"[尝试{attempt}/{self.max_retry}] 请求超时")
                except ConnectionError:
                    print(f"[尝试{attempt}/{self.max_retry}] 网络连接失败")
                except RequestException as e:
                    print(f"[尝试{attempt}/{self.max_retry}] 请求异常：{str(e)}")

                # 不是最后一次，等待后重试
                if attempt < self.max_retry:
                    time.sleep(1)

        print(f"全部{self.max_retry}次重试均失败，url={url}")
        return None

    def get(self, url, params=None):
        return self.request("GET", url, params=params)

    def post_json(self, url, json_data=None):
        return self.request("POST", url, json_data=json_data)


if __name__ == "__main__":
    client = HttpClient(max_retry=2)

    # 测试GET请求
    get_resp = client.get("https://httpbin.org/get", params={"username": "demo"})
    if get_resp:
        print("\n===== GET成功 =====")
        print(get_resp.json())

    # 测试POST‑JSON请求
    post_resp = client.post_json("https://httpbin.org/post", json_data={"msg": "hello python"})
    if post_resp:
        print("\n===== POST成功 =====")
        print(post_resp.json())

    # 模拟错误地址，观察重试逻辑
    bad_resp = client.get("https://not.exist.test.xxx")
    if bad_resp is None:
        print("\n错误地址请求按预期失败")
