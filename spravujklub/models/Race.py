class Race:
    id = 1

    def __init__(self, name, place, date, user_registered):
        self.id = Race.id
        self.name = name
        self.place = place
        self.date = date
        self.user_registered = user_registered
        Race.id += 1
