from bs4 import BeautifulSoup
import requests

def main():

    url = 'https://life.ru/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        
        allNews = []
        soup = BeautifulSoup(res.text, "html.parser")
        allNews = soup.findAll('a', class_ ='StyledLink-sc-1wu5ik4-0 iYqATD')

        temp = [] 
        
        for x in allNews: 
            if x not in temp: 
                temp.append(x) 
        allNews = temp

        for data in allNews:
            print(data.text)
    else:
        print("Error conection")
            

main()
