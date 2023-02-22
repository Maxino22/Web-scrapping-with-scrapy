import scrapy


class CompanysSpider(scrapy.Spider):
    name = 'companies'
    start_urls = [
        "https://yellow.co.ke/categories/food-manufacturing/?page=1",
        "https://yellow.co.ke/categories/food-manufacturing/?page=2",
        "https://yellow.co.ke/categories/food-manufacturing/?page=3",
        "https://yellow.co.ke/categories/food-manufacturing/?page=4",
    ]

    def parse(self, response):
        for company in response.css('div.single-product'):
            yield {
                "title": company.css('h4.title a::text').get().strip(),
                "phone": company.css('div.address-details span a::text').get(),
                " location ": company.css('div.address-details span::text')[0].get()
            }
        # next_page = response.css('ul.pagination li a::attr(href)')[5].get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
