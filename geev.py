from bs4 import BeautifulSoup
from config import GEEV_URL
import requests

def search():

    res = requests.get(GEEV_URL)

    if res.ok:
        soup = BeautifulSoup(res.text,'html.parser')
        posts = soup.findAll('molecule-ad-card')
        
        posts_to_push = []
        
        for element in posts:

            try:
                pfp = element.findAll('img')[1]['src']
            except:
                pfp = "https://images.geev.fr/63c1a1c8937a20001227ad0b/squares/32"

            # 30x30 -> 1000x1000
            pict = element.find('img')['src'].split("/")
            pict[-1] = "1000"
            pict = '/'.join(pict)

            item = {
                "name": element.find('span',{'class':'mol-itemCard-description-title glob-font-body-bold'}).text.strip(),
                "distance": element.find('li').text,
                "link": "https://www.geev.com" + element.find('a')['href'],
                "picture": pict,
                "pfp": pfp
            }

            posts_to_push.insert(0,item)
            
        return posts_to_push