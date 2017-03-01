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
    try:
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

        return [title,genres, director, producers, cast, date, overview, poster, trailer,getNamePosterSimilar(codiceFilm,2,8)]
    except KeyError as err:
        print("chiave film non esistente:",err.args)
        return None



def getNamePoster(codiceFilm):
    try:
        m = Movie(codiceFilm)
        title=m.title
        if (m.poster!=None):
            poster = "" + m.poster.geturl()
        else:
            poster="http://nicosoftware.altervista.org/img/noposter.png"

        return [title,poster]


    except KeyError as err:
        print("chiave film non esistente:",err.args)
        return None

def getNamePosterSimilar(codiceFilm,elemPerPage,elemEstratti):
    try:

        m = Movie(codiceFilm)
        movie = m.getSimilar()
        count=0;
        count2=0;
        a = []
        l=[]
        data=[]
        n=8

        #verifica numero film simili
        if(len(movie)<8):
            n=len(movie)
        if(n==0):
            return None

        for movie in movie:

            code = mongoDriver.getIdMovielens(long(movie.id))
            if code!=0:
                count+=1
                count2+=1
                title=movie.title
                if (movie.poster!=None):
                    poster = "" + movie.poster.geturl()
                else:
                    poster="http://nicosoftware.altervista.org/img/noposter.png"

                data.append(title)
                data.append(poster)
                data.append(code)
                l.append(data)
                data=[]

            if count==elemPerPage:
                a.append(l)
                l=[]
                count=0
            if count2==elemEstratti:
                break

        return a
    except KeyError as err:
        print("chiave film non esistente:",err.args)
        return None


def getNameAndSimilar(codiceFilm,):
    try:
        m = Movie(codiceFilm)
        title=m.title
        similar= getNamePosterSimilar(codiceFilm,4,8)
        return [mongoDriver.getIdMovielens(codiceFilm),title,similar]
    except KeyError as err:
        return None





if __name__ == '__main__':
    a=getNameAndSimilar(14411)
    print(a)
