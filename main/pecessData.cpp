#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
	ifstream r;
	ofstream w;
	string info[7];
	r.open("data1.txt");
	w.open("data2.txt");
	while(!r.eof())
	{
		for(int i=0;i<7;i++)
		{
			getline(r,info[i]);
		}
		if(info[3]!="") w<<("https://plants.usda.gov/"+info[3])<<endl;
		if(info[4]!="") w<<("https://plants.usda.gov/"+info[4])<<endl;
	}
	
	w.flush();
	w.close();
	r.close();
	return 0;
}
