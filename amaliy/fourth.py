import requests
from bs4 import BeautifulSoup

url = "https://kun.uz"


response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

a_tag_soup = soup.find_all('a')

links = []

for a_tag in a_tag_soup:
    href = a_tag.get('href')
    if href:
        links.append(href)

with open("links.txt", "w", encoding="utf-8") as file:
    for link in links:
        file.write(link + "\n")

print(f"{len(links)} ta havola links.txt fayliga saqlandi.")