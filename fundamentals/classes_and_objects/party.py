class Person:
    def __init__(self, name):
        self.name = name


class Party:

    def __init__(self):
        self.people = []

    def invite_people(self, person):
        self.people.append(person)

    def people_going(self):
        return ', '.join([person.name for person in self.people])

    def number_of_guests(self):
        return len(self.people)


party = Party()

while True:
    command = input()

    if command == 'End':
        break

    name = command

    person = Person(name)
    party.invite_people(person)

print(f'Going: {party.people_going()}')
print(f'Total: {party.number_of_guests()}')
