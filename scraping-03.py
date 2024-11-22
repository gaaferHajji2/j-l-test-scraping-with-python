from bs4 import BeautifulSoup as bs;

import requests;

data = requests.get('http://pythonscraping.com/pages/page1.html');

t1 = bs(data.content, 'lxml');

print(t1.h1);