import random
import tkinter
import urllib.request
from bs4 import BeautifulSoup
import requests

howmanypages = 5
counter = 10
whilecounter = 1
url = "https://www.indeed.co.uk/jobs?q=&l=bb10&radius=10"
page = "&start="

html_content = requests.get(url).text

soup = BeautifulSoup(html_content, 'lxml')

for joblisting in soup.find_all('div', class_='jobsearch-SerpJobCard'):
    jobtitle = joblisting.div.a.text
    companyName = joblisting.span.text

    money1 = joblisting.find('div', class_='salarySnippet')
    if str(money1) != 'None':
        money1 = money1.span.text

    summary = joblisting.find('div', class_='summary').text
    footer = joblisting.find('div', class_='footer')

    if str(footer) != 'None':
        footer = footer.text


    print('Title: ', jobtitle)
    print()
    print('Company Name: ',companyName)
    print()
    print('Salary: ',money1)
    print()
    print('Summary: ',summary)
    print()
    print('Footer: ',footer)

    print('_____________________________')


