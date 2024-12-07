from scrapy.linkextractors import LinkExtractor;

from scrapy.spiders import CrawlSpider, Rule;

class ArticlesSpider(CrawlSpider):

    name = 'articles';

    allowed_domains = ['wikipedia.org']

    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life'];