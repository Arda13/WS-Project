import time
import pandas as pd

from selenium import webdriver


driver = webdriver.Firefox()
driver.get("https://www.remoteok.io")

title_list = []
location_list = []
company_list = []
tool_list = []

time.sleep(3)

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

time.sleep(3)


titleCount = 0
titles = driver.find_elements_by_xpath("//h2[@itemprop='title']")
for title in titles:
    titleText = title.text
    print(titleText)
    title_list.append(titleText)
    titleCount += 1
    print(titleCount)
    if titleCount == 152:
        break

locationCount = 0
locations = driver.find_elements_by_css_selector("div.location")
for location in locations:
    locationText = location.text
    print(locationText)
    location_list.append(locationText)
    locationCount += 1
    print(locationCount)
    if locationCount == 152:
        break

companyCount = 0
companies = driver.find_elements_by_xpath("//h3[@itemprop='name']")
for company in companies:
    companyText = company.text
    print(companyText)
    company_list.append(companyText)
    companyCount += 1
    print(companyCount)
    if companyCount == 152:
        break

toolsCount = 0
tools = driver.find_elements_by_css_selector('td.tags')
for tool in tools:
    toolText = tool.text
    print(toolText)
    tool_list.append(toolText)
    toolsCount += 1
    print(toolsCount)
    if toolsCount == 152:
        break

driver.quit()

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