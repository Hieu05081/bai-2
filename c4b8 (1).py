print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


from tkinter import *

# Tạo cửa sổ chính
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

# Tạo nhãn (label)
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

# Hàm xử lý sự kiện khi nhấn nút
def clicked():
    lbl.configure(text="Button was clicked !!")

# Tạo nút (button) và thêm vào cửa sổ
btn = Button(window, text="Click Me", command=clicked, bg="blue", fg="white")
btn.grid(column=1, row=0)

# Hiển thị cửa sổ
window.mainloop()
