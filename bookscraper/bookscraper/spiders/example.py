# to run crawler, 
# cd C:\Users\user\Documents\Universidade\4º ANO\AO\webcrawlers
# scrapy crawl example -o film.json
from genericpath import exists
from numpy import append
import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'
    #allowed_domains = ['example.com']
    start_urls = ['https://www.imdb.com/search/title/?title_type=feature&user_rating=1.0,10.0&runtime=0,1600',
    'https://www.imdb.com/search/title/?title_type=feature&user_rating=1.0,10.0&runtime=0,1600&start=51&ref_=adv_nxt']

    def parse(self, response):
        for filmes in response.css('.lister-item-content'):
            id = filmes.css('span::text').get()[:-1],
            duracao = filmes.css('.runtime ::text').get()[:-4]
            titulo = filmes.css('a::text').get(),
            ano = filmes.css('.lister-item-year.text-muted.unbold ::text').get()[1:-1],
            nota = filmes.css('.inline-block.ratings-imdb-rating strong::text').get(),
            genero = filmes.css('.genre ::text').get()[1:-12]

            yield {
                'id': id, 
                'titulo': titulo, 
                'ano': ano, 
                'nota': nota,
                'duracao': duracao,
                'genero': genero
            }
            
        next_page = response.xpath('//*[@id="main"]/div/div[1]/div[2]/a[2]').attrib['href'] 
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)