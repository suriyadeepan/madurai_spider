import scrapy
from bs4 import BeautifulSoup

class MaduraiSpider(scrapy.Spider):
    name = 'madurai_spider'
    allowed_domains = [ 'projectmadurai.org' ]
    start_urls = ['http://www.projectmadurai.org/pmworks.html']
    root_url = 'http://www.projectmadurai.org'

    def parse(self, response):
        # get soup from response
        soup = BeautifulSoup(response.body,'lxml')
        '''
        # get all links
        links = soup.findAll('a')
        # filter links to get unicode html docs;
        #   and yield
        for doc_link in links:
            if 'href' in doc_link.attrs:
                if '/utf8/' in doc_link.get('href'):
                    yield { 'link' : root_url + link.get('href') }
        '''
        # Scrape from table instead
        table = soup.find('table', attrs={'class':'sortable'})
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')

        for row in rows:
            cols = row.find_all('td')
            '''
            print('>> title: '  + cols[1].text + '\n')
            print('> author: ' + cols[2].text + '\n')
            print('> genre: '  + cols[3].text + '\n')
            if 'href' in cols[5].find('a').attrs:
                print('> link: '   + self.root_url + cols[5].find('a').get('href') + '\n')
            '''
            if 'href' in cols[5].find('a').attrs:
                yield { 
                        'title'  : cols[1].text, 
                        'author' : cols[2].text,
                        'genre'  : cols[3].text,
                        'link'   : cols[5].find('a').get('href')
                        }

#    def parse_docs(self, response):

