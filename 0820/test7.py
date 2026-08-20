import requests


def fetch_page_info(url):
    """
    爬取指定 URL 的页面信息，并打印基本情况。
    若发生异常，则抛出并显示错误原因。
    """
    # 伪装成常见浏览器，降低反爬风险
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        # 发送 GET 请求，设置超时 10 秒
        response = requests.get(url, headers=headers, timeout=10)

        # 主动检查 HTTP 状态码，若不为 200 则抛出异常
        response.raise_for_status()

        # 获取响应的一些基本信息
        status_code = response.status_code
        encoding = response.encoding  # 服务器返回的编码（可能不准确）
        apparent_encoding = response.apparent_encoding  # 从内容推断的编码
        content_length = len(response.text)  # 字符数

        # 打印页面基本情况
        print(f"请求成功！")
        print(f"   状态码: {status_code}")
        print(f"   服务器声称编码: {encoding}")
        print(f"   实际推断编码: {apparent_encoding}")
        print(f"   页面字符总数: {content_length}")
        print("\n--- 页面源码前 300 个字符 ---")
        print(response.text[:300])  # 预览部分内容
        print("--- 预览结束 ---\n")

        # 如果需要，可以返回响应对象供后续处理
        return response

    except requests.exceptions.Timeout:
        print("请求超时，请检查网络或稍后重试。")
        raise  # 重新抛出异常，让上层处理
    except requests.exceptions.ConnectionError:
        print("网络连接失败（DNS 解析失败、拒绝连接等）。")
        raise
    except requests.exceptions.HTTPError as e:
        print(f"HTTP 错误: {e}（状态码: {response.status_code}）")
        raise
    except requests.exceptions.RequestException as e:
        print(f"请求过程中发生未知异常: {e}")
        raise


if __name__ == "__main__":
    # 目标 URL（微信读书搜索李白的页面）
    target_url = "https://weread.qq.com/web/search/books?author=%E6%9D%8E%E7%99%BD&ii=ce932220813ab691eg017c6c"

    # 调用函数，捕获可能抛出的异常
    try:
        resp = fetch_page_info(target_url)
        # 如果还想进一步处理页面内容，可以在这里写逻辑
    except Exception as e:
        print(f"程序因异常退出: {e}")