# Scraping Project Madurai


Visit [Project Madurai](http://www.projectmadurai.org/pmworks.html).


## Prerequisites


1. Scrapy
2. Beautiful Soup

## Steps


* Get the [title, author, genre, link] to html documents by parsing the table

```bash
scrapy crawl madurai_spider -o index.json
```

* Crawl the links and write to html/

```bash
scrapy crawl mad_doc_spider
```

* *What next?*

I plan to build a toy semantic search engine by first constructing *tamil word embeddings*, then encoding all the documents into fixed length vectors in a high dimensional space. Build an index (n-dimensional) based on the encodings. When the user enters a query in tamil, it is encoded into a fixed length vector (n-dimensional) and a beam search is performed to identify neighboring vectors that represent html documents. This ensures a *strong* semantic similarity between the query and the results.
