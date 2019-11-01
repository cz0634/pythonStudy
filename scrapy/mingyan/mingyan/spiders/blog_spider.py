import scrapy

class blog(scrapy.Spider):
    name = "mingyan2"

    def start_requests(self):
        urls = ['https://www.lbbug.com/class/1.html?page=2']
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        page = response.url.split("=")[1]
        filename = 'mingyan-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('保存文件： %s ' % filename)