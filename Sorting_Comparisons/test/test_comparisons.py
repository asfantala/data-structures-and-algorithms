import pytest

from ..comparisons import sort_by_name, sort_by_year


@pytest.fixture
def movies():
    return  [
    {
        "title": "Inception",
        "year": 2010,
        "genres": ["Action"]
    },
    {
        "title": "The Matrix",
        "year": 1999,
        "genres": ["Action"]
    },
    {
        "title": "Fight Club",
        "year": 1999,
        "genres": ["Drama"]
    },
    {
        "title": "Interstellar",
        "year": 2014,
        "genres": ["Adventure", "Drama", "Sci-Fi"]
    },
    {
        "title": "The Shawshank Redemption",
        "year": 1994,
        "genres": ["Drama"]
    },
]


def test_sort_by_name(movies):
    sorted_movies = sort_by_name(movies)
    assert sorted_movies[0]["title"] == "Fight Club"
    assert sorted_movies[1]["title"] == "Inception"
    assert sorted_movies[2]["title"] == "Interstellar"
    assert sorted_movies[3]["title"] == "The Matrix"
    assert sorted_movies[4]["title"] == "The Shawshank Redemption"


def test_sort_by_year(movies):
    sorted_movies = sort_by_year(movies)
    assert sorted_movies[0]["year"] == 1994
    assert sorted_movies[1]["year"] == 1999
    assert sorted_movies[2]["year"] == 1999
    assert sorted_movies[3]["year"] == 2010
    assert sorted_movies[4]["year"] == 2014