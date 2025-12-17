# import colorgram
# colors = colorgram.extract('hirst_painting.jpg', 50)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colour = (r, g, b)
#     rgb_colors.append(new_colour)
# print(rgb_colors)
import turtle as t
t.colormode(255)

colour_list =[(237, 224, 80), (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218),
              (204, 75, 12), (219, 161, 103), (234, 224, 4), (11, 23, 63), (29, 189, 111),
              (22, 107, 174), (16, 28, 177), (216, 134, 179), (8, 186, 216), (229, 167, 200),
              (210, 25, 148), (122, 190, 160), (7, 49, 26), (34, 136, 72), (63, 20, 7),
              (126, 219, 234), (190, 14, 4), (109, 87, 215), (140, 217, 202), (238, 64, 34),
              (71, 10, 28), (10, 98, 50), (166, 181, 232), (237, 170, 159), (253, 5, 42),
              (9, 87, 103), (21, 35, 249), (63, 100, 8), (253, 9, 5), (0, 246, 244), (0, 250, 254)]

tim = t.Turtle()
tim.speed("fastest")
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(350)
tim.setheading(0)

def hirst_(number_of_dots):
    colour_index = 0
    for dot_count in range(1,number_of_dots+1):
        colour_index = (dot_count + 1) % len(colour_list)
        tim.pendown()
        tim.dot(20,colour_list[colour_index])
        tim.penup()
        tim.forward(50)
        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)

hirst_(100)



screen = t.Screen()
screen.exitonclick()