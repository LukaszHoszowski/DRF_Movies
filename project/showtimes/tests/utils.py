from random import sample, randint, choice, choices
from faker import Faker

from movielist.models import Person, Movie
from showtimes.models import Cinema

faker = Faker("pl_PL")


def random_person():
    """Return a random Person object from db."""
    people = Person.objects.all()
    return choice(people)


def random_cinema():
    """Return a random Cinema object from db."""
    cinema = Cinema.objects.all()
    return choice(cinema)


def random_movies():
    """Return a random Movie object from db."""
    movie = Movie.objects.all()
    return choices(movie, k=3)


def fake_person_data():
    person_data = {
        'name': f'{faker.name}',
    }
    return person_data


def fake_cinema_data():
    cinema_data = {
        'name': f'kino {faker.company}',
        'city': f'{faker.city}',
        'movies': f'{random_movies().title}',
    }


def fake_movie_data():
    """Generate a dict of movie data

    The format is compatible with serializers (`Person` relations
    represented by names).
    """
    movie_data = {
        "title": f"{faker.job()} {faker.first_name()}",
        "description": faker.sentence(),
        "year": int(faker.year()),
        "director": random_person().name,
    }
    people = Person.objects.all()
    actors = sample(list(people), randint(1, len(people)))
    actor_names = [a.name for a in actors]
    movie_data["actors"] = actor_names
    return movie_data

print(fake_movie_data())


def find_person_by_name(name):
    """Return the first `Person` object that matches `name`."""
    return Person.objects.filter(name=name).first()


def find_cinema_by_name(name):
    """Return the first `Cinema` object that matches `name`."""
    return Cinema.objects.filter(name=name).first()


def find_movie_by_title(title):
    """Return the first `title` object that matches `title`."""
    return Movie.objects.filter(title=title).first()


def create_fake_movie():
    """Generate new fake movie and save to database."""
    movie_data = fake_movie_data()
    movie_data["director"] = find_person_by_name(movie_data["director"])
    actors = movie_data["actors"]
    del movie_data["actors"]
    new_movie = Movie.objects.create(**movie_data)
    for actor in actors:
        new_movie.actors.add(find_person_by_name(actor))


def create_fake_person():
    person_data = fake_person_data()
    Person.objects.create(**person_data)

