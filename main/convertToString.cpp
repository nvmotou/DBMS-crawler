#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
	ifstream r;
	ofstream w;
	string info;
	string choice1;
	
	cout<<"��������Ҫת��Ϊ�ַ������ļ���"<<endl;
	cin>>choice1;
	cout<<"������Ŀ����ļ�����"<<endl;
	cin>>choice2;
	r.open(choice1+".txt");
	w.open(choice2+".txt");
	while(!r.eof())
	{
		getline(r,info);
		w<<"'"+info+"'"<<endl;
	}

	w.flush();
	w.close();
	r.close();
	return 0;
}
