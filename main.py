import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50 States correct", prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in data.state.to_list():
            if state not in guessed_states:
                missing_states.append(state)
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break
    if answer_state in data.state.to_list():
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x-10), int(state_data.y))
        t.write(answer_state)

