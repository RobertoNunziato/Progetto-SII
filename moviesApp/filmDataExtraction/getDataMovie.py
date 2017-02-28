from tmdb3 import set_key
from tmdb3 import get_locale, set_locale
from tmdb3 import Movie
from mongodb import mongoDriver

set_key('15ab57d70390c8dbcfd29edd3f047416')
set_locale('en', 'gb')

def getDataFilm(codiceFilm):
    """get data film riceve in input un codice di un film contenuto in TMDB e
    restituisce un array contenente in ordine:
    titolo, regista, produttori, cast, data di rilascio, trama, poster, trailer"""

    m = Movie(codiceFilm)

    title=m.title
    genres = ""

    for g in m.genres:

        genres+=g.name+", "
    genres=genres[:-2]+"."

    cast = ""

    for n in m.cast:
        cast = cast + n.name + " as " + n.character + ", "

    cast = cast[:-2] +"."

    trailer=""

    if(len(m.youtube_trailers)!=0):
        trailer = m.youtube_trailers[0].geturl()
        trailer = trailer.replace("watch?v=", "embed/")

    if (m.poster!=None):
        poster = "" + m.poster.geturl()
    else:
        poster="http://nicosoftware.altervista.org/img/noposter.png"

    overview = m.overview

    date = str(m.releasedate)

    producers = ""
    director = ""

    for c in m.crew:
        if (c.job == 'Director'):
            director += c.name + "\n"
        if (c.job == 'Producer'):
            producers += c.name + "\n"

    return [title,genres, director, producers, cast, date, overview, poster, trailer,getNamePosterSimilar(codiceFilm)]

def getNamePoster(codiceFilm):
    m = Movie(codiceFilm)
    title=m.title
    if (m.poster!=None):
        poster = "" + m.poster.geturl()
    else:
        poster="http://nicosoftware.altervista.org/img/noposter.png"


    return [title,poster]

def getNamePosterSimilar(codiceFilm):
    m = Movie(codiceFilm)
    simili = m.getSimilar()
    count=0;
    a = []
    l=[]
    n=8
    if(len(simili)<8):
        n=len(simili)
    if(n==0):
        return None
    for s in range(0,n):
        count+=1
        code = long(simili[s].id)
        print(code)

        title=simili[s].title
        if (simili[s].poster!=None):
            poster = "" + simili[s].poster.geturl()
        else:
            poster="http://nicosoftware.altervista.org/img/noposter.png"


        l.append([title,poster])
        if count==2:
            a.append(l)
            l=[]
            count=0
    if count>0 and count<2:
        a.append(l)
    return a







if __name__ == '__main__':
    codice = '135397'
    a = getDataFilm(codice)
    print(a)
    print(len(a[9]))
    for i in range(0,len(a[9])-1):
        for m in a[9][i]:
            print(m[0])

