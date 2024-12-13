print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


from tkinter import *

# Tạo cửa sổ chính
root = Tk()
root.title("Thông tin cá nhân và lựa chọn số")
root.geometry('400x300')

# Tạo các nhãn và ô nhập liệu cho thông tin cá nhân
Label(root, text="Họ tên:").grid(row=0, column=0, padx=10, pady=5)
entry_name = Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Ngày tháng năm sinh:").grid(row=1, column=0, padx=10, pady=5)
entry_dob = Entry(root)
entry_dob.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="MSSV:").grid(row=2, column=0, padx=10, pady=5)
entry_mssv = Entry(root)
entry_mssv.grid(row=2, column=1, padx=10, pady=5)

Label(root, text="Ngành học:").grid(row=3, column=0, padx=10, pady=5)
entry_major = Entry(root)
entry_major.grid(row=3, column=1, padx=10, pady=5)

# Tạo không gian để phân cách
Label(root, text="").grid(row=4, column=0, pady=5)

# Tạo phần lựa chọn số
Label(root, text="Chọn một số:").grid(row=5, column=0, padx=10, pady=5)
v = IntVar()
v.set(1)  # Khởi tạo lựa chọn ban đầu là 1
Radiobutton(root, text="1", variable=v, value=1).grid(row=5, column=1, sticky=W)
Radiobutton(root, text="2", variable=v, value=2).grid(row=6, column=1, sticky=W)
Radiobutton(root, text="3", variable=v, value=3).grid(row=7, column=1, sticky=W)

# Tạo nút "Click Me"
def show_choice():
    selection = "Bạn đã chọn số " + str(v.get())
    label_result.config(text=selection)

btn = Button(root, text="Click Me", command=show_choice)
btn.grid(row=8, column=1, pady=10)

# Tạo nhãn để hiển thị kết quả lựa chọn
label_result = Label(root)
label_result.grid(row=9, column=1, pady=10)

# Hiển thị cửa sổ
root.mainloop()
