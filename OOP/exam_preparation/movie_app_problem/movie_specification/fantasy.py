from project.movie_specification.movie import Movie


class Fantasy(Movie):
    AGE_RESTRICT = 6

    def __init__(self, title: str, year: int, owner: object, age_restriction=AGE_RESTRICT):
        super().__init__(title, year, owner, age_restriction)

    def details(self):
        return f'Fantasy - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}'
