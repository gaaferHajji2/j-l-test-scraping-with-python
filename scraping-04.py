import requests;

from bs4 import BeautifulSoup;

data = requests.get('http://www.pythonscraping.com/pages/warandpeace.html');

bs = BeautifulSoup(data.content, 'lxml');

t1 = bs.find_all('span', attrs={'class': 'green'});

print("The Green Span List Length is: ", len(t1));

for name in t1:
    print(name.get_text());