# import colorgram
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
#
# colours_rgb=[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_code=(r, g, b)
#     colours_rgb.append(color_code)
# print(colours_rgb)
import turtle as Turtle_module
import random




number_dots=100
colour_list=[(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
Turtle_module.colormode(255)

tim = Turtle_module.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)
tim.forward(270)
tim.setheading(360)
for dot_num in range(1,number_dots + 1):
    tim.dot(20,random.choice(colour_list))
    tim.forward(50)
    if dot_num%10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(360)



screen=Turtle_module.Screen()
screen.exitonclick()