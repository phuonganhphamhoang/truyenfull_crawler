import scrapy
import re

class TruyenSpider(scrapy.Spider):
    name = "truyen_spider"
    allowed_domains = ["truyenfull.vision"]
    start_urls = [
        "https://truyenfull.vision/my-dung-su-xuyen-qua-lam-nong-phu-lam-giau-nuoi-con/"
    ]

    def parse(self, response):
        # ===== Thông tin truyện =====
        title = response.css("h3.title::text").get()
        author = response.css("a[itemprop='author']::text").get()
        genres = response.css(".info-holder a[itemprop='genre']::text").getall()

        self.logger.info(f"Truyện: {title}")
        self.logger.info(f"Tác giả: {author}")

        # ===== Lấy link trang danh sách chương =====
        chapter_links = response.css("ul.list-chapter li a::attr(href)").getall()

        # Nếu trang đầu chưa có list đầy đủ (có pagination)
        if not chapter_links:
            chapter_page = response.url
        else:
            chapter_page = response.url

        yield scrapy.Request(
            chapter_page,
            callback=self.parse_chapter_list,
            meta={
                "title": title,
                "author": author,
                "genres": genres,
            }
        )

    def parse_chapter_list(self, response):
        title = response.meta["title"]
        author = response.meta["author"]
        genres = response.meta["genres"]

        chapters = response.css("ul.list-chapter li a::attr(href)").getall()

        for chapter_url in chapters:
            yield scrapy.Request(
                response.urljoin(chapter_url),
                callback=self.parse_chapter,
                meta={
                    "title": title,
                    "author": author,
                    "genres": genres,
                    "chapter_url": chapter_url,
                }
            )

        # ===== Pagination =====
        current_page = 1
        match = re.search(r'/trang-(\d+)/', response.url)
        if match:
            current_page = int(match.group(1))

        next_page = response.css("a::attr(href)").getall()

        for link in next_page:
            match = re.search(r'/trang-(\d+)/', link)
            if match:
                page_number = int(match.group(1))
                if page_number == current_page + 1:
                    yield response.follow(
                        link,
                        callback=self.parse_chapter_list,
                        meta=response.meta
                    )

    def parse_chapter(self, response):
        title = response.meta["title"]
        author = response.meta["author"]
        genres = response.meta["genres"]

        full_title = response.css("title::text").get()
        chapter_title = full_title.split(":")[1].split("-")[0].strip()
        content_list = response.css("#chapter-c p::text").getall()
        content = "\n".join([c.strip() for c in content_list if c.strip()])

        yield {
            "truyen_title": title,
            "author": author,
            "genres": genres,
            "chapter_title": chapter_title,
            "chapter_url": response.url,
            "content": content,
        }