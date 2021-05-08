import scrapy
import pandas as pd
import time

title_list = []
location_list = []
company_list = []
tool_list = []



class RemoteSpider(scrapy.Spider):
    name = "remote"



    def start_requests(self):
        urls = [
            'https://remoteok.io/?pagination=1620463662&worldwide=false',
            'https://remoteok.io/?pagination=1620136820&worldwide=false',
            'https://remoteok.io/?pagination=1619802411&worldwide=false',
            'https://remoteok.io/?pagination=1619562412&worldwide=false',
            'https://remoteok.io/?pagination=1619099398&worldwide=false',
            'https://remoteok.io/?pagination=1618862987&worldwide=false',
            'https://remoteok.io/?pagination=1618523785&worldwide=false',
            'https://remoteok.io/?pagination=1618342031&worldwide=false',
            'https://remoteok.io/?pagination=1618000671&worldwide=false',
            'https://remoteok.io/?pagination=1617759427&worldwide=false'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'text/html'}, encoding='utf-8')

    def parse(self, response):
        title = response.xpath('//h2[@itemprop="title"]/text()').getall(),
        titleText = [title for title in title]
        desiredTitle =next(iter(titleText))
        for tit in desiredTitle:
            title_list.append(tit)

        location = response.xpath('//div[@class="location tooltip"]/text()').getall(),
        locationText = [location for location in location]
        desiredLocation = next(iter(locationText))
        for loc in desiredLocation:
            location_list.append(loc)

        company = response.xpath('//h3[@itemprop="name"]/text()').getall(),
        companyText = [company for company in company]
        desiredCompany = next(iter(companyText))
        for com in desiredCompany:
            company_list.append(com)

        tools = response.xpath('//td[@class="tags"]/a/text()').getall(),
        toolsText = [tools for tools in tools]
        desiredTools = next(iter(toolsText))
        for too in desiredTools:
            tool_list.append(too)

        Job_Title = pd.DataFrame(title_list)

        Location = pd.DataFrame(location_list)

        Company = pd.DataFrame(company_list)

        Tools = pd.DataFrame(tool_list)

        Job_Title = Job_Title.rename(columns={0: 'Title'})
        Location = Location.rename(columns={0: 'Location'})
        Company = Company.rename(columns={0: 'Company'})
        Tools = Tools.rename(columns={0: 'Tools'})

        Remote = pd.concat([Job_Title, Company, Location, Tools], axis=1, join="inner")

        Remote.to_excel('scrapy.xlsx')


