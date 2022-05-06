from urllib import request
from http import client
import requests
from bs4 import BeautifulSoup
import os

url = 'https://tripleler.tistory.com/entry/test'
try:
    page = requests.get(url)
except Exception:
    print('error')
else:
    if page.status_code == 200:
        print('success')
    else:
        print('not response')


def get_url_source(url):
    try:
        f = request.urlopen(url)
        url_info = f.info()
        url_charset = client.HTTPMessage.get_charsets(url_info)[0]
        url_source = f.read().decode(url_charset)
        return url_source

    except Exception:
        pass


page_source = get_url_source(url)
print(type(page_source))
soup = BeautifulSoup(page_source, 'html.parser')
print(type(soup))
contents = soup.find('div', 'tt_article_useless_p_margin contents_style').find_all('figure')
print(contents)

file_urls = [content.find('a').attrs['href'] for content in contents]


def download(url, file_name):
    with open(file_name, "wb") as f:
        response = requests.get(url)
        f.write(response.content)


path = './downloads'
os.makedirs(path, exist_ok=True)
for file_url in file_urls:
    file_name = file_url.split('?')[0].split('/')[-1]
    download(file_url, path + '/' + file_name)
