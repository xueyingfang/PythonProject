import os

def ensure_directory_exists(file_path):
    """确保文件所在的目录存在，若不存在则递归创建"""
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

def write_and_read_file(file_path, content):
    """
    演示文件写入和读取，包含完整的异常处理
    """
    # 1. 确保目录存在（避免写入时目录不存在报错）
    try:
        ensure_directory_exists(file_path)
    except OSError as e:
        print(f"创建目录失败: {e}")
        return

    # 2. 写入文件（使用 'w' 模式，utf-8 编码）
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"成功写入文件: {file_path}")
    except (PermissionError, OSError) as e:
        print(f"写入文件失败 (权限或系统错误): {e}")
        return
    except UnicodeEncodeError as e:
        print(f"写入文件失败 (编码错误): {e}")
        return

    # 3. 读取文件（使用 'r' 模式）
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
        print("读取内容如下:")
        print(data)
    except FileNotFoundError:
        print(f"读取文件失败: 文件 {file_path} 不存在")
    except PermissionError:
        print(f"读取文件失败: 无权限访问 {file_path}")
    except UnicodeDecodeError as e:
        print(f"读取文件失败 (解码错误): {e}")
    except OSError as e:
        print(f"读取文件失败 (系统错误): {e}")

if __name__ == "__main__":
    # 使用原始字符串避免转义问题
    file_path = r"C:\学习\Python\202608191.txt"#前缀 r：防转义，代表原始字符串
    content = "你好，Python！\n今天是2026年8月19日。\n文件读写示例成功！"

    write_and_read_file(file_path, content)