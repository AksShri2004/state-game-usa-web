import turtle

scr = turtle.Screen()
scr.title("US States quiz")
scr.setup(725,491)
image = "blank_states_img.gif"

turtle.addshape(image)
turtle.shape(image)

import pandas

data = pandas.read_csv("50_states.csv")


state = turtle.Turtle()
state.hideturtle()
state.penup()

states = []
# all_states = data.state.list()

while not len(states) == 50:
    user_state = scr.textinput(title="Guess 50 States", prompt="Type another state: ").title()
    # user_state.title()
    if user_state == "Exit":
        # for n in range
        miss_states = []
        for n in data.state:
            if n not in states:
                miss_states.append(n)
        print(miss_states)
        break

    for n in data.state:
        if user_state == n:
            current_state = data[data.state == user_state]
            x_cor = int(current_state.x)
            y_cor = int(current_state.y)
            state.goto(x_cor, y_cor)
            state.write(str(user_state), False, "center", "Arial")
            states.append(n)
            score = len(states)
        else:
            pass

with open("records.txt", mode = "w") as final:
    final.write(f"new record: {states}")
# print(miss_states)
turtle.mainloop()
