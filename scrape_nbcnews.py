
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import csv
 
def web_scarp(headlines):
    len(headlines)
    for i in range(len(headlines)):
        print(headlines[i].text)



if __name__ == "__main__":
    URL="https://www.nbcnews.com/"
    req = requests.get(URL)
    soup = bs(req.content, 'html.parser')
    headlines = soup.find_all('span',{'class':'tease-card__headline'})
    web_scarp(headlines)
    data_nbc = pd.DataFrame(headlines)
    data_nbc.to_csv("nbc_business.csv",mode='a', index= True,header=False)    