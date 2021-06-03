from bs4 import BeautifulSoup
import requests
import csv
import urllib
from PIL import Image

headers = {
    'authority': 'www.amazon.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}


while True:
    print("enter q to quit")
    pro = input("enter your product name ")
    if pro =='q':
        break
    url = "https://www.amazon.in/s?k=" + pro + "&ref=nb_sb_nosssams"
    # print(url)
    source = requests.get(url, headers=headers, proxies=urllib.request.getproxies()).text
    soup = BeautifulSoup(source, 'lxml')
    for i in soup.find_all('div',class_="s-expand-height s-include-content-margin s-border-bottom s-latency-cf-section"):
        t=i.h2.span.text
        print(i.h2.span.text)
        vids = i.find('img', class_='s-image')['src']
        print(vids)
        try:
            print(i.i.span.text)
            a=i.find('span',class_="a-offscreen")
            price=a.text
            print("price:",end=" ")
            print(a.text)
        except:
            pass
    for i in soup.find_all('div',class_="a-section a-spacing-medium a-text-center"):
         t = i.h2.span.text
         print(i.h2.span.text)
         vids = i.find('img', class_='s-image')['src']
         print(vids)
         try:
            print(i.i.span.text)
            a = i.find('span', class_="a-offscreen")
            price=a.text
            print("price:" ,end=" ")
            print(a.text)
         except:
            pass
    for i in soup.find_all('div', class_="s-include-content-margin s-border-bottom s-latency-cf-section"):
        t=i.h2.span.text
        print(i.h2.span.text)
        vids = i.find('img', class_='s-image')['src']
        print(vids)
        try:
            print(i.i.span.text)
            a = i.find('span', class_="a-offscreen")
            price=a.text
            print("price:",end=" ")
            print(a.text)
        except:
            pass

