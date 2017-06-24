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
