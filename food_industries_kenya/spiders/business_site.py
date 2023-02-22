import scrapy


class BusinessSiteSpider(scrapy.Spider):
    name = "business"
    start_urls = [
        "https://www.businesslist.co.ke/category/food-manufacturing",
        "https://www.businesslist.co.ke/category/food-manufacturing/2",
        "https://www.businesslist.co.ke/category/food-manufacturing/3"

    ]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'COOKIES_ENABLED': False,
        'DOWNLOAD_DELAY': 2,
    }

    def parse(self, response):
        nested_page_url = response.css(
            "div.company h4 a::attr(href)").extract()

        for url in nested_page_url:
            yield scrapy.Request(url, callback=self.parse_nested_page)

    def parse_nested_page(self, response):
        title = response.css("div.info #company_name::text").get()
        phone = response.css("div.info .phone::text").get()
        location = response.css("div.info .location::text").get()

        yield {
            "title": title,
            "phone": phone,
            "location": location
        }
