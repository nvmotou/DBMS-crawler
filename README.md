# DBMS-crawler
This is my crawler homework using python.
初期探索：
一开始打算使用python自己开发一个专门针对此次作业的爬虫程序，但是由于考虑到以下几个原因而选择了放弃：一.经过对Python爬虫的初步了解，我觉得很难在短期学会Python的基本语法并开发出属于自己的爬虫；二.数据量过大，而我又不具有自己的服务器，数据采集方面存在问题；三.我一开始想利用正则表达式对网页信息进行提取，但是由于对规则的认识过浅、缺乏开发经验，进度实在是太慢了，经过好长一段时间只能做到准确获取到1091个植物的symbol，别的信息都未能正确全部进行提取，这也让我对这条路的选择产生了动摇。
但是在寻找Python爬虫的相关学习资料时我无意间发现了集搜客这个第三方爬虫软件，而且经过短时间的学习我发觉这款软件比较容易上手，操作难度比较低，而且可以使用远端服务器，抓取准确率也比较高，于是我最终选择了使用集搜客对网页信息进行搜集。
整体思路：
首先使用集搜客爬虫软件对三级网页（第一级主页，第二级profile，第三级characteristic）内容进行抓取，并在主页上下载fs和pg的PDF文件到本地。
然后将搜集的网页信息（xml形式）通过xmlmerge-master转化为excel表格的形式，方便统计管理。
接着将PDF进行批量转化，得到大量一一对应的txt和xml文件。（这里用到了pdfminer中的pdf2txt.py，就是利用这个程序对大量PDF进行批处理）
然后利用python对xml文件进行解析，得到黑体字标题，利用这些标题将txt进行分割，得到对应的内容直接生成sql脚本；利用C++程序对抓取到的网页信息进行分析，得到利于导出SQL脚本的形式。
最后将SQL脚本导入数据库。
最后完善阶段：
1.一开始导入由于爬取规则定的存在问题，导致Symbol,Scientific_name和Common_name插入缺值，后经修正使得插入数量正确。
2.插入profile页标签信息时遇到native_status列中内容换行的情况，果断使用了text进行存储。
3.插入characteristic信息和插入pdf信息时发现总提示row size too large的错误使得插入列数较少，后来经过修改表引擎为myisam使得插入列数从197直线上升至525，取得重大突破。
4.在检查时发现由于C++文件流读取规则的问题导致植物的Scientific_name和Common_name出现大量错误，最终将重载运算符改为getline，问题得到解决，并在此时机发现了之前缺少的一个植物的Common_name。
唯一美中不足的地方：在插入有关内容时遇到字符集编码的问题，导致一些列的值插入失败，提示incorrect string，在修改几乎所有字符集为utf-8后问题仍未得到解决，最终放弃。
在制作中对于特殊的信息进行了手动提取（如无Common_name的植物的Symbol和Scientific_name）、特殊的文件（如ccpg开头的文件）进行了手动操作，获取相关内容，将值加入到数据库中。

# EGG-INFO
  这个是pdfminer的egg相关文件
  
# pdfminer
  适用于python2的解析pdf用到的库
  
# requests
  原本用作提取网页的url，后废弃
  
# xmlmerge-master
  github上下载的用于处理集搜客爬虫软件抓取后xml结果文件的库，可以将xml转到excel以表格形式中存储起来
  
# main
  这个是处理数据的主要部分，核心代码都在这里面
  
# converToString.cpp
  将txt文件中的每一行都变为字符串，即在两边加上引号
  
# createBatFile.cpp
  方便制作批处理文件
  
# makeSQL.cpp
  制作SQL脚本
  
# rename.bat
  方便批量重命名文件，用于将文件前缀进行转化
  
# gooseeker.py
  集搜客爬虫软件提供的py文件
  
# pdfToTxt.bat和pdfToXml.bat
  将pdf批量转化为txt和xml
  
# pecessData.cpp
  主要是处理爬虫抓取的PDF数据，方便为集搜客爬虫软件提供线索来下载PDF并为方便字段命名
  
# 各种数据文件
  大部分都是从网页中使用集搜客爬虫软件直接抓取的，少部分手动搜集，大部分根据命名就可以知道是什么内容，其中包括大量的pdf还有转化得到的txt和xml文件，以及经过处理之后得到的txt文件和excel文件
  
# crawler.py
  python实现的提取pdf转化得到的xml信息并根据这些信息对PDF内容进行分割，最终得到字段名和字段的对应值，将其写入txt文件，生成sql脚本
