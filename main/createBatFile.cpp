#include<iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
	ifstream r;
	ofstream w1;
	ofstream w2;
	string fname;
	
	r.open("data4.txt");
	w1.open("D:/pythonProjects/DBMS-crawler/main/pdfToTxt.txt",ios::app);
	w2.open("D:/pythonProjects/DBMS-crawler/main/pdfToXml.txt",ios::app);
	while(!r.eof())
	{
		getline(r,fname);
		w1<<"python2 D:/python/python2.7.13/Scripts/pdf2txt.py -o D:/pythonProjects/DBMS-crawler/main/data_1/"+fname+".txt D:/pythonProjects/DBMS-crawler/main/data/"+fname+".pdf"<<endl;
		w2<<"python2 D:/python/python2.7.13/Scripts/pdf2txt.py -o D:/pythonProjects/DBMS-crawler/main/data_1/"+fname+".xml D:/pythonProjects/DBMS-crawler/main/data/"+fname+".pdf"<<endl;
	}
	
	w1.flush();
	w1.close();
	w2.flush();
	w2.close();
	r.close();
	return 0;
}
