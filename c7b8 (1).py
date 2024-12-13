print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


import tkinter
import random

# Danh sách các màu có thể có.
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0

# Thời gian chơi còn lại, ban đầu là 120 giây.
timeleft = 120

# Hàm bắt đầu trò chơi.
def startGame(event):
    if timeleft == 120:
        countdown()  # Bắt đầu đếm ngược.
        nextColour()  # Chọn màu tiếp theo.

# Hàm chọn và hiển thị màu tiếp theo.
def nextColour():
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()  # Kích hoạt ô nhập liệu.

        if e.get().lower() == colours[1].lower():
            score += 2  # Cộng 2 điểm cho mỗi lần đoán đúng.
        else:
            score -= 1  # Trừ 1 điểm cho mỗi lần đoán sai.

        e.delete(0, tkinter.END)  # Xóa ô nhập liệu.
        random.shuffle(colours)

        label.config(fg=str(colours[1]), text=str(colours[0]))  # Thay đổi màu và chữ.
        scoreLabel.config(text="Score: " + str(score))  # Cập nhật điểm số.

# Hàm đếm ngược.
def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1  # Giảm thời gian.
        timeLabel.config(text="Time left: " + str(timeleft))  # Cập nhật thời gian còn lại.
        timeLabel.after(1000, countdown)

# Tạo cửa sổ giao diện người dùng.
root = tkinter.Tk()

root.title("COLORGAME")
root.geometry("375x200")

# Thêm nhãn hướng dẫn.
instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!",
                             font=('Helvetica', 12))
instructions.pack()

# Thêm nhãn điểm số.
scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()

# Thêm nhãn thời gian còn lại.
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

# Thêm nhãn hiển thị màu.
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# Thêm ô nhập liệu màu.
e = tkinter.Entry(root)
root.bind('<Return>', startGame)  # Gọi hàm 'startGame' khi nhấn phím Enter.
e.pack()
e.focus_set()

# Bắt đầu giao diện người dùng.
root.mainloop()
