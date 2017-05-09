#!/usr/bin/env python3

# 17.py
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

# Use the BeautifulSoup and requests Python packages to print out a list of all 
# the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

# Thsis was possible thanks to this:
# https://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html

# Get the excerpts from the homepage
def simpler_example():
    url = 'https://frnmst.gitlab.io'
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html, 'html.parser')
    # print (soup.prettify())
    #print (soup.title)

    # Take out the <div> of name and get its value
    for e in soup.find_all('div', class_='excerpt'):
        print(e.text)

def nyt():
    url = 'https://www.nytimes.com/'
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html, 'html.parser')

    # Two ways: since class is a reserved keyword in python an alternative way 
    # is needed.
    # for title in soup.find_all('h2', class_='story-heading'):
    for title in soup.find_all('h2', {'class': 'story-heading'}):
        print(title.text.strip())

def main():
    nyt()
    # simpler_example()


main()
