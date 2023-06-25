import pandas
import turtle
from score import score
screen = turtle.Screen()
keyboard = turtle.Screen()
screen.bgpic("blank_states_img.gif")
screen.title("US States Game")
states = pandas.read_csv("50_states.csv")
timmy_turtle = turtle.Turtle()
timmy_turtle.penup()
timmy_turtle.hideturtle()

game_is_on = True
while game_is_on:
    input_state = screen.textinput(f"Score = {score}", "enter the state name")
    states_list = states["state"].to_list()
    for i in range(len(states_list)):
        if input_state == states_list[i]:
            input_state_row = states[states.state == input_state]
            state_x = input_state_row.x.iloc[0]
            state_y = input_state_row.y.iloc[0]
            timmy_turtle.setposition(state_x, state_y)
            timmy_turtle.write(input_state)
            score += 1
            game_is_on = True
            break
        else:
            game_is_on = False

screen.exitonclick()