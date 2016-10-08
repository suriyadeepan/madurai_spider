import scrapy
from bs4 import BeautifulSoup

import json
import os

class MadDocSpider(scrapy.Spider):
    name = 'mad_doc_spider'
    allowed_domains = [ 'projectmadurai.org' ]
    # read from file : index.json
    with open('index.json') as f:
        index = json.load(f)
    start_urls = [ 'http://www.projectmadurai.org/' + row['link'] for row in index ]

    def parse(self, response):
        # get soup from response
        #soup = BeautifulSoup(response.body,'lxml')
        # read doc and yeild context indexed with link
        url = response.url
        # save html to file
        with open('html/' + os.path.basename(url),'wb') as f:
            f.write(response.body)
