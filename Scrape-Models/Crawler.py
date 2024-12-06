import requests;

from bs4 import BeautifulSoup;

from content import Content;

from website import Website;

class Crawler:
    def getPage(self, url):
        try:
            data = requests.get(url);
        except Exception as e:
            print("Error In Get Page: ", e.__str__());
            return None;
        return BeautifulSoup(data.content, 'lxml');

    def getElements(self, bs, selector):
        # select Returns Empty String If No Object Found
        items = bs.select(selector);

        if items is not None and len(items)> 0:
            return '\n'.join([item.get_text().trim() for item in items]);
        else:
            print(f"No Items Found For selector {selector}");

    def getContent(self, website: Website, path) -> Content:
        url = website.url + path;
        bs = self.getPage(url);

        if bs is not None:
            title = self.getElements(bs, website.titleTag);
            body  = self.getElements(bs, website.bodyTag);

            return Content(url, title, body);
    
        return Content(url, '', '');