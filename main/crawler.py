from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
import requests
import re
import os
import time
from lxml import etree
from selenium import webdriver
from gooseeker import GsExtractor
# from io import open

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


# 获取网页内容
r = requests.get('https://plants.usda.gov/java/factSheet?sort=factSheet')
data = r.text
# data.replace('<')

# 利用正则查找指定的内容
# pattern = re.compile("href=\"profile\?symbol=(\w*)\" target=\"")
# res = pattern.search('forum/ABC/topic/CDF').groups()

symbols = re.findall(r"scope=\"row\">(\w*)</th>\r\n        <td class=\"resultsind1\">[\s\S]*?</td>", data)
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
    """
    while i < len(sci_name):
        if(i!=len(sci_name)-1):
            sci_names[pos] += (sci_name[i] + " ")
        else:
            sci_names[pos] += sci_name[i]
        i += 1
    """
    # print (sci_names[pos])
    # print (com_names[pos])
    coreWebdata = requests.get('https://plants.usda.gov/core/profile?symbol=' + symbols[pos])
    pos += 1


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