from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer as ss
import requests as rq
import pandas as pd
import matplotlib.pyplot as plt

# <h2 class="title is-5">Dispensing optician</h2>

url = 'https://realpython.github.io/fake-jobs/'
webpage = rq.get(url)

job_titles = []
company_titles = []
location_titles = []
date_titles = []


data = {'Job titles': job_titles, 'Company titles': company_titles, 'Location Title': location_titles, "Date": date_titles}


soup = bs(webpage.content, 'html.parser')
job_title_tags = soup.find_all('h2')


#Job Titles
for job in job_title_tags:
    job_titles.append(job.text.upper())

#H3 Tags
company_title_tags = soup.find_all('h3')

for company in company_title_tags:
    company_titles.append(company.text.upper())


location_title_tags = soup.find_all(class_='location')

for location in location_title_tags:
    location_titles.append(
        location.text.upper()
        .removeprefix('\n        ')
        .removesuffix(', AA\n      ')
        .removesuffix(', AP\n      ')
        .removesuffix(', AE\n      ')
        )
    

date_title_tags = soup.find_all(class_='is-small has-text-grey')

for date in date_title_tags:
    date_titles.append(
        date.text.upper()
        .removeprefix('\n')
        .removesuffix('\n')
    )

#print(date_titles)
#print(len(date_titles))

#print(soup.prettify)
df = pd.DataFrame(data)
print(df)
df.to_clipboard()
df.to_csv
