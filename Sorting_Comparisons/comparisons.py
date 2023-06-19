def sort_movies_by_year(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie['year'], reverse=True)
    return sorted_movies

def sort_movies_by_title(movies):
    def remove_leading_articles(title):
        articles = ['The ', 'An ', 'A ']
        for article in articles:
            if title.startswith(article):
                return title[len(article):]
        return title

    sorted_movies = sorted(movies, key=lambda movie: remove_leading_articles(movie['title'].lower()))
    return sorted_movies


