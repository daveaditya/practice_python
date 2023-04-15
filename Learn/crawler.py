import requests
from bs4 import BeautifulSoup

#
def get_movies(year,month):

     while month <= month:
        base = "http://www.imdb.com/movies-coming-soon/" + str(year) + "-" + "0" + str(month) + "/?ref_=cs_dt_nx"
        source_code = requests.get(base)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        for link in soup.findAll('a', {'itemprop': 'url'}):
            href = link.get('href')
            if href[1:6] == "title":
                print(link.text)
                get_rating("http://www.imdb.com" + href)
        month += 1
        print("\n")


def get_rating(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    for span in soup.findAll('span',{'itemprop': 'ratingValue'}):
        rating = span.text
        print("\t\t" + "Rating : " + rating)
    for desc in soup.findAll('div', {'class': 'summary_text'}):
        description = desc.text
        print("\t\t" + "Description : " + description)

get_movies(2016,8)
