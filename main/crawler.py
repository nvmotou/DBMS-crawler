from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

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

"""# 获取网页内容
r = requests.get('https://plants.usda.gov/java/factSheet?sort=factSheet')
data = r.text

# 利用正则查找所有链接
link_list=re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", data)
for url in link_list:
    print url"""