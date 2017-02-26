from tmdb3 import set_key
from tmdb3 import get_locale, set_locale
from tmdb3 import Movie


def getDataFilm(codiceFilm):
    """get data film riceve in input un codice di un film contenuto in TMDB e
    restituisce un array contenente in ordine:
    titolo, regista, produttori, cast, data di rilascio, trama, poster, trailer"""
    set_key('15ab57d70390c8dbcfd29edd3f047416')
    set_locale('en', 'gb')
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

    trailer = m.youtube_trailers[0].geturl()
    trailer = trailer.replace("watch?v=", "embed/")

    poster = "" + m.poster.geturl()

    overview = m.overview

    date = str(m.releasedate)

    producers = ""
    director = ""

    for c in m.crew:
        if (c.job == 'Director'):
            director += c.name + "\n"
        if (c.job == 'Producer'):
            producers += c.name + "\n"

    return [title,genres, director, producers, cast, date, overview, poster, trailer]


if __name__ == '__main__':
    codice = '14564'
    a = getDataFilm(codice)
    print(a[6])
