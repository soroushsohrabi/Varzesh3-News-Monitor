import time
import threading
import requests
from bs4 import BeautifulSoup
from lxml import etree

links=[]
def get_links():
    web=requests.get("https://www.varzesh3.com/")
    soup = BeautifulSoup(web.content, "html.parser")
    dom = etree.HTML(str(soup))
    results = dom.xpath('//*[@id="v3-app"]/div[1]/div/div/div[1]/div[2]/div[3]/div/div[2]/div/div[3]/div/div[1]')
    for r in results:
        tags = r.xpath('.//a/@href')
        for href in tags:
            if href not in links:
                links.append(href)
    with open("links.txt","w") as f:
        for link in links:
            f.write(link+"\n")
m=0
while True:
    start=time.time()
    if m >= 120:
        th = threading.Thread(target=get_links, name="th")
        th.start()
        print("updated")
        m = 0
    time.sleep(1)
    finish = time.time()
    m += (finish - start)

