from bs4 import BeautifulSoup as BS
import pandas as pd
import requests
from urllib.request import Request, urlopen

urls = ['https://remoteok.io/?pagination=1620463662&worldwide=false','https://remoteok.io/?pagination=1620136820&worldwide=false','https://remoteok.io/?pagination=1619802411&worldwide=false','https://remoteok.io/?pagination=1619562412&worldwide=false','https://remoteok.io/?pagination=1619099398&worldwide=false','https://remoteok.io/?pagination=1618862987&worldwide=false','https://remoteok.io/?pagination=1618523785&worldwide=false','https://remoteok.io/?pagination=1618342031&worldwide=false','https://remoteok.io/?pagination=1618000671&worldwide=false','https://remoteok.io/?pagination=1617759427&worldwide=false']
title_list = []
location_list = []
company_list = []
tool_list = []

for url in urls:
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    bs = BS(response.content, 'html.parser')


    ### Job Title ###
    bs_title = bs.find_all('h2', {'itemprop':'title'})
    for title in bs_title:
        titles = title.get_text()
        title_list.append(titles)


    ### Location ###
    bs_location = bs.find_all('div', {'class':'location'})
    for location in bs_location:
        locations = location.get_text()
        location_list.append(locations)




    ### Company ###
    bs_company = bs.find_all('h3', {'itemprop':'name'})
    for company in bs_company:
        companies = company.get_text()
        company_list.append(companies)



    ### Tools ###
    bs_tools = bs.find_all('td', {'class':'tags'})
    for tool in bs_tools:
        tools = tool.get_text()
        tool_list.append(tools)




Job_Title = pd.DataFrame(title_list)

Location = pd.DataFrame(location_list)

Company = pd.DataFrame(company_list)

Tools = pd.DataFrame(tool_list)

Job_Title = Job_Title.rename(columns={0: 'Title'})
Location = Location.rename(columns={0: 'Location'})
Company = Company.rename(columns={0: 'Company'})
Tools = Tools.rename(columns={0: 'Tools'})

Remote = pd.concat([Job_Title, Company, Location, Tools], axis=1, join="inner")
location_count = Remote.Location.str.split(expand=True).stack().value_counts(normalize=True) * 100
print(location_count)

title_count = Remote.Title.str.split(expand=True).stack().value_counts(normalize = True) * 100
print(title_count)

company_count = Remote.Company.str.split(expand=True).stack().value_counts(normalize = True) * 100
print(company_count)

tools_count = Remote.Tools.str.split(expand=True).stack().value_counts(normalize = True) * 100
print(tools_count)