import turtle
import customtkinter
window = turtle.Screen()
window.bgcolor("black")



 # Write text on animation
text = turtle.Turtle()
text.hideturtle()
text.color("orange")
text.penup()
text.sety(175)
text.write("Happy Halloween", font=("Trattatello", 60, "bold"), align="center")

turtle.done()