class medscraper(scrapy.Spider):
    name = "cass"

    # Function. like this constructor in JS
    def start_requests(self):
        list_of_urls = ["https://medium.com/", "https://medium.com/@rukshandanadir/7-html-tags-you-didnt-know-existed-21812c9cc8d5"]

        for url in list_of_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Function runs until sees another function (def) at same indent
    def parse(self, response):
        print(response.css("img::attr(src)").extract())