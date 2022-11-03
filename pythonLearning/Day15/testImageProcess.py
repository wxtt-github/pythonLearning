from PIL import Image, ImageFilter

image = Image.open('./pythonLearning/Day15/graph.jpg')

# 展示图像
# image.format, image.size, image.mode
# ('JPG', (500,750), 'RGB')
# image.show()

# 剪裁图像
# rect = 10, 10, 20, 20
# image.crop(rect).show()

# 生成缩略图
# size = 128, 128
# image.thumbnail(size)
# image.show()

# 缩放和黏贴图像
# image1 = Image.open('./pythonLearning/Day15/graph.jpg')
# image2 = Image.open('./pythonLearning/Day15/graph.jpg')
# rect = 80, 20, 310, 360
# guido_head = image2.crop(rect)
# width, height = guido_head.size
# image1.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))
# image1.show()

# 旋转和翻转
# image.rotate(180).show()
# image.transpose(Image.FLIP_LEFT_RIGHT).show()

# 操作像素
# for x in range(80, 310):
#     for y in range(20, 360):
#         image.putpixel((x, y), (128, 128, 128))
# image.show()

# 滤镜效果
image = Image.open('./pythonLearning/Day15/graph1.jpg')
image.filter(ImageFilter.CONTOUR).show()

# 处理Excel电子表格
# import datetime

# from openpyxl import Workbook

# wb = Workbook()
# ws = wb.active

# ws['A1'] = 42
# ws.append([1, 2, 3])
# ws['A2'] = datetime.datetime.now()

# wb.save("sample.xlsx")

# 处理word文档
# from docx import Document
# from docx.shared import Inches

# document = Document()

# document.add_heading('Document Title', 0)

# p = document.add_paragraph('A plain paragraph having some ')
# p.add_run('bold').bold = True
# p.add_run(' and some ')
# p.add_run('italic.').italic = True

# document.add_heading('Heading, level 1', level=1)
# document.add_paragraph('Intense quote', style='Intense Quote')

# document.add_paragraph(
#     'first item in unordered list', style='List Bullet'
# )
# document.add_paragraph(
#     'first item in ordered list', style='List Number'
# )

# document.add_picture('monty-truth.png', width=Inches(1.25))

# records = (
#     (3, '101', 'Spam'),
#     (7, '422', 'Eggs'),
#     (4, '631', 'Spam, spam, eggs, and spam')
# )

# table = document.add_table(rows=1, cols=3)
# hdr_cells = table.rows[0].cells
# hdr_cells[0].text = 'Qty'
# hdr_cells[1].text = 'Id'
# hdr_cells[2].text = 'Desc'
# for qty, id, desc in records:
#     row_cells = table.add_row().cells
#     row_cells[0].text = str(qty)
#     row_cells[1].text = id
#     row_cells[2].text = desc

# document.add_page_break()

# document.save('demo.docx')
