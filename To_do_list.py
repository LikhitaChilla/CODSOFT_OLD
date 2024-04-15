
from tkinter import *
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(END, task)
        entry_task.delete(0, END)
        

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        pass

root = Tk()
root.title("To-Do List")
root.config(bg="black")

frame_tasks = Frame(root)
frame_tasks.pack()

listbox_tasks = Listbox(frame_tasks, height=10, width=30,bg="#e699ff",highlightcolor="black",font=('oswald',20))
listbox_tasks.pack(side=LEFT)

scrollbar_tasks = Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=RIGHT, fill=Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = Entry(root,font=('Helvetica',26),width=20)
entry_task.pack()

button_add_task = Button(root, text="Add Task", width=60, command=add_task,bg="#33ffff")
button_add_task.pack()

button_delete_task = Button(root, text="Delete Task", width=60, command=delete_task,bg="#ffff4d")
button_delete_task.pack()

root.mainloop()