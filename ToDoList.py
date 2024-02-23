from tkinter import *
from tkinter import messagebox

tasklist = []


def addtask():
    try:
        global tasklist
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        for i in tasks:
            if i != "\n":
                tasklist.append(i)
                listbox.insert(END, i)
    except:
        file = open("tasks.txt", "w")
        file.close()


def addnewtask():
    global tasklist
    task = new_task.get()
    if task != "":
        listbox.insert(END, task)
        tasklist.append(task)
        content.set("")
        print(task.replace('\n', ''), "added")
        with open('tasks.txt', 'a') as file:
            file.write((task))
            file.write('\n')
        file.close()

    else:
        messagebox.showwarning("Warning", "Please enter a task")


def removetask():
    global tasklist
    try:
        task = listbox.get(ANCHOR)
        tasklist.remove(task)
        listbox.delete(ANCHOR)
        print(task.replace('\n', ''), "removed. Remaining tasks -", len(tasklist))
        with open('tasks.txt', 'w') as file:
            for i in tasklist:
                file.write(i + '\n')
        file.close()
    except ValueError:
        messagebox.showwarning("Warning", "Please select a task to remove")


root = Tk()
root.geometry("330x470")
root.resizable(False, False)
root.config(bg="#223441")
root.title("To-Do List")

title_label = Label(root, text="TO-DO LIST", bg="#223441", fg="orange", font=('Courier new', 23))
title_label.pack(pady="10")

frame = Frame(root)
frame.pack(pady=10)
listbox = Listbox(frame, width="29", height="10", font=("Times new roman", 12), bd=0, fg="black",
                  highlightthickness=0, cursor="hand2", selectbackground="light gray", activestyle="none")
listbox.pack(side=LEFT, fill=BOTH, pady=4)

scroll = Scrollbar(frame)
scroll.pack(side=LEFT, fill=BOTH)

listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)

addtask()

info_label = Label(root, text="Enter a Task: ", font="times 10", bg="#223441", fg="White")
info_label.pack()
content = StringVar()
new_task = Entry(root, font="times 15", width="25", textvariable=content)
new_task.pack(pady=0)

button_frame = Frame(root, bg="#223441")
button_frame.pack(pady=10)
add = Button(button_frame, text="Add new task", bg="light blue", width="13", command=addnewtask)
add.pack(padx=10, pady=5, side=LEFT, fill=BOTH)
remove = Button(button_frame, text="Remove tasks", bg="#de5e60", width="13", command=removetask)
remove.pack(padx=10, pady=5, expand=True, side=RIGHT, fill=BOTH)

end_label = Label(root, text="Never wait till tomorrow", bg="#223441", fg="white", font=('Calibri new', 11))
end_label.pack()
root.mainloop()