from turtle import *

color('chocolate', 'yellow1')
begin_fill()
circle(80)
end_fill()

penup()
goto(-30, 90)
dot(30, 'white')
dot(15, 'black')

goto(30, 90)
dot(30, 'white')
dot(15, 'black')

goto(-40, 70)
pendown()

width(2)
color('red')
right(90)
circle(40, 180)
penup()

goto(56, 83)
dot(20, 'VioletRed1')

goto(-56, 83)
dot(20, 'VioletRed1')

goto(0, 78)

exitonclick()

