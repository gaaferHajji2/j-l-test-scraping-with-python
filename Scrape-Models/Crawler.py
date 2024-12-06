import requests;

from bs4 import BeautifulSoup;

from content import Content;

from website import Website;

class Crawler:
    def get_page(self, url):
        try:
            data = requests.get(url);
        except Exception as e:
            print("Error In Get Page: ", e.__str__());
            return None;
        # print("The Data For BS Is: ", data.content);
        return BeautifulSoup(data.content, 'lxml');

    def get_elements(self, bs, selector):
        # select Returns Empty String If No Object Found
        items = bs.select(selector);

        if items is not None and len(items)> 0:
            return '\n'.join([item.get_text().strip() for item in items]);
        else:
            print(f"No Items Found For selector {selector}");

    def get_content(self, website: Website, path) -> Content:
        url = website.url + path;
        bs = self.get_page(url);

        if bs is not None:
            title = self.get_elements(bs, website.titleTag);
            body  = self.get_elements(bs, website.bodyTag);

            return Content(url, title, body);
    
        return Content(url, '', '');