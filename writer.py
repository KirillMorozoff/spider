import getBooks
from bs4 import BeautifulSoup
import requests
import sqlite3 as lite
from proxies import proxyDict_1
from proxies import proxyDict_2

def parse_and_write(count_start, count_end, proxy_dic):
    i = count_start
    while i < count_end:
        url = 'https://www.goodreads.com/book/isbn/' + str(i)
        r = requests.get(url, proxies=proxy_dic)
        soup = BeautifulSoup(r.content, "html.parser")
        con = lite.connect('books.db')
        with con:
            cur = con.cursor()
            # Вносим данные
            cur.execute("INSERT INTO books VALUES('" + str(i) + "', '" + getBooks.getTitle(soup).replace("'", "") + "', '" + getBooks.getAuthor(soup).replace("'", "") + "', '" + getBooks.getRaitingValue(soup).replace("'", "") + "', '" + getBooks.getRaitings(soup).replace("'", "") + "', '" + getBooks.getReviews(soup).replace("'", "") + "', '" + getBooks.getPages(soup).replace("'", "") + "', '" + getBooks.getPublished(soup).replace("'", "") + "', '" + getBooks.getAwards(soup).replace("'", "").replace("'", "") + "', '" + getBooks.getGenres(soup).replace("'", "") + "', '" + getBooks.getLanguage(soup).replace("'", "") + "', '" + getBooks.getISBN(soup).replace("'", "") + "', '" + getBooks.getReadersEnjoyed(soup).replace("'", "") + "')")
        con.commit()
        print(str(i))
        i=i+1