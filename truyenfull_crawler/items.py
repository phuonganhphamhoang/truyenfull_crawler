import scrapy

class ChapterItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()

class TruyenItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    genres = scrapy.Field()
    chapters = scrapy.Field()   # list of ChapterItem