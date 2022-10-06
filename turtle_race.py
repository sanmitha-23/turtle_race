from turtle import Turtle, Screen
import random

race_is_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
print(user_input)


colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'red']
y = [-100, -60, -20, 20, 60, 100]
turtle_list = []


for turtle_index in range(0, 6):    # doesn't include 6
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y[turtle_index])
    turtle_list.append(new_turtle)


if user_input:
    race_is_on = True


while race_is_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            race_is_on = False
            turtle_col = turtle.pencolor()
            if turtle.pencolor() == user_input:
                print(f"You've won! The {turtle_col} turtle is the winner.")
            else:
                print(f"You've lost! The {turtle_col} turtle is the winner.")

        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)


screen.exitonclick()
