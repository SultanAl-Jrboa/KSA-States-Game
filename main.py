import turtle
import pandas

screen = turtle.Screen()
screen.title("KSA States Game")
image = "Saudi_Arabia_location_map.svg.gif"
screen.addshape(image)
turtle.shape(image)

#This code is used to extract the coordinates from the image when the mouse clicks on the specified city

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()


data = pandas.read_csv("KSA_States.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 13:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/13 States Correct",
                                    prompt="What's another state's mame").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

