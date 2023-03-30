from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPE = ['Guitarist', 'Drummer', 'Singer']

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ConcertTrackerApp.VALID_MUSICIAN_TYPE:
            raise ValueError('Invalid musician type!')

        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f'{name} is already a musician!')

        if musician_type == 'Guitarist':
            new_musician = Guitarist(name, age)
        elif musician_type == 'Drummer':
            new_musician = Drummer(name, age)
        elif musician_type == 'Singer':
            new_musician = Singer(name, age)

        self.musicians.append(new_musician)
        return f'{name} is now a {musician_type}.'

    def create_band(self, name: str):
        for band in self.bands:
            if band.name == name:
                raise Exception(f'{name} band is already created!')
        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f'{place} is already registered for {concert.genre} concert!')

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f'{genre} concert in {place} was added.'

    def add_musician_to_band(self, musician_name: str, band_name: str):
        valid_musician = False
        valid_band = False

        curr_musician = None
        curr_band = None

        for musician in self.musicians:
            if musician.name == musician_name:
                valid_musician = True
                curr_musician = musician
                break
        if not valid_musician:
            raise Exception(f"{musician_name} isn't a musician!")

        for band in self.bands:
            if band.name == band_name:
                valid_band = True
                curr_band = band
                break
        if not valid_band:
            raise Exception(f"{band_name} isn't a band!")

        curr_band.members.append(curr_musician)
        return f'{curr_musician.name} was added to {curr_band.name}.'

    def remove_musician_from_band(self, musician_name: str, band_name: str):

        valid_member = False
        valid_band = False

        curr_member = None
        curr_band = None

        for band in self.bands:
            if band.name == band_name:
                valid_band = True
                curr_band = band
                break
        if not valid_band:
            raise Exception(f"{band_name} isn't a band!")

        for member in curr_band.members:
            if member.name == musician_name:
                valid_member = True
                curr_member = member
                break
        if not valid_member:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        curr_band.members.remove(curr_member)
        return f'{musician_name} was removed from {band_name}.'

   
    def start_concert(self, concert_place: str, band_name: str):
        band = [band for band in self.bands if band.name == band_name][0]
        concert = [concert for concert in self.concerts if concert.place == concert_place][0]
        for musician_type in ["Drummer", "Singer", "Guitarist"]:
            if not any(
                    filter(
                        lambda x: x.__class__.__name__ == musician_type,
                        band.members
                    )
            ):
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == 'Rock':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' and \
                        "play the drums with drumsticks" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' and "sing high pitch notes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play rock" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Metal':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' and "play the drums with drumsticks" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' and "sing low pitch notes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play metal" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Jazz':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' \
                        and "play the drums with drum brushes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' \
                        and ("sing low pitch notes" not in band_member.skills
                             or "sing high pitch notes" not in band_member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play jazz" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
