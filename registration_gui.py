from tkinter import*
from tkinter import ttk
from tkinter import messagebox

# Function To Save Data
def save_data():
    name= name_entry.get
    course = course_box.get()

    if name == "":
        messagebox.showwarning("Warning", "Enter Your Name")
    
    else:
        output_label.config(text="Name:" + name + "\nCourse:" + course)

# Function To Clear Data
def clear_data():
    name_entry.delete(0, END)
    course_box.set("Select Course")
    output_label.config(text="")


# Main Window
root = Tk()
root.title("Course Registration")
root.geometry("350x250")

# Menu Bar
menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Clear", command=clear_data)
file_menu.add_seperator()
file_menu.add_command(label="Exit",command=root.destroy)

menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# Title
title_label = Label(root, text="Course Registration", font=("Arial", 14))
title_label.grid(row=0, column=0, padx=10, pady=10)

# Name
name_label = Label(root, text="Name")
name_label.grid(row=1, column=0, padx=10, pady=10)

name_entry = Entry(root)
name_entry.grid(row=1, column=1)

# Course DropDown
course_label=Label(root, text="Course")
course_label.grid(row=2, column=0)

course_box = ttk.Combobox(root)
course_box["values"] = ("Scratch Basics", "Python", "Robotics", "3D Printing")
course_box.set("Select Course")
course_box.grid(row=2, column=1)

# Button
save_button = Button(root, text="Save", command=save_data)
save_button.grid(row=3, column=0, columnspan=2, pady=10)

# Output
output_label = Label(root, text="")
output_label.grid(row=4, column=0, columnspan=2)

root.mainloop()