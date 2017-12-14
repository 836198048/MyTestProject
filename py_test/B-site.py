# -*- coding:utf-8 -*-
import urllib,gzip,json
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

all_data=[]

def page_serarch():
    z=1
    while(1):
        url='https://bangumi.bilibili.com/web_api/season/index_global?page='+str(z)+'&page_size=20&version=0&is_finish=0&start_year=0&tag_id=&index_type=1&index_sort=0&quarter=0'
        soup = get_soup(url)
        data=json.loads(soup.text)
        #print(data)
        if z%10==0:
            print(z)
        if len(data['result']['list'])==0:
            break
        for i in data['result']['list']:
            all_data.append([i['title'],i['url']])
        z += 1
    bilibili_data=pd.DataFrame(all_data,columns=['动漫标题','网址'])
    writer = pd.ExcelWriter('./B站动漫.xlsx')
    bilibili_data.to_excel(writer,'B站动漫')
    writer.save()
    #print(bilibili_data)

def get_soup(url):
    try:
        webheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = urllib.request.Request(url=url, headers=webheaders)  # 构造请求报头
        webpage = urllib.request.urlopen(req)  # 发送请求报头,timeout=30
    except:
        for i in range(10):
            print('connect error try again:'+str(i+1))
            try:
                webheaders = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate',
                    'Connection': 'keep-alive'
                }
                req = urllib.request.Request(url=url, headers=webheaders)  # 构造请求报头
                webpage = urllib.request.urlopen(req)  # 发送请求报头,timeout=30
                break
            except:
                print('error in:'+url)
    if webpage.headers.get('content-encoding', '') == 'gzip':
        webpage = gzip.decompress(webpage.read()).decode("utf-8")
    soup = BeautifulSoup(webpage, 'lxml')
    return soup

if __name__ == '__main__':
    page_serarch()