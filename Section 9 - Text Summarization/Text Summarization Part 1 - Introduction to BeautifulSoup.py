# Text Summarization using NLP

# Install BeautifulSoup 4 - pip install beautifulsoup4
# Install lxml - pip install lxml

# Importing the libraries
import bs4 as bs
import urllib.request

# Gettings the data source
source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Global_warming').read()

# Parsing the data/ creating BeautifulSoup object
soup = bs.BeautifulSoup(source,'lxml')