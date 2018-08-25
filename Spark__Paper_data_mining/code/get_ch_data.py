"""
	将doc文件转化成txt文件作为语料库使用
"""
import os
from docx import Document


path = './Datasets/origin_data/'
file_list = os.listdir(path)
for file in file_list:
    file_path = path + file
    document = Document(file_path)
    for paragraph in document.paragraphs:
        if '\u4e00' <= paragraph.text[:1] <= '\u9fff':
            with open('./Datasets/ch_data/' + file, 'a+') as fw:
                fw.write(paragraph.text)

