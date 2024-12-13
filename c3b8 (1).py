print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


import turtle
import random

# Thiết lập màn hình
screen = turtle.Screen()
screen.bgcolor("white")

# Tạo đối tượng turtle
pen = turtle.Turtle()
pen.speed(0)  # Đặt tốc độ vẽ tối đa

# Hàm vẽ hình tròn tại vị trí xác định
def draw_circle(x, y, radius, color):
    pen.penup()
    pen.goto(x, y - radius)  # Đặt vị trí tại đỉnh của hình tròn
    pen.pendown()
    pen.pencolor(color)
    pen.circle(radius)

# Hàm vẽ hình vuông tại vị trí xác định
def draw_square(x, y, side, color):
    pen.penup()
    pen.goto(x, y)  # Đặt vị trí tại góc trái trên của hình vuông
    pen.pendown()
    pen.pencolor(color)
    for _ in range(4):
        pen.forward(side)
        pen.right(90)

# Định nghĩa các màu sắc và tham số
colors = ["red", "blue", "green", "purple", "orange", "cyan"]
num_shapes = 12
radius = 50
side = 100

# Vẽ các hình tròn và hình vuông xen kẽ
for i in range(num_shapes):
    angle = 360 / num_shapes * i
    x = radius * 2 * turtle.cos(turtle.radians(angle))
    y = radius * 2 * turtle.sin(turtle.radians(angle))
    draw_circle(x, y, radius, random.choice(colors))
    draw_square(x - side / 2, y - side / 2, side, random.choice(colors))

# Ẩn con rùa và hiển thị kết quả
pen.hideturtle()
screen.mainloop()
