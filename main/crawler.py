"""
from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from io import StringIO
import requests
import re
import os
import time
from lxml import etree
from selenium import webdriver
from gooseeker import GsExtractor
from pdfminer.layout import *
import io
import sys
"""
# from io import open
import xml.dom.minidom
import string
import re



# 解析xml文件并得到标题
file1= open("pdfNames.txt","r")
content = ''
content1 = ''
count = 0
while 1:
    line = file1.readline()
    if not line:
        break
    line = line.strip()
    symbol = line[3:len(line)]
    dom = xml.dom.minidom.parse('data_2/'+line+'.xml')
    b = line
    if line.find('cs_') != -1:
        strinfo = re.compile('cs_')
        b = strinfo.sub('pg_', line)
    root = dom.documentElement
    itemlist1 = root.getElementsByTagName('textline')
    i = 0
    begin1 = -1
    end1 = -1
    title = ''
    for item1 in itemlist1:
        content = ''
        itemlist = item1.getElementsByTagName('text')
    # itemlist = root.getElementsByTagName('text')
        for item in itemlist:
            isize = item.getAttribute('size')
            ifont = item.getAttribute('font')
            if isize == '13.357' and ifont == 'TimesNewRomanPS-BoldMT':
                content = content + item.firstChild.data
        if content!='' and content!=' ':
            # 已经得到一个标题
            name = title
            title = content.strip()
            x = re.findall('[a-zA-Z0-9]+', title)
            title = '_'.join(x)
            f1 = open('data_1/' + b + ".txt",'r',encoding='utf-8')
            text1 = f1.read()
            f1.close()
            if i == 0:
                begin1 = text1.find(content)
                i = 1
            else:
                end1 = text1.find(content, begin1)
                text2 = text1[begin1+len(content1)+1:end1]
                begin1 = end1
                # 本来是打算写到文件里面的，但是由于C++抓取txt全部内容不如python方便所以使用Python生成sql脚本
                f = open('pymakesql.txt',"a+",encoding='utf-8')
                f.write("drop procedure if exists schema_change;\n")
                f.write("delimiter ';;';\n")
                f.write("create procedure schema_change()\n")
                f.write("begin\n")
                f.write("if not exists (select * from information_schema.columns where table_name = 'usdaplant' and column_name = '" + b[0:2]+'_'+name + "') then\n")
                f.write('alter table usdaplant add COLUMN '+b[0:2]+'_'+name+' LongText;\n')
                f.write("end if;\n")
                f.write("end;;\n")
                f.write("delimiter ';';\n")
                f.write("call schema_change();\n")
                f.write("drop procedure if exists schema_change;\n")
                f.write('update usdaplant set '+b[0:2]+'_'+name+' = \''+text2+'\' where Symbol = \''+symbol.upper()+'\';\n')
                # f = open("D:/pythonProjects/DBMS-crawler/main/data_3/" + b + "_" + name + ".txt", "w", encoding='utf-8')
                # f.write('\''+text2+'\'')
                # f.close()
            content1 =content
    count += 1
    print ('已经完成'+str(count)+'个文件！请稍等...')



"""
file1= open("data4.txt","r")
while 1:
    line = file1.readline()
    if not line:
        break
    line = line.strip('\n')
    file2 = open('D:/pythonProjects/DBMS-crawler/main/data_3/'+line+'.txt','r')
    file3 = open('D:/pythonProjects/DBMS-crawler/main/data_3/' + line + '.txt', 'r')
    line3 = file3.readline()
    line2 = line3
    while 1:
        line3 = file2.readline()
        if not line3:
            break
        title = line2.strip()
        colname = title.replace(' ', '_')
        c = colname.replace('/','_')
        fullname = 'D:/pythonProjects/DBMS-crawler/main/data_4/' + line + '_' + c + '.txt'
        if open(fullname, 'w',encoding= 'utf-8'):
            file3 = open(fullname, 'w',encoding= 'utf-8')
        file4 = open('D:/pythonProjects/DBMS-crawler/main/data_1/' + line + '.txt', 'r',encoding= 'utf-8')
        text1 = file4.read()
        file4.close()
        begin1 = text1.find(line2)
        end1 = text1.find(line3,begin1)
        text2 = text1[begin1+1:end1]
        file3.write('\''+text2+'\'')
        file3.close()
        line2 = line3
"""

"""
def convert_pdf(path, page=1):
    path = "data/" + path + ".pdf"
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, pageno=page, laparams=laparams)
    fp = open(path, 'rb')
    process_pdf(rsrcmgr, device, fp)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str

file1= open("data4.txt")
while 1:
    line = file1.readline()
    if not line:
        break
    line = line.strip('\n')
    f = open("data_1/" + line + ".txt", "w+")
    print(convert_pdf(line), file=f)
"""


"""
def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

pdfFile = urlopen("https://plants.usda.gov/factsheet/pdf/fs_abba.pdf")
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()
"""


"""
# 获取网页内容
r = requests.get('https://plants.usda.gov/java/factSheet?sort=factSheet')
data = r.text
# data.replace('<')

# 利用正则查找指定的内容
# pattern = re.compile("href=\"profile\?symbol=(\w*)\" target=\"")
# res = pattern.search('forum/ABC/topic/CDF').groups()

symbols = re.findall(r"<td class=\"resultsind1\">([\s\S]*?)</td>", data)
sci_names = []# re.findall(r"Fact Sheet for (\w*) in Word Format", data)
com_names = []# re.findall(r"</a></td><td>(\w*\s*\w*)</td>", data)
pos = 0
print(len(symbols))
# href="/factsheet/doc/fs_abba.docx"
# <td><a href="profile?symbol=ACKO2" target="_top"><em>Acacia</em> <em>koaia</em></a></td><td>koaoha</td>
while pos < len(symbols) :
    # print (symbols[pos])
    # pattern1 = re.compile(r"scope=\"row\">" + symbols[pos] + "[\s\S]*?</td>")
    # sousuo = pattern1.findall(data)
    # print(len(sousuo))
    # pattern2 = re.compile(r"<em>(\w*)</em>")
    # sci_name = pattern2.search(sousuo).groups()
    # i = 0
    
    while i < len(sci_name):
        if(i!=len(sci_name)-1):
            sci_names[pos] += (sci_name[i] + " ")
        else:
            sci_names[pos] += sci_name[i]
        i += 1
    # print (sci_names[pos])
    # print (com_names[pos])
    # coreWebdata = requests.get('https://plants.usda.gov/core/profile?symbol=' + symbols[pos])
    pos += 1
"""


"""
driver = webdriver.Chrome()
url = 'https://plants.usda.gov/java/factSheet?sort=factSheet'
driver.get(url)
#等待2秒，根据动态网页加载耗时进行自定义
#time.sleep(2)
content = driver.page_source.encode('utf-8')
doc = etree.HTML(content)
bbsExtra = GsExtractor()
bbsExtra.setXsltFromAPI("8df2d8dbe99c35601696bf6d5f2f7951", "plants_1")
result = bbsExtra.extract(doc)
current_path = os.getcwd()
file_path = current_path + "/result-2.xml"
open(file_path,"wb").write(result)
print(str(result).encode('gbk','ignore').decode('gbk'))
"""

