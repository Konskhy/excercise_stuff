class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def __getitem__(self, item):
        return self.players[item]

    def __repr__(self):
        return print(f'{self.name} : {self.players}')

    def __str__(self):
        return print(f'{self.name} with {len(self.players)} players')
