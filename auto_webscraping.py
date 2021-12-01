import requests
from bs4 import BeautifulSoup

yt_link = 'https://www.youtube.com/feed/trending'

responce = requests.get (yt_link)
print ('status code' , responce.status_code)
# print ('output' , responce.text)

with open ('trending.html' , 'w') as f:
  f.write(responce.text)

soup = BeautifulSoup(responce.text , 'html.parser')

print ( "page title:" , soup.title.text)

