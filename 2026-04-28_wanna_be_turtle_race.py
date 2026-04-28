import turtle
import random
import time

# --- Setup the Screen ---
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.title("The Great Turtle Derby")
screen.bgcolor("forestgreen")

# --- Draw the Finish Line ---
line_drawer = turtle.Turtle()
line_drawer.speed(0)
line_drawer.penup()
line_drawer.goto(230, 150)
line_drawer.pendown()
line_drawer.color("white")
line_drawer.pensize(5)
line_drawer.goto(230, -150)
line_drawer.hideturtle()

# --- Initialize the Racers ---
colors = ["red", "orange", "blue", "purple", "yellow"]
y_positions = [100, 50, 0, -50, -100]
all_turtles = []

for i in range(5):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    # Move to the starting line on the left
    new_turtle.goto(x=-250, y=y_positions[i])
    all_turtles.append(new_turtle)

# --- The Race Logic ---
is_race_on = True

while is_race_on:
    for racer in all_turtles:
        # Check if a turtle has crossed the finish line (x > 230)
        if racer.xcor() > 230:
            is_race_on = False
            winning_color = racer.pencolor()
            
            # Announce the winner
            announcer = turtle.Turtle()
            announcer.hideturtle()
            announcer.penup()
            announcer.goto(0, 0)
            announcer.write(f"The {winning_color} turtle wins!", 
                            align="center", font=("Arial", 24, "bold"))
            break

        # Move each turtle by a random amount
        distance = random.randint(1, 10)
        racer.forward(distance)

# Keep the window open until clicked
screen.exitonclick()