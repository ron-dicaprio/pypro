#-*-coding:utf-8 -*-
#!/usr/bin/env python
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
from os import path

def split_pdf(self):
    # 判断是否存在该文件
    if path.exists(self):
        with open(self, 'rb') as input_file:
            # 初始化PDF实体类
            pdf_file = PdfFileReader(input_file)
            # 获取文档页码
            pages = pdf_file.getNumPages()
            # 逐页拆分
            for i in range(pages):
                # 根据传入的路径获取文件名
                filename = path.split(self)[-1]
                # 过滤一下没有后缀的文件
                if '.' in filename:
                    # 拆分后的文件名称
                    newname = filename.split('.')[0] + '_' + str(i+1) + '.pdf'
                    # 构建空文本实体类
                    pdf_writer = PdfFileWriter()
                    # 空文本实体类写入特定页数的内容
                    pdf_writer.addPage(pdf_file.getPage(i))
                    # 新文件落地路径
                    filepath = path.split(self)[0] + '\\' + newname
                    print(filepath)
                    # 写入拆分的
                    with open(file=filepath, mode='wb') as outputfile:
                        pdf_writer.write(outputfile)
    else:
        print('sys error! file not found!')
        exit(-1)

def comb_pdf(self):
    self = list(self)
    print('1')
    # 初始化PDF实体类
    pdf_combine = PdfFileMerger()
    # list循环append到pdf_combine
    for pdf in self:
        pdf_combine.append(open(pdf, 'rb'))
    # 定义输出的pdf路径
    outfile = path.split(self[0])[0] + '\\' + 'combine.pdf'
    print(outfile)
    # 二进制流写入pdf文档
    with open(outfile, 'wb+') as fileout:
        pdf_combine.write(fileout)
