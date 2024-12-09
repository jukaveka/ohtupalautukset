from matchers import And, PlaysIn, HasAtLeast, HasFewerThan


class QueryBuilder:
    def __init__(self, query = And()):
        self.query = query

    def plays_in(self, team):
        return QueryBuilder(And(PlaysIn(team)))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr)))

    def build(self):
        return self.query