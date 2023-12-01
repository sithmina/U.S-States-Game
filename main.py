import turtle 
import pandas


screen = turtle.Screen()
screen.title("U.S States Game.")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:

    guess = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                             prompt="What is another state?").title()
    print(guess)

#If guess is one of the states in all the states of the 50_states.csv.
    if guess == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")        
        break
    if guess in all_states:
        guessed_states.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(guess)
