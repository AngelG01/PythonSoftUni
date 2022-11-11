import random
from replit import clear
import art
import data


def pick_a_person():
    number = random.randint(0, len(data.data)) - 1
    person = data.data[number]
    return person


def correct_answer(first_person, second_person):
    if first_person['follower_count'] > second_person['follower_count']:
        return 'A'
    else:
        return 'B'


points = 0
person_a = pick_a_person()
while True:
    person_b = pick_a_person()

    print(art.logo)
    if points > 0:
        print(f"You are right! Current score: {points}")

    print(
        f'Compare A: {person_a["name"]}, a {person_a["description"]}, from {person_a["country"]}')
    print(art.vs)
    print(f'Against B: {person_b["name"]}, a {person_b["description"]}, from {person_b["country"]}')
    person_answer = input('Who has more follower? "A" or "B": ')

    if person_answer != correct_answer(person_a, person_b):
        clear()
        print(f"Sorry that's wrong. Final score: {points}")
        break
    clear()
    points += 1
    person_a = person_b
