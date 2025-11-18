#multi_thread(varzesh3)

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
                get_img(href)
    with open("links.txt","w") as f:
        for link in links:
            f.write(link+"\n")

def get_img(link:str):
    link=link.strip()
    web=requests.get(link)
    soup = BeautifulSoup(web.content, "html.parser")
    dom = etree.HTML(str(soup))
    result = dom.xpath('/html/body/div/div[1]/div/div/div[2]/div[2]/div[2]/div/img')
    if len(result)!=0:
        img = result[0].get('src').strip()
        name=img.split('/')[-1].split('.')[0]
        web = requests.get(img)
        with open("images/" + f"{name}.jpg", "wb") as f:
            f.write(web.content)
    else:
        pass
m=0
while True:
    start=time.time()
    if m >= 120:
        th = threading.Thread(target=get_links, name="th")
        th.start()
        print("new")
        m = 0
    time.sleep(1)
    finish = time.time()
    m += (finish - start)

