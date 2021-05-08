import pandas as pd


df = pd.read_excel(r'spiders/scrapy.xlsx')
print(df)

location_count = df.Location.str.split(expand=True).stack().value_counts(normalize=True) * 100

title_count = df.Title.str.split(expand=True).stack().value_counts(normalize=True) * 100

company_count = df.Company.str.split(expand=True).stack().value_counts(normalize=True) * 100

print(location_count)
print(title_count)
print(company_count)