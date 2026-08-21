# pip install pandas

# import requests
#
# # GET 请求
# resp = requests.get("https://httpbin.org/get", params={"name": "张三"})
# print(resp.status_code)   # 200
# print(resp.json())        # 解析 JSON 响应
#
# # POST 请求
# resp = requests.post(
#     "https://httpbin.org/post",
#     data={"key": "value"},
#     headers={"User-Agent": "Mozilla/5.0"},
#     timeout=10
# )
# print(resp.text)
#
# # 下载图片
# resp = requests.get("https://httpbin.org/image/png")
# with open("image.png", "wb") as f:
#     f.write(resp.content)


# pip install numpy

# import pandas as pd
#
# # ========== 1. 创建数据并保存 ==========
# data = {
#     "姓名": ["张三", "李四", "王五"],
#     "年龄": [20, 21, 19],
#     "成绩": [85, 92, 78],
# }
# df = pd.DataFrame(data)
#
# # 保存为 Excel（需要 openpyxl）
# df.to_excel("data.xlsx", index=False)
# print("文件已保存：data.xlsx")
#
# # ========== 2. 读取 Excel ==========
# # 手动指定 engine，避免格式判断失败
# df = pd.read_excel("data.xlsx", engine="openpyxl")
# print(df)
#
# # ========== 3. 常用操作 ==========
# print("\n--- 前2行 ---")
# print(df.head(2))
#
# print("\n--- 统计描述 ---")
# print(df.describe())
#
# print("\n--- 成绩大于80的记录 ---")
# print(df[df["成绩"] > 80])
#
# print("\n--- 新增等级列 ---")
# df["等级"] = df["成绩"].apply(lambda x: "优秀" if x >= 90 else "良好")
# print(df)


# pip install numpy

# import numpy as np
#
# # 创建数组
# arr = np.array([1, 2, 3, 4, 5])
# matrix = np.array([[1, 2], [3, 4]])
#
# # 常用生成
# print(np.zeros((2, 3)))       # 全零矩阵
# print(np.ones((2, 2)))        # 全一矩阵
# print(np.arange(0, 10, 2))    # [0 2 4 6 8]
# print(np.random.rand(3, 3))   # 随机矩阵
#
# # 运算
# print(arr.mean())    # 平均值
# print(arr.sum())     # 求和
# print(arr.max())     # 最大值
# print(matrix.T)      # 转置
# print(np.dot(matrix, matrix))  # 矩阵乘法


# pip install beautifulsoup4 lxml
# from bs4 import BeautifulSoup
#
# html = """
# <div class="book">
#     <h2>Python编程</h2>
#     <p class="price">59.9元</p>
#     <a href="/detail/1">查看详情</a>
# </div>
# """
#
# soup = BeautifulSoup(html, "html.parser")
#
# # 查找元素
# print(soup.find("h2").text)              # Python编程
# print(soup.find("p", class_="price").text)  # 59.9元
# print(soup.find("a")["href"])            # /detail/1
#
# # CSS 选择器
# print(soup.select_one(".book h2").text)  # Python编程
# print(soup.select("div.book"))           # 所有匹配元素


# pip install matplotlib

# import matplotlib.pyplot as plt
#
# # 设置中文显示
# plt.rcParams["font.sans-serif"] = ["SimHei"]
# plt.rcParams["axes.unicode_minus"] = False
#
# # 折线图
# x = [1, 2, 3, 4, 5]
# y = [10, 15, 13, 18, 16]
# plt.plot(x, y, marker="o", label="销售额")
# plt.title("月度销售趋势")
# plt.xlabel("月份")
# plt.ylabel("销售额（万元）")
# plt.legend()
# plt.savefig("chart.png", dpi=150)
# plt.show()
#
# # 柱状图
# plt.bar(["A", "B", "C"], [30, 50, 20])
# plt.show()


# from openpyxl import Workbook, load_workbook
# from openpyxl.styles import Font, Alignment, PatternFill
#
# # 创建工作簿
# wb = Workbook()
# ws = wb.active
# ws.title = "学生成绩"
#
# # 写入数据
# ws["A1"] = "姓名"
# ws["B1"] = "成绩"
# ws.append(["张三", 85])
# ws.append(["李四", 92])
#
# # 设置样式
# ws["A1"].font = Font(bold=True, color="FFFFFF")
# ws["A1"].fill = PatternFill("solid", fgColor="4472C4")
# ws["A1"].alignment = Alignment(horizontal="center")
#
# # 调整列宽
# ws.column_dimensions["A"].width = 15
#
# wb.save("scores.xlsx")
#
# # 读取文件
# wb = load_workbook("scores.xlsx")
# ws = wb["学生成绩"]
# for row in ws.iter_rows(values_only=True):
#     print(row)


# pip install python-docx

# from docx import Document
# from docx.shared import Pt, Inches
# from docx.enum.text import WD_ALIGN_PARAGRAPH
#
# doc = Document()
#
# # 标题
# title = doc.add_heading("工作报告", level=0)
# title.alignment = WD_ALIGN_PARAGRAPH.CENTER
#
# # 段落
# p = doc.add_paragraph("这是第一段内容。")
# p.add_run("加粗部分").bold = True
# p.add_run("，正常部分。")
#
# # 列表
# doc.add_paragraph("第一项", style="List Bullet")
# doc.add_paragraph("第二项", style="List Bullet")
#
# # 表格
# table = doc.add_table(rows=3, cols=2)
# table.style = "Table Grid"
# table.cell(0, 0).text = "姓名"
# table.cell(0, 1).text = "年龄"
# table.cell(1, 0).text = "张三"
# table.cell(1, 1).text = "25"
#
# doc.save("report.docx")


# pip install pillow

# from PIL import Image, ImageFilter, ImageDraw, ImageFont
#
# # 打开图片
# img = Image.open("chart.png")
# print(img.size, img.mode)   # (宽度, 高度)  RGB
#
# # 缩放
# img_resized = img.resize((400, 300))
#
# # 裁剪
# img_cropped = img.crop((100, 100, 500, 400))  # 左, 上, 右, 下
#
# # 旋转
# img_rotated = img.rotate(90)
#
# # 滤镜
# img_blur = img.filter(ImageFilter.GaussianBlur(radius=5))
#
# # 加水印文字
# font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 60)
# draw = ImageDraw.Draw(img)
# draw.text((100, 100), "我的水印", font=font, fill=(255, 0, 0, 128))
#
# # 保存和格式转换
# img.save("output.png")
# img.save("output.webp", "WEBP")


# pip install tqdm

# from tqdm import tqdm
# import time
#
# # 基本用法
# for i in tqdm(range(100)):
#     time.sleep(0.05)
#
# # 带描述
# for item in tqdm(["a", "b", "c"], desc="处理中"):
#     time.sleep(0.5)
#
# # 处理列表
# data = list(range(1000))
# result = [x * 2 for x in tqdm(data, desc="计算")]


# pip install python-dateutil

# from dateutil.parser import parse
# from dateutil.relativedelta import relativedelta
# from datetime import datetime
#
# # 灵活解析各种日期字符串
# print(parse("2024-01-15"))           # 2024-01-15 00:00:00
# print(parse("Jan 15, 2024"))         # 2024-01-15 00:00:00
# print(parse("15/01/2024", dayfirst=True))  # 2024-01-15
#
# # 日期加减（支持年月）
# now = datetime.now()
# print(now + relativedelta(months=1))     # 一个月后
# print(now + relativedelta(years=1))      # 一年后
# print(now - relativedelta(days=10))      # 十天前
#
# # 计算两个日期差
# d1 = parse("2024-01-01")
# d2 = parse("2025-03-15")
# diff = relativedelta(d2, d1)
# print(f"{diff.years}年{diff.months}月{diff.days}天")


# pip install pypdf2 pdfplumber
# pip install pdfplumber pypdf2 fpdf2

# # ============================================================
# # 0. 先生成两个示例 PDF（
# # ============================================================
# from fpdf import FPDF
# from fpdf.enums import XPos, YPos  # 新增：导入新的位置枚举
#
# def create_sample_pdf(filename, title, content):
#     """生成一个简单的 PDF 文件"""
#     txt = ""
#     ln = False
#     pdf = FPDF()
#     pdf.add_page()
#     # 设置字体（fpdf2 内置支持Unicode的字体）
#     pdf.add_font("msyh", "", "C:/Windows/Fonts/msyh.ttc")
#     pdf.set_font("msyh", size=16)
#     pdf.cell(
#         200, 10,
#         text=title,
#         new_x=XPos.LMARGIN,
#         new_y=YPos.NEXT,
#         align="C"
#     )
#     pdf.set_font("msyh", size=12)
#     pdf.multi_cell(0, 10, text=content)
#     pdf.output(filename)
#     print(f"已生成：{filename}")
#
# create_sample_pdf("1.pdf", "第一份文档", "这是第一份PDF的内容。\n作者：张三\n日期：2024年")
# create_sample_pdf("2.pdf", "第二份文档", "这是第二份PDF的内容。\n包含更多文字信息。")
#
#
# # ============================================================
# # 1. pdfplumber 提取文字和表格
# # ============================================================
# import pdfplumber
#
# print("\n" + "=" * 50)
# print("使用 pdfplumber 提取 1.pdf 的内容")
# print("=" * 50)
#
# try:
#     with pdfplumber.open("1.pdf") as pdf:
#         print(f"总页数：{len(pdf.pages)}")
#         for i, page in enumerate(pdf.pages, 1):
#             print(f"\n--- 第 {i} 页 ---")
#             text = page.extract_text()
#             if text:
#                 print(text)
#             else:
#                 print("（该页无文字内容）")
#
#             # 提取表格（如果有）
#             tables = page.extract_tables()
#             if tables:
#                 print(f"\n找到 {len(tables)} 个表格：")
#                 for table in tables:
#                     for row in table:
#                         print(row)
# except FileNotFoundError as e:
#     print(f"文件不存在：{e}")
# except Exception as e:
#     print(f"读取PDF失败：{e}")
#
#
# # ============================================================
# # 2. PyPDF2 合并多个 PDF
# # ============================================================
# from PyPDF2 import PdfReader, PdfWriter
#
# print("\n" + "=" * 50)
# print("使用 PyPDF2 合并 1.pdf 和 2.pdf")
# print("=" * 50)
#
# try:
#     writer = PdfWriter()
#
#     # 依次读取并添加每一页
#     for filename in ["1.pdf", "2.pdf"]:
#         reader = PdfReader(filename)
#         print(f"添加 {filename}，共 {len(reader.pages)} 页")
#         for page in reader.pages:
#             writer.add_page(page)
#
#     # 写入合并后的文件
#     with open("merged.pdf", "wb") as f:
#         writer.write(f)
#     print("合并完成：merged.pdf")
#
# except FileNotFoundError as e:
#     print(f"文件不存在：{e}")
# except Exception as e:
#     print(f"合并失败：{e}")
#
#
# # ============================================================
# # 3. PyPDF2 拆分 PDF（提取指定页）
# # ============================================================
# print("\n" + "=" * 50)
# print("从 merged.pdf 中提取第1页保存为单独文件")
# print("=" * 50)
#
# try:
#     reader = PdfReader("merged.pdf")
#     writer = PdfWriter()
#     writer.add_page(reader.pages[0])  # 只加第1页（索引从0开始）
#
#     with open("page1.pdf", "wb") as f:
#         writer.write(f)
#     print("已保存：page1.pdf")
# except Exception as e:
#     print(f"拆分失败：{e}")


