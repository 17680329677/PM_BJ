# -*- coding: utf-8 -*-
#实现北京PM2.5的实时监测  网页为：http://www.86pm25.com/city/beijing.html
#数据位于一个table中，使用Pandas套件的read_html导入表格


def rbSite():		#单击监测站按钮后的出来函数
	n = 0
	for s in data.ix[:,0]:		#逐一取得监测站点
		if(s == site.get()):		#如果某监测站点名称与选中的监测站点相同，则取得该站点的PM2.5值
			pm = data.ix[n]['PM2.5浓度']
			pm = pm[:-5]		#去掉后面的5个字符 只取数值部分
			pm = int(pm)		#转化为整型
			if(pd.isnull(pm)):		#如果没有数据，则提示
				result1.set(s+"站当前无PM2.5数据！ ")
			else:
				if(pm <= 35):
					grade1 = "优秀"
				elif(pm <= 53):
					grade1 = "良好"
				elif(pm <= 70):
					grade1 = "中等"
				else:
					grade1 = "差"
				result1.set(s+"站 PM2.5 值为："+str(pm)+";"+grade1)
			break		#找到选中的监测站就跳出循环
		n += 1
		

		
def clickRefresh():		#重新读取数据
	global data
	df = pd.read_html("http://www.86pm25.com/city/beijing.html")
	data = df[0]
	rbSite()		#更新监测站点数据
	
	
def sitemake():		#建立监测站点按钮
	global sitelist,listradio
	for c1 in sitelist:		#逐一建立按钮
		rbtem = tk.Radiobutton(frame1,text=c1,variable=site,value=c1,command=rbSite)
		listradio.append(rbtem)
		if(c1 == sitelist[0]):		#默认选取第一个站点
			rbtem.select()
		rbtem.pack(side="left")		#按钮靠左排列





#用户数据接口配置
import tkinter as tk		#python的GUI编程接口
import pandas as pd
df = pd.read_html("http://www.86pm25.com/city/beijing.html")
data = df[0]
#print(data)		尝试打印该表

win = tk.Tk()
win.geometry("640x270")
win.title("PM2.5 实时监测")		#以上为创建监测的对话框

city = tk.StringVar()		#区县名称变量
site = tk.StringVar()		#监测站点名称变量
result1 = tk.StringVar()		#显示信息变量
citylist = []		#区县列表
sitelist = []		#监测站点列表
listradio = []		#区县按钮列表
#建立监测站列表
for s in data["监测站点"]:
	if(s not in sitelist):
		sitelist.append(s)		#将表格中还不在列表中的监测站点插入
#print(sitelist)

label1 = tk.Label(win,text="监测站点：",font=("新细明体",14))
label1.pack()
frame1 = tk.Frame(win)		#监测站点容器
frame1.pack()
sitemake()		#生成测站点按钮
btnDown = tk.Button(win,text="更新数据",font=("新细明体",14),command=clickRefresh)
btnDown.pack(pady=6)
lblResult1 = tk.Label(win,textvariable=result1,fg='red',font=("新细明体",16))
lblResult1.pack(pady=6)
rbSite()		#显示PM2.5的实时监测值
win.mainloop()





