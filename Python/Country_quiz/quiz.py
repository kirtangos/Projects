# import turtle
# import pandas as pd 

# screen=turtle.Screen()
# screen.title("U.S game")
# image="C:\Python tutorial\Projects\Country_quiz\states_img.gif"
# turtle.addshape(image)
# turtle.shape(image)

# df=pd.read_csv("C:\Python tutorial\Projects\Country_quiz\states.csv ")
# guessed_states = []
# all_states=df.state.to_list()
# while len(guessed_states)<50:
#     answer_state=screen.textinput(title="Guess the state",prompt="What is the other state name")
#     if answer_state=="Exit":
#         missing_states=[]
#         for state in all_states:
#             if state not in guessed_states:
#                 missing_states.append(state)
#             new_data=pd.DataFrame(missing_states)
#             new_data.to_csv("states_to_leanr.csv")
#         break 
#     if answer_state in all_states:
#         guessed_states.append(answer_state)
#         t=turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data=df[df.state==answer_state]
#         t.goto(state_data.x.item(),state_data.y.item())
#         t.write(state_data.state.item())

# screen.exitonclick()



import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
