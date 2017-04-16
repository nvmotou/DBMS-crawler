#include <iostream>
#include <fstream>
#include <string>
using namespace std;
void createTable();
void insertSci();
void insertSciCom();
void insertPro();
void insertChar();
int main()
{
	while(1)
	{
		cout<<"请输入你想生成的sql脚本的编号："<<endl;
		cout<<"1.创建初始表并插入主键symbol"<<endl;
		cout<<"2.插入只有scientific name而没有common name的植物的scientific name"<<endl;
		cout<<"3.插入拥有scientific name和common name的植物的scientific name和common name"<<endl;
		cout<<"4.插入profile页面中的黑体标签"<<endl;
		cout<<"5.插入characteristic页面中的信息"<<endl;
		cout<<"6.退出"<<endl;
		int choice = 0;
		cin>>choice;
		switch(choice)
		{
		case 1:
			createTable();
			break;
		case 2:
			insertSci();
			break;
		case 3:
			insertSciCom();
			break;
		case 4:
			insertPro();
			break;
		case 5:
			insertChar();
			break;
		case 6:
			break;
		}
		if(choice==6) break;
	}
	
	return 0;
}
void createTable()
{
	ofstream w;
	ifstream r;
	string symbol = "";
	
  	r.open("Main_Symbol.txt");
  	w.open("createTable.txt");
  	w<<"create table usdaplant(Symbol varchar(20) primary key);"<<endl;
	while(!r.eof())
	{
		getline(r,symbol);
		w<<"insert into usdaplant(Symbol) values("+symbol+");"<<endl;
	}
	
	r.close();
	w.flush();
	w.close();
}
void insertSci()
{
	ofstream w;
	string noProfile[3];
	ifstream r;

	r.open("In_Sci.txt");
	w.open("insertSci.txt");
	w<<"alter table usdaplant add column Scientific_Name varchar(50);"<<endl;
	for(int i=0;i<39;i++)
	{
		for(int j=0;j<3;j++)
			getline(r,noProfile[j]);
		w<<"update usdaplant set Scientific_Name = '"+noProfile[1]+"' where Symbol='"+noProfile[0]+"';"<<endl;
	}
	
	r.close();
	w.flush();
	w.close();
}
void insertSciCom()
{
	ifstream sym;
	ifstream sci;
	ifstream com;
	ofstream w;
	string profile[3];
	
	w.open("insertSciCom.txt");
	w<<"alter table usdaplant add column Scientific_Name varchar(50);"<<endl;
	w<<"alter table usdaplant add column Common_Name varchar(50);"<<endl;
	sym.open("symbol1.txt");
	sci.open("sci.txt");
	com.open("com.txt");
	for(int i=0;i<1052;i++)
	{
		getline(sym,profile[0]);
		getline(sym,profile[1]);
		getline(sym,profile[2]);
		w<<"update usdaplant set Scientific_Name = '"+profile[1]+"' where Symbol='"+profile[0]+"';"<<endl;
		w<<"update usdaplant set Common_Name = '"+profile[2]+"' where Symbol='"+profile[0]+"';"<<endl;
	}
	
	w.flush();
	w.close();
	sym.close();
	sci.close();
	com.close();
}
void insertPro()
{
	ifstream tabsf[5];
	ofstream w;
	ifstream r4;
	string symbol1;
	string tab[5]={"Group1","Family","Duration","Growth_Habit","Native_Status"};
	string tabv[5];

	for(int i=0;i<5;i++)
	{
		tabsf[i].open(tab[i]+".txt");
	}
	r4.open("Pro_Symbol.txt");
	w.open("insertPro.txt");
	for(int i=0;i<1052;i++)
	{
		getline(r4,symbol1);
		for(int j=0;j<5;j++)
		{
			getline(tabsf[j],tabv[j]);
			if(j<4)
			{
				w<<"drop procedure if exists schema_change;"<<endl;
				w<<"delimiter ';;';"<<endl;
				w<<"create procedure schema_change()"<<endl;
				w<<"begin"<<endl;
				w<<"if not exists (select * from information_schema.columns where table_name = 'usdaplant' and column_name = '"+tab[j]+"') then"<<endl;
				w<<"alter table usdaplant add column "+tab[j]+" varchar(50);"<<endl;
				w<<"end if;"<<endl;
				w<<"end;;"<<endl;
				w<<"delimiter ';';"<<endl;
				w<<"call schema_change();"<<endl;
				w<<"drop procedure if exists schema_change;"<<endl;
				w<<"update usdaplant set "+tab[j]+" ="+tabv[j]+" where Symbol="+symbol1+";"<<endl;
			}
			else
			{
				w<<"drop procedure if exists schema_change;"<<endl;
				w<<"delimiter ';;';"<<endl;
				w<<"create procedure schema_change() begin"<<endl;
				w<<"if not exists (select * from information_schema.columns where table_name = 'usdaplant' and column_name = '"+tab[j]+") then"<<endl;
				w<<"alter table usdaplant add column "+tab[j]+" text;"<<endl;
				w<<"end if;"<<endl;
				w<<"end;;"<<endl;
				w<<"delimiter ';';"<<endl;
				w<<"call schema_change();"<<endl;
				w<<"drop procedure if exists schema_change;"<<endl;
				w<<"update usdaplant set "+tab[j]+" ="+tabv[j]+" where Symbol="+symbol1+";"<<endl;
			}
		}
	}


	w.flush();
	w.close();
	r4.close();
	for(int i=0;i<5;i++)
	{
		tabsf[i].close();
	}
}
void insertChar()
{
	ifstream r1,r2,r3;
	string symbol = "";
	string name = "";
	string value = "";
	ofstream w;
	
	r1.open("Char_Symbol.txt");
	r2.open("Char_Col.txt");
	r3.open("Char_Value.txt");
	w.open("insertChar.txt");
	while(!r1.eof())
	{
		getline(r1,symbol);
		getline(r2,name);
		getline(r3,value);
		w<<"drop procedure if exists schema_change;"<<endl;
		w<<"delimiter ';;';"<<endl;
		w<<"create procedure schema_change() begin"<<endl;
		w<<"if not exists (select * from information_schema.columns where table_name = 'usdaplant' and column_name = '"+name+"') then"<<endl;
		w<<"alter table usdaplant add column "+name+" text;"<<endl;
		w<<"end if;"<<endl;
		w<<"end;;"<<endl;
		w<<"delimiter ';';"<<endl;
		w<<"call schema_change();"<<endl;
		w<<"drop procedure if exists schema_change;"<<endl;
		w<<"update usdaplant set "+name+" ="+value+" where Symbol='"+symbol+"';"<<endl;
	}
	
	w.flush();
	w.close();
	r1.close();
	r2.close();
	r3.close();
}
