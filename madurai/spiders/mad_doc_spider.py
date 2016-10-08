import scrapy
from bs4 import BeautifulSoup

class MadDocSpider(scrapy.Spider):
    name = 'mad_doc_spider'
    allowed_domains = [ 'projectmadurai.org' ]
    # read from file : index.json
    #start_urls = 
    root_url = 'http://www.projectmadurai.org/utf8/'

    def parse(self, response):
        # get soup from response
        soup = BeautifulSoup(response.body,'lxml')
        # read doc and yeild context indexed with link

