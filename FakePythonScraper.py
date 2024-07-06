from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer as ss
import requests as rq
import pandas as pd
import matplotlib.pyplot as plt

#Giving soup the URL
url = 'https://realpython.github.io/fake-jobs/'
webpage = rq.get(url)

# Appended Lists
job_titles = []
company_titles = []
location_titles = []
date_titles = []

#Creating the data map
data = {'Job titles': job_titles, 'Company titles': company_titles, 'Location Title': location_titles, "Date": date_titles}

#Parsing the Website
soup = bs(webpage.content, 'html.parser')

#Finding Job Titles
job_title_tags = soup.find_all('h2')
for job in job_title_tags:
    job_titles.append(job.text.upper())

#Finding Company Names
company_title_tags = soup.find_all('h3')

for company in company_title_tags:
    company_titles.append(company.text.upper())

# Finding Locations and cleaning the results
location_title_tags = soup.find_all(class_='location')

for location in location_title_tags:
    location_titles.append(
        location.text.upper()
        .removeprefix('\n        ')
        .removesuffix(', AA\n      ')
        .removesuffix(', AP\n      ')
        .removesuffix(', AE\n      ')
        )
#Finding the dates and cleaning the results
date_title_tags = soup.find_all(class_='is-small has-text-grey')
for date in date_title_tags:
    date_titles.append(
        date.text.upper()
        .removeprefix('\n')
        .removesuffix('\n')
    )

#Mapping/printing data to dataframe
df = pd.DataFrame(data)
print(df)
#Exporting
df.to_clipboard()
df.to_csv
