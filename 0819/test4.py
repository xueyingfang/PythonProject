# # 写入文件
# with open("test.txt", "w", encoding="utf-8") as f: # "w"只写，若文件存在则清空，不存在则创建。
#     f.write("今天\n")
#     f.write("20260819\n")

# # 读取文件
# with open("test.txt", "r", encoding="utf-8") as f: # "r"只读（默认），文件必须存在。
#     content = f.read()
#     print(content)

# "\n" 是一个换行符（长度为1）。
# r"\n" 是两个字符：反斜杠和字母 n（长度为2）。
# 逐行读取
# path = "C:\\学习\\Python\\20260819.txt"
path = r"C:\学习\Python\20260819.txt"
with open(path, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# # 追加内容
# with open("test.txt", "a", encoding="utf-8") as f: # "a"追加，写入内容追加到末尾。
#     f.write("追加内容\n")
