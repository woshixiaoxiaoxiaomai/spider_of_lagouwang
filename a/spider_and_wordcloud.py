#coding=utf-8
import lxml;
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
"""
    html="https://www.lagou.com/zhaopin/shenduxuexi"
    
    res=urlopen(html)
    bsobj=bs(res)
    #for link in bsobj.finaAll("a",{"class":"position_link"}):
     #   if 'href' in link.attrs:
     #       print(link.attrs['href'])
    
    #print(bsobj.findAll("a",{"class","position_link"}))
    totalpages=bsobj.find("input",{"id":"totalPageCountSEO"})
    pagescount=int(totalpages.attrs["value"])
    f=open("D:/urls.txt","a+");
    while(pagescount>1):
        #print(pagescount)
        #print(pagescount-1)
        html = "https://www.lagou.com/zhaopin/shenduxuexi"+"/"+str(pagescount)
        res = urlopen(html)
        bsobj = bs(res)
        print("downloading %d page"%pagescount)
        for link in bsobj.findAll("a",{"class":"position_link"}):
            if "href" in link.attrs:
                print(link.attrs["href"])
                f.write(link.attrs["href"])
                f.write("\n")
        pagescount=pagescount-1
    
    
    f.close()
    #totalpages=bsobj.find("input",{"id":"totalPageCountSEO"})
    #print(totalpages.attrs["value"])
"""

def geturls(self,urll):
    html = "https://www.lagou.com/zhaopin/"+urll  #shenduxuexi

    res = urlopen(html)
    bsobj = bs(res)
    # for link in bsobj.finaAll("a",{"class":"position_link"}):
    #   if 'href' in link.attrs:
    #       print(link.attrs['href'])

    # print(bsobj.findAll("a",{"class","position_link"}))
    totalpages = bsobj.find("input", {"id": "totalPageCountSEO"})
    pagescount = int(totalpages.attrs["value"])
    f = open("D:/urls.txt", "a+");
    while (pagescount > 1):
        # print(pagescount)
        # print(pagescount-1)
        html = "https://www.lagou.com/zhaopin/"+urll + "/" + str(pagescount)
        res = urlopen(html)
        bsobj = bs(res)
        print("downloading %d page" % pagescount)
        for link in bsobj.findAll("a", {"class": "position_link"}):
            if "href" in link.attrs:
                print(link.attrs["href"])
                f.write(link.attrs["href"])
                f.write("\n")
        pagescount = pagescount - 1

    f.close()
    # totalpages=bsobj.find("input",{"id":"totalPageCountSEO"})
    # print(totalpages.attrs["value"])

def getjob_description(self):
    f1 = open("D:/urls.txt", "r")
    f2 = open("D:/jobbt.txt", "a+", encoding="utf-8")
    url = f1.readline();
    while url:
        res = urlopen(url)
        # res1=bs(res.read())
        bsobj = bs(res)
        jobname = bsobj.find("span", {"class": "ceil-job"})
        print(jobname.get_text())
        f2.write(jobname.get_text())
        # jobbt=bsobj.findAll("dd",{"class":"job_bt"}).div.p
        jobbt = bsobj.find("dd", {"class": "job_bt"}).find("div", {})  # .findALL("p",{})
        # print(jobbt)
        for i in jobbt.findAll("p", {}):
            ii = i.get_text()
            # ii.replace(u"\xa0",u"")
            print(ii)

            f2.write(ii)
            f2.write("\t")
        f2.write("\n")
        url = f1.readline()

    f1.close()
    f2.close()
import jieba
import wordcloud
import jieba.posseg as pseg
f=open("D:/jobbt.txt","r",encoding="utf-8")
r1=f.readline()
dic={}
print(r1)
i=0
while r1:
    words=pseg.cut(r1)
    for word,flag in words:
        #print('%s,%s'%(word,flag))
        if(flag=='eng'):# or flag=="n"):
            #print('%s,%s'%(word,flag))
            word=word.lower()
            if(word in dic):
                dic[word]=dic[word]+10
            else:dic[word]=1
    #print(dic)
    r1=f.readline()
    i=i+1
    print(i)
    print(len(dic))
f.close()
print(dic)

b=sorted(dic.items(),key=lambda item:item[1],reverse=True)
#print(b)
b=b[1:100]
dd={}
total=0
for i in b:
    total=total+i[1]
for i in b:
    print(i)
    dd[i[0]]=i[1]/total

#from scipy.misc import imread
#import numpy as np
#from PIL import Image
#from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt
#alice_coloring = imread("F:/python程序/例题/网络爬虫/yxdown/a.png")
alice_coloring = np.array(Image.open( "a.png"))
wc = WordCloud(background_color="white", #背景颜色max_words=2000,# 词云显示的最大词数
#mask=alice_coloring,#设置背景图片
stopwords=STOPWORDS.add("said"),
max_font_size=40, #字体最大值
random_state=42).generate_from_frequencies(dd)
#image_colors = ImageColorGenerator(alice_coloring)

plt.figure()
plt.imshow(wc)
plt.axis("off")
plt.show()
    # 以下代码显示图片
"""    
    plt.imshow(wc)
    plt.axis("off")
    # 绘制词云
    plt.figure()
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
    plt.imshow(wc.recolor(color_func=image_colors))
    plt.axis("off")
    # 绘制背景图片为颜色的图片
    plt.figure()
    plt.imshow(alice_coloring, cmap=plt.cm.gray)
    plt.axis("off")
    plt.show()
    # 保存图片
    wc.to_file("名称.png")
"""
