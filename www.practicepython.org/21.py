#!/usr/bin/env python3

# 21.py
#
# python-training/www.practicepython.org (c) 2017 by Franco Masotti
#                                        <franco.masotti@student.unife.it>
#
# python-training/www.practicepython.org is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by/4.0/>.

# Take the code from the How To Decode A Website exercise (if you didn’t do it
# or just want to play with some different code, use the code from the
# solution), and instead of printing the results to a screen, write the results
# to a txt file. In your code, just make up a name for the file you are saving
# to. Extras: Ask the user to specify the name of the output file that will be 
# saved.

from bs4 import BeautifulSoup
import requests

def get_web_page(url,filename):
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html, 'html.parser')

    # The with instruction auto closes the file when finished.
    with open(filename, 'w') as storage:
        for title in soup.find_all('h2', {'class': 'story-heading'}):
            storage.write(title.text.strip() + '\n')

if __name__ == '__main__':
    filename = False
    while not filename:
        filename = input("Input a file name for a 'txt' format output: ")

    # Strcat (much esaier than in C).
    filename = filename + '.txt'

    get_web_page('https://www.nytimes.com/', filename)


