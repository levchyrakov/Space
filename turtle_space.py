import turtle
import math

screen = turtle.Screen()
screen.setup(900, 700)
screen.bgcolor("#120d2b")
screen.title("Черепашка рисует космос 🐢")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Рисуем звезду
def star(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("#ffffff")
    for _ in range(5):
        t.forward(size)
        t.right(144)

# Круг
def circle(x, y, r, color):
    t.penup()
    t.goto(x, y-r)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

# 🌙 Луна
circle(250, 220, 65, "#ffeaa7")
circle(275, 245, 65, "#120d2b")

# ⭐ Звёзды
stars = [
    (-350, 270, 12), (-250, 190, 8), (-100, 280, 10),
    (20, 210, 7), (120, 300, 11), (330, 170, 9),
    (-320, 50, 7), (-50, 120, 8), (180, 80, 6)
]

for x, y, s in stars:
    star(x, y, s)

# 🌌 Горизонт
t.penup()
t.goto(-450, -180)
t.pendown()
t.color("#302060")
t.begin_fill()

for x in range(-450, 451, 20):
    y = -100 + 35 * math.sin(x / 80)
    t.goto(x, y)

t.goto(450, -350)
t.goto(-450, -350)
t.end_fill()

# 🏔 Горы
t.color("#49327a")
t.begin_fill()
t.penup()
t.goto(-450, -180)
t.pendown()

points = [
    (-450, -180), (-330, -70), (-240, -160),
    (-120, -50), (-20, -150), (100, -60),
    (220, -150), (330, -40), (450, -140),
    (450, -350), (-450, -350)
]

for p in points:
    t.goto(p)

t.end_fill()

# 🌊 Вода
t.color("#211642")
t.begin_fill()
t.penup()
t.goto(-450, -180)
t.pendown()
t.goto(450, -140)
t.goto(450, -350)
t.goto(-450, -350)
t.goto(-450, -180)
t.end_fill()

# Отражение луны
for i in range(12):
    width = 100 - i * 6
    y = 100 - i * 13

    t.penup()
    t.goto(250 - width/2, y)
    t.pendown()
    t.color("#f9d976")
    t.pensize(3)

    t.forward(width)

# 🌿 Трава
t.pensize(2)
t.color("#49a078")

for x in range(-430, 451, 25):
    t.penup()
    t.goto(x, -170)
    t.pendown()
    t.goto(x + 8, -130 + (x % 30))
    
    t.penup()
    t.goto(x, -170)
    t.pendown()
    t.goto(x - 10, -140)

# 🌸 Цветы
def flower(x, y):
    circle(x, y, 7, "#ff6b9d")
    circle(x+8, y+4, 7, "#ff6b9d")
    circle(x+8, y-5, 7, "#ff6b9d")
    circle(x-8, y+4, 7, "#ff6b9d")
    circle(x-8, y-5, 7, "#ff6b9d")
    circle(x, y, 3, "#ffd166")

for x, y in [(-350,-125), (-100,-115), (120,-130),
             (300,-105), (380,-140), (-250,-150)]:
    flower(x, y)

# 🐢 Маленькая черепашка в центре
t.penup()
t.goto(-40, -250)
t.pendown()

# панцирь
t.color("#3ddc84")
t.begin_fill()
t.circle(35)
t.end_fill()

# голова
circle(0, -210, 15, "#70e000")

# лапки
for x, y in [(-35,-245), (35,-245), (-30,-275), (30,-275)]:
    circle(x, y, 10, "#70e000")

# узор панциря
t.color("#176b3a")
t.pensize(2)
for angle in range(0, 360, 60):
    t.penup()
    t.goto(-40, -250)
    t.setheading(angle)
    t.forward(35)
    t.pendown()
    t.goto(-40, -250)

# глаза
circle(-6, -205, 3, "black")
circle(6, -205, 3, "black")

# подпись
t.penup()
t.goto(0, -320)
t.color("#ffffff")
t.write(
    "🐢  TURTLE DREAMS  🐢",
    align="center",
    font=("Arial", 22, "bold")
)

turtle.done()