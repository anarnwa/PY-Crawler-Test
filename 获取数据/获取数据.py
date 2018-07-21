import urllib.request as http
import os
import time
import datetime
sel=input("选择：\n 1.每日信息     2.总计信息\n")
while 1:
    File = open("in.txt")
    t = open("out.txt", "w")
    Time=""
    if sel=="1":
        Time = input("输入查询日期：****-**-**\n四位年份-两位月份-两位日期\n直接回车则默认为今日\n")
        if Time=="":
            now=datetime.datetime.now()
            Time = str(now.strftime('%Y-%m-%d'))
    m=0
    while 1:
        line = File.readline()
        if not line:
            break
        line=line.strip("\n")
        line=line.split(" ")
        phone=line[0]
        name=line[1].replace("space","")
        content = http.urlopen('https://hemaxs.taobao.com/promote/PromoteManage/getLogs.json?phone='+phone+'&param=xr0jCumC%2Fvo%3D').read()
        text=content.decode('utf-8')
        f=text.split('"promtePurchaseCount":')[1].split(',"activityStartTime":')
        y=text.split('"checkStatus":')
        u=f[1].split('000,"purchaseStatus":1')
        cou=0
        if sel!="1":
            if len(y)>0:
                for r,e in enumerate(y):
                    if r!=0:
                        b=y[r].split(',"custAccount":')[0]
                        if b=="1":
                            cou+=1
        if sel=="1":
            if len(u)>1:
                for i in u:
                    p=i[::-1].split(':')[0][::-1]
                    if p!='true}':
                        timeStamp=int(p)
                        localTime = time.localtime(timeStamp) 
                        strTime = time.strftime("%Y-%m-%d", localTime) 
                        if strTime==Time:
                            m+=1
        if sel=="1":
            if name!="":
                print("%s   %s单日下单：%d" % (name , Time ,m), file = t)   #f[0]总计    m单日
            else:
                print("%s   %s单日下单：%d" % (phone ,Time, m), file = t)
        else:
            if name!="":
                print("%s   总计推广次数：%s   有效推广次数：%s   下单次数:%s" % (name ,r,cou, f[0]), file = t)   #f[0]总计    m单日
            else:
                print("%s   总计推广次数：%s   有效推广次数：%s   下单次数:%s" % (phone ,r,cou, f[0]), file = t)
        m=0
        cou=0
    t.close()
    File.close();
    os.system("out.txt")
    os.system("cls")
    if sel!="1":
        break

    

