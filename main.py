import requests
from html import unescape
from bs4 import BeautifulSoup
content = requests.get("https://www.timeout.com/film/best-movies-of-all-time")
data = content.text
soup = BeautifulSoup(data, "html.parser")
list_h3 = soup.find_all(name='h3', class_='_h3_cuogz_1')
for each in list_h3:
    with open("movies_list.txt", mode='a') as m_list:
        movie = unescape(each.getText())
        print(f"{movie}\n")
        m_list.write(f"{each.getText()}\n")