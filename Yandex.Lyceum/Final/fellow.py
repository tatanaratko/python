class Fellow:
    def __init__(self, name, knowledge, is_varmint):
        self.name = name
        self.knowledge = knowledge
        self.rest_knowledge = 0
        self.is_varmint = is_varmint

    def __str__(self):
        return f'Fellow {self.name} - {self.knowledge}'

    def __eq__(self, other):
        return self.knowledge == other.knowledge and \
            self.is_varmint == other.is_varmint and self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.weight() < other.weight()

    def __gt__(self, other):
        return self.weight() > other.weight()

    def __le__(self, other):
        return self.weight() <= other.weight()

    def __ge__(self, other):
        return self.weight() >= other.weight()

    def study(self, amount):
        self.knowledge += (amount + self.rest_knowledge) // 10
        self.rest_knowledge = (amount + self.rest_knowledge) % 10

    def prankster(self):
        self.is_varmint = not self.is_varmint

    def speak(self):
        if self.is_varmint:
            return 'Silly donkey'
        return 'Good boy'

    def weight(self):
        return (self.knowledge, not self.is_varmint, len(self.name), self.name)