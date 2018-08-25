"""
    提取原始文件中的关键词。并保存在key_words文件夹中
"""

import docx
import os
import re
import jieba

filename = './Datasets/origin_data/'
stop_words = ['', '']


for name in os.listdir(filename):
    txt = docx.Document(filename+name)
    paras = txt.paragraphs
    for i in range(len(paras)):
        duan = []
        if paras[i].text[0:2] == '关键':
            seg_list = jieba.cut(paras[i].text, cut_all=False)
            # 使用正则表达式切分关键词
            seg_list = re.split('[ :,，：关键词\u3000]', paras[i].text)
            for word in seg_list:
                if word not in stop_words:
                    if word != '\t':
                        duan.append(word)
            with open('./Datasets/key_words/'+name, 'a') as fl:
                for line in duan:
                    fl.write(line+' ')
                fl.write('\n')
