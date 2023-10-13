import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=730, height=500)
turtle.shape(image)

guessed_states = []

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states guessed",
                                    prompt="What's another state name?").title()

    if answer_state == "Exit":
        states_to_learn = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_t = data[data.state == answer_state]
        t.goto(int(state_t.x), int(state_t.y))
        t.write(state_t.state.item())
        guessed_states.append(answer_state)
