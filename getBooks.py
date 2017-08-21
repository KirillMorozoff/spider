

def getTitle(soup):
    try:
        title = soup.find(id="bookTitle").text
        title = ' '.join(title.split())
        return title
    except AttributeError:
        title = ''
        return title

def getAuthor(soup):
    try:
        author = soup.find(id="bookAuthors").text
        author = ' '.join(author.split())
        return author
    except AttributeError:
        author = ''
        return author

def getRaitingValue(soup):
    try:
        raitingValue = soup.find(attrs={'class' : 'average'}).text
        raitingValue = ' '.join(raitingValue.split())
        return raitingValue
    except AttributeError:
        raitingValue = ''
        return raitingValue

def getRaitings(soup):
    try:
        raitings = soup.find(attrs={'class' : 'votes value-title'}).text
        raitings = ' '.join(raitings.split()).replace(",", "")
        return raitings
    except AttributeError:
        raitings = ''
        return raitings

def getReviews(soup):
    try:
        reviews = soup.find(attrs={'class' : 'count value-title'}).text
        reviews = ' '.join(reviews.split()).replace(",", "")
        return reviews
    except AttributeError:
        reviews = ''
        return reviews

def getPages(soup):
    try:
        pages = soup.find('span', itemprop='numberOfPages').text
        pages = ' '.join(pages.split()).replace(" pages", "")
        return pages
    except AttributeError:
        pages = ""
        return pages

def getPublished(soup):
    try:
        published = soup.find('nobr', attrs={'class' : 'greyText'}).text
        published = ' '.join(published.split()).replace("(", "").replace(")", "")
        return published
    except AttributeError:
        published = soup.find_all('div', attrs={'class' : 'row'})
        try:
            published = str(published[1])
            published = ' '.join(published.split()).replace('<div class="row"> ', "").replace(" </div>", "")
            return published
        except IndexError:
            published = ''
            return published

def getAwards(soup):
    try:
        awards = soup.find('div', itemprop='awards').text
        awards = ' '.join(awards.split())
        return awards
    except AttributeError:
        awards = ""
        return awards

def getGenres(soup):
    genres = soup.find_all('a', attrs={'class' : 'actionLinkLite bookPageGenreLink'})
    i=0
    while i < len(genres):
        genres[i] = genres[i].text
        i = i+1
    genres = str(genres)
    genres = genres.replace("[", "").replace("]", "").replace("'", "")
    return genres

def getLanguage(soup):
    language = soup.find_all('div', attrs={'class' : 'infoBoxRowItem'})
    i=0
    while i < len(language):
        language[i] = language[i].text
        i = i+1
    try:
        language = language[2]
        if len(language) > 10:
            language = ""
        return language
    except IndexError:
        language = ""
        return language

def getISBN(soup):
    ISBN = soup.find_all('div', attrs={'class' : 'infoBoxRowItem'})
    i=0
    while i < len(ISBN):
        ISBN[i] = ISBN[i].text
        i = i+1
    try:
        ISBN = ' '.join(ISBN[1].split())
        return ISBN
    except IndexError:
        ISBN = ''
        return ISBN

def getReadersEnjoyed(soup):
    readersEnjoyed = soup.find_all('li', attrs={'class' : 'cover'})
    i=0
    while i < len(readersEnjoyed):
        readersEnjoyed[i] = readersEnjoyed[i].attrs
        i = i+1
    return str(readersEnjoyed).replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("'class': 'cover', ", "").replace("'", "").replace("id: bookCover_", "")