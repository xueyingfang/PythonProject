# 异常处理

# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     # 捕获特定异常后的处理
#     print("除数不能为零！")

# try:
#     num = int(input("输入数字："))
# except ValueError:
#     print("不是有效数字")
# else:
#     # 没有异常时才执行
#     print(f"你输入的是 {num}")
# finally:
#     # 无论是否异常都执行（常用于释放资源）
#     print("程序结束")

# try:
#     int("abc")
# except ValueError as e:
#     print(f"异常类型：{type(e).__name__}")
#     print(f"异常信息：{e}")
#     # e.args 是异常的参数元组
#     print(f"异常参数：{e.args}")

# # 捕获所有 Exception 子类（但不捕获 KeyboardInterrupt 等）
# def risky_operation():
#     """模拟一个可能抛出各种异常的操作"""
#     return 10 / 0  # 这里会触发 ZeroDivisionError
# try:
#     risky_operation()
# except Exception as e:
#     print(f"捕获到异常：{e}")

# 注意：尽量不要用裸 except，会捕获包括 KeyboardInterrupt 在内的所有异常

# def set_age(age):
#     if age < 0:
#         raise ValueError("年龄不能为负数")
#     if age > 150:
#         raise ValueError("年龄不合理")
#     return age
#
# try:
#     set_age(151)
# except ValueError as e:
#     print(e)

# # 继承 Exception 或其子类
# class BusinessError(Exception):
#     """业务异常基类"""
#     pass
#
# class InsufficientBalanceError(BusinessError):
#     """余额不足异常"""
#     def __init__(self, balance, amount):
#         self.balance = balance
#         self.amount = amount
#         super().__init__(f"余额不足：当前余额 {balance}，需要 {amount}")
#
# # 使用
# try:
#     raise InsufficientBalanceError(100, 200)
# except InsufficientBalanceError as e:
#     print(e)  # 余额不足：当前余额 100，需要 200

# def load_config(path):
#     try:
#         with open(path) as f:
#             return f.read()
#     except FileNotFoundError as e:
#         # 保留原始异常链，便于调试
#         raise RuntimeError("配置文件加载失败") from e
#
# try:
#     load_config("nonexistent.ini")
# except RuntimeError as e:
#     print(f"外层异常：{e}")
#     print(f"原始异常：{e.__cause__}")
