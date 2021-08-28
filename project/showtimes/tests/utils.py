from random import sample, randint, choice
from faker import Faker

from showtimes.models import Cinema, Screening

faker = Faker("pl_PL")


def random_cinema():
    """Return a random Person object from db."""
    cinema = Cinema.objects.all()
    return choice(cinema)


def fake_cinema_data():
    """Generate a dict of movie data

    The format is compatible with serializers (`Person` relations
    represented by names).
    """
    cinema_data = {
        "name": f"{faker.automotive()}",
        "city": faker.city(),
    }
    cinema = Cinema.objects.all()
    actors = sample(list(people), randint(1, len(people)))
    movie_data["actors"] = actor_names
    return movie_data


def find_cinema_by_name(name):
    """Return the first `Person` object that matches `name`."""
    return Cinema.objects.filter(name=name).first()


def create_fake_movie():
    """Generate new fake movie and save to database."""
    movie_data = fake_movie_data()
    movie_data["director"] = find_person_by_name(movie_data["director"])
    actors = movie_data["actors"]
    del movie_data["actors"]
    new_movie = Movie.objects.create(**movie_data)
    for actor in actors:
        new_movie.actors.add(find_person_by_name(actor))
