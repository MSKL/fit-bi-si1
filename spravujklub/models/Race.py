class Race:
    id = 1

    def __init__(self, name, type, place, date, deadline, user_registered):
        self.id = Race.id
        self.name = name
        self.type = type
        self.place = place
        self.date = date
        self.start = "12:00:00"
        self.deadline = deadline
        self.user_registered = user_registered
        self.organizer = "Franta"
        self.end_registration = "5 minut před startem"
        self.discipline = "beh"
        self.url = "www.zavod-blabla.cz"
        self.info = "Lorem ipsum bla bla bla"
        Race.id += 1
