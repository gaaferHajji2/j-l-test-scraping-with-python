import requests;

from bs4 import BeautifulSoup;

import re;

import datetime;

import random;

random.seed(datetime.datetime.now().__str__());

def getLinks(article_url):
    data = requests.get(f'http://en.wikipedia.org{article_url}');
    bs = BeautifulSoup(data.content, 'lxml');

    return bs.find('div', { 'id': 'bodyContent' }) \
    .find_all('a', { 'href': re.compile('^(/wiki/)((?!:).)*$') });

links = getLinks('/wiki/Kevin_Bacon');

while len(links) > 0:
    new_article = links[random.randint(0, len(links) - 1)].attrs['href'];

    print("We Choose Random New Article: ", new_article);

    links = getLinks(new_article);