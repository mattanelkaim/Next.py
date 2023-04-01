import tkinter as tk


def display_image():
    image_file = tk.PhotoImage(file="image.png")
    image_label = tk.Label(top, image=image_file)
    image_label.pack()
    top.mainloop()


top = tk.Tk()
label = tk.Label(top, text="what's my favorite video?", fg='blue', font=("Arial", 20))
button = tk.Button(top, text="click to find out!", font=("Arial", 15), command=display_image)

label.pack()
button.pack()

top.mainloop()
