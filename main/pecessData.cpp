#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
	ifstream r;
	ofstream w;
	ofstream w1;
	string info[3];
	r.open("data3.txt");
	w.open("data2.txt");
	w1.open("data1x.txt",ios::app);
	int num = 0;
	while(!r.eof())
	{
		for(int i=0;i<3;i++)
		{
			getline(r,info[i]);
		}
		w1<<info[0]<<endl;
		num++;
//		if(info[3]!="") w<<("https://plants.usda.gov/"+info[3])<<endl;
//		if(info[4]!="") w<<("https://plants.usda.gov/"+info[4])<<endl;
	}
	cout<<num<<endl;
	
	w1.flush();
	w1.close();
	w.flush();
	w.close();
	r.close();
	return 0;
}
