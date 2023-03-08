from project.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)
        self.guests += room.guests

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                if room.is_taken == False and people <= room.capacity:
                    room.take_room(people)
                    self.guests += people
                else:
                    return room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                if room.is_taken:
                    self.guests -= room.guests
                    room.free_room()
                else:
                    return room.free_room()

    def status(self):
        free_rooms = [str(x.number) for x in self.rooms if not x.is_taken]
        taken_rooms = [str(x.number) for x in self.rooms if x.is_taken]

        return f'Hotel {self.name} has {self.guests} total guests\nFree rooms: {", ".join(free_rooms)}\nTaken rooms: {", ".join(taken_rooms)}'
