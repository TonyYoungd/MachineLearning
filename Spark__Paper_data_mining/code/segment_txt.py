"""
    对生成的txt文档进行分词
"""
import jieba
jieba.load_userdict('./corpus/dict/dict.txt')
f1 = open("./corpus/1/data.txt")
f2 = open("./corpus/1/fenci.txt", 'w')
content = f1.read()  # 读取全部内容
content = content.replace('\r\n', '').strip()  # 删除换行
content = content.replace(' ', '').strip()  # 删除空行、多余的空格
content_seg = jieba.cut(content)  # 为文件内容分词
f2.write(' '.join(content_seg))
f1.close()
f2.close()