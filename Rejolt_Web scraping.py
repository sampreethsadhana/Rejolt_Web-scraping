# importing modules
import requests
from bs4 import BeautifulSoup
import csv
import pandas as p

# Scraping the data
url = "https://www.flipkart.com/search?q=mobiles"
r = requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")

titles = soup.find_all('div',class_='KzDlHZ')
ratings = soup.find_all('span',class_='Wphh3N')
reviews = soup.find_all('div',class_='XQDdHH')
prices = soup.find_all('div',class_='Nx9bqj _4b5DiR')

mt = []
mr = []
mre = []
mp = []

for title,rating,rev,pri in zip(titles,ratings,reviews,prices):
    mt.append(title.text)
    mr.append(rating.text)
    mre.append(rev.text)
    mp.append(pri.text)

# saving data in csv

data = {'mt':mt,'mr':mr,'mre':mre,'mp':mp}
model = p.DataFrame(data=data)

model.to_csv("mobilesdata.csv")