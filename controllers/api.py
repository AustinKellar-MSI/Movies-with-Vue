def insert_movie():
    # in this funciton, we take the data that the JavaScript sent us and insert it into the database!
    new_movie_id = db.movies.insert(
        title=request.vars.title,
        description=request.vars.description,
        rating=request.vars.rating
    )
    return response.json(dict(id=new_movie_id))

def get_all_movies():
    movies = db(db.movies).select() # this asks the database for all entries in the movies table
    return response.json(dict(movies=movies)) # return all movies as a JSON object back to JavaScript

def delete_movie():
    db(db.movies.id == request.vars.id).delete()
    return "movie deleted!"