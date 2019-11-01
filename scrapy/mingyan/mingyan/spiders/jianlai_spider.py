import scrapy

class jianlai(scrapy.Spider):
    name = "jl"

    def start_requests(self):
        urls = ['https://www.x11kt.com/read/131441/31598936.html']
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        title = response.css('.bdsub dl dd')[0].css('h1::text').extract_first()
        title = title.replace('正文 ', '')
        content = response.xpath('string(//dd[@id="contents"])').extract_first()
        content = content.replace('\r\n\r\n', '\r\n')
        with open('jl\\%s.txt' % '剑来', 'a', encoding='utf-8') as f:
            f.write(title + '\r\n')
            f.write(content + '\r\n')
            self.log(title)
        # contentArr = response.css('#contents::text').extract()
        # for each in contentArr:
        #     with open('jl\\%s.txt' % title, 'a', encoding='utf-8') as f:
        #         f.write(each)
        #         self.log(each)

        next_page = 'https://www.x11kt.com' + response.css('.bdsub dd')[1].css('h3 a:nth-child(3)::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)