import turtle
import math

screen = turtle.Screen()
screen.setup(800, 700)
screen.bgcolor("#111222")
screen.title("❤️ Сердце")

t = turtle.Turtle()
t.shape("turtle")
t.color("#ff1744")
t.pensize(5)
t.speed(10)

# Переходим в начало
t.penup()

first = True

# Параметрическое сердце
for i in range(500):
    angle = i * 2 * math.pi / 500

    x = 16 * math.sin(angle) ** 3
    y = (
        13 * math.cos(angle)
        - 5 * math.cos(2 * angle)
        - 2 * math.cos(3 * angle)
        - math.cos(4 * angle)
    )

    # Увеличиваем размер
    x *= 15
    y *= 15

    if first:
        t.goto(x, y)
        t.pendown()
        first = False
    else:
        t.goto(x, y)

    # Обновляем экран постепенно
    if i % 5 == 0:
        screen.update()

# Текст внутри
t.penup()
t.goto(0, -40)
t.color("white")
t.write(
    "LOVE",
    align="center",
    font=("Arial", 28, "bold")
)

turtle.done()