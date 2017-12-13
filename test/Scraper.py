# # -*- coding: utf-8 -*-
#
# import scrapy
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
#
#
#
# class ElectronicsSpider(scrapy.Spider):
#     name = "electronics"
#     allowed_domains = ["https://www.nettiauto.com/vaihtoautot?pfrom=3000&pto=7000"]
#     start_urls = [
#         'https://www.nettiauto.com/vaihtoautot?pfrom=3000&pto=7000',
#         'https://www.olx.com.pk/tv-video-audio/',
#         'https://www.olx.com.pk/games-entertainment/'
#     ]
#
#     rules = (
#         Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
#              callback="parse_item",
#              follow=True),)
#
#     def parse_item(self, response):
#         print('Processing..' + response.url)
#
# def main():
#     lul = ElectronicsSpider()
#     lul.parse_item()
# if __name__ == '__main__':
#     main()