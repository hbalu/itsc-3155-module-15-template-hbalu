from flask.testing import FlaskClient
from src.models import db, Movie
from app import app

def test__get_all_movies(test_app: FlaskClient):


    test_movie = Movie(title='The Dark Knight', director = 'Christopher Nolan', rating = 5)
    db.session.add(test_movie)
    db.session.commit()

    res = test_app.get('/movies')
    page_data: str = res.data

    assert res.status_code== 200 
    assert f'<td><a href="/movies/(test_movie.movie_id)">The Dark Knight</a></td>' in page_data
    assert '<td>Christopher Nolan</td>' in page_data
    assert '<td>5</td>' in page_data
