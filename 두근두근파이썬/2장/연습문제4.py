import turtle

t = turtle.Turtle()
radius = 50

t.up()
t.goto(0,0)
t.down()
t.circle(radius)

t.up()
t.goto(100,0)
t.down()
t.circle(radius+20)

t.up()
t.goto(200,0)
t.down()
t.circle(radius+40)

#원의 반지름 50 (0,0) (100,0) (200,0)의 위치에 원그리기 단, 좌표가 움직일때마다 반지름 20증가, 반복문 사용x
