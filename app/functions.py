from app.db_connect import get_db



##### Filter movies by title
def filter_movies_by_alphabet(range_start, range_end):
    db = get_db()
    cursor = db.cursor()
    query = 'SELECT * FROM movies WHERE title >= %s AND title <= %s'
    cursor.execute(query, (range_start, range_end))
    movies = cursor.fetchall()
    return movies

##### Filter movies by decade
def filter_movies_by_decade(decade):
    db = get_db()
    cursor = db.cursor()
    start_year = int(decade)
    end_year = start_year + 9
    query = 'SELECT * FROM movies WHERE release_year BETWEEN %s AND %s'
    cursor.execute(query, (start_year, end_year))
    movies = cursor.fetchall()
    return movies


##### Filter movies by genre
def filter_movies_by_genre(genre_id):
    db = get_db()
    cursor = db.cursor()
    query = '''
    SELECT movies.id, movies.title, movies.release_year, movie_genres.genre_id 
    FROM movies
    JOIN movie_genres ON movies.id = movie_genres.movie_id
    WHERE movie_genres.genre_id = %s
    '''
    cursor.execute(query, (genre_id,))
    movies = cursor.fetchall()
    return movies