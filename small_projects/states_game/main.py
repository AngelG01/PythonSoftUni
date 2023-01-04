import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data['state'].tolist()
guessed_states = []
coordinates = data.to_dict()

correct_count = 0


while correct_count < 51:
    answer_state = turtle.textinput(f'{correct_count}/50 correct guesses', "What's another state's name").title()

    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]

#         for state in all_states:
#             if state not in guessed_states:
#                 missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if answer_state in all_states:
        state_coordinates = data[data.state == answer_state]
        timmy = turtle.Turtle()
        timmy.hideturtle()
        timmy.penup()
        timmy.goto(int(state_coordinates.x), int(state_coordinates.y))
        timmy.write(answer_state, align='center', font=('Arial', 8, 'normal'))
        correct_count += 1
        guessed_states.append(answer_state)


turtle.mainloop()
