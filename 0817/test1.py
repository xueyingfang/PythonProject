# s = "Hello, Python!"
# # 索引与切片
# print(s[0])
# print(s[-1])
# print(s[0:5])
# print(s[7:])
#
# # 常用方法
# print(s.upper())
# print(s.lower())
# print(s.replace("Python", "World"))
# print(s.split(","))
# print(len(s))

# # 字符串格式化
# name = "小明"
# age = 18
# print(f"我叫{name}，今年{age}岁")
# print("我叫{}，今年{}岁".format(name, age))
# print("我叫%s，今年%d岁" % (name, age))
#
# # 多行字符串
# multi_line = """第一行
# 第二行
# 第三行"""
# print(multi_line)

# # 用户交互
# a=int(input("请输入第一个数字：")) #int转化字符串类型
# b=int(input("请输入第二个数字："))
# print(a+b)
#

# Ctrl+Alt+L代码格式化快捷键

# # 条件判断
# a = int(input("请输入你的成绩："))
# if 60 <= a <= 100:
#     print("您的成绩合格。")
# elif 0 <= a < 60:
#     print("不合格。")
# else:
#     print("请输入0-100的数字。")

# # 三元表达式
# age = 20
# status = "成年" if age >= 18 else "未成年"
# print(status)

# # while循环
# a=1
# while a<10:
#     print(a)
#     a=a+1

# a=1
# b=0
# while a<10:
#     print(a)
#     b = a + b
#     a=a+1
# print(b)

# # for 循环
# for i in range(5):  # 0-5
#     print(i, end=" ")
# print()
#
# for i in range(1, 10, 2):  # 1-10（步长为2）
#     print(i, end=" ")
# print()
#
# # 遍历列表
# fruits = ["苹果", "香蕉", "橙子"]
# for index, fruit in enumerate(fruits):
#     print(f"{index}: {fruit}")

# # 创建列表
# fruits = ["苹果", "香蕉", "橙子"]

# # 增删改查
# fruits.append("葡萄")  # 末尾添加
# print(fruits[:])
# fruits.insert(1, "梨")  # 指定位置插入
# print(fruits[:])
# fruits.remove("香蕉")  # 删除指定元素
# print(fruits[:])
# fruits.pop()  # 删除末尾元素
# print(fruits[:])
# fruits[0] = "红苹果"  # 修改元素
# print(fruits[:])

# # 切片
# print(fruits[1:3])  # 第2到第3个元素
# print(fruits[-2:])  # 最后两个元素

# # 常用操作
# print(len(fruits))  # 长度
# print("苹果" in fruits)  # 是否包含
# fruits.sort()  # 排序
# numbers = [3, 1, 4, 1, 5]
# print(sorted(numbers))
#
# # 列表推导式
# squares = [x ** 2 for x in range(1, 6)]
# print(squares)  # [1, 4, 9, 16, 25]

# # 创建字典
# student = {
#     "name": "张三",
#     "age": 20,
#     "major": "计算机"
# }

# # 访问
# print(student["name"])  # 张三
# print(student.get("age"))  # 20
# print(student.get("score", 0))  # 不存在返回默认值 0
#
# # 增删改
# student["score"] = 95  # 添加键值对
# student["age"] = 21  # 修改值
# del student["major"]  # 删除键值对
#
# # 遍历
# for key, value in student.items():
#     print(f"{key}: {value}")
#
# # 常用方法
# print(student.keys())  # 所有键
# print(student.values())  # 所有值
# print(student.items())  # 所有键值对

# # 集合：无序、不重复
# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}
#
# print(s1 & s2)  # 交集：{3, 4}
# print(s1 | s2)  # 并集：{1, 2, 3, 4, 5, 6}
# print(s1 - s2)  # 差集：{1, 2}
#
# # 去重
# nums = [1, 2, 2, 3, 3, 3]
# unique_nums = list(set(nums))
# print(unique_nums)  # [1, 2, 3]

# # 基本函数
# def greet(name, greeting="你好"):
#     return f"{greeting}，{name}！"
#
#
# print(greet("小明"))  # 你好，小明！
# print(greet("小红", "早上好"))  # 早上好，小红！
#
#
# # 可变参数
# def sum_all(*i):
#     return sum(i)
#
#
# print(sum_all(1, 2, 3, 4))
#
#
# def print_info(**user):
#     for key, value in user.items():
#         print(f"{key}: {value}")
#
#
# print_info(name="张三", age=20)
#
# # lambda 匿名函数
# square = lambda x: x ** 2
# print(square(5))

# 高阶函数
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
