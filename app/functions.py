from app.db_connect import get_db

def filter_movies(genre=None, title=None, release_year=None):
    db = get_db()
    cursor = db.cursor()
    query = 'SELECT * FROM movies WHERE 1=1'
    params = []

    if genre:
        query += ' AND genre = %s'
        params.append(genre)
    if title:
        query += ' AND title LIKE %s'
        params.append(f'%{title}%')
    if release_year:
        query += ' AND release_year = %s'
        params.append(release_year)

    cursor.execute(query, params)
    movies = cursor.fetchall()
    return movies

