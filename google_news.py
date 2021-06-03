from bs4 import BeautifulSoup
import requests
import csv
source=requests.get('https://news.google.com').text
soup=BeautifulSoup(source,'lxml')
#print(soup.prettify())
#print(article)
csv2=open('cms.csv','w')
csvw=csv.writer(csv2)
csvw.writerow(['heading','link','time'])
i=-1;
article=soup.find_all("article")
for article in soup.find_all('article'):
    try:

        for a in article.find_all('h3'):
            ai=article.h3.text
            time=article.time.text
            link=a.find('a')['href']
            link='https://news.google.com'+link
            print(ai)
            print(link)
            print(time)
            csvw.writerow([ai,link,time])
    except:
        None
csvw.writerow(['sub-heading','link','time'])
csvw.writerow(['-','-','-'])

for article in soup.find_all('article'):
        try:
            for b in article.find_all('h4'):
                bii=article.h4.text
                time=article.time.text
                print(bii)
                link=a.find('a')['href']
                link='https://news.google.com'+link
                print(link)
                print(time)

                csvw.writerow([bii,link,time])
        except:
             None
csv2.close()




