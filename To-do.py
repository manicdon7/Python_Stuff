from tkinter import *
from customtkinter import *

class TodoList:
    def __init__(self, master):
        self.tasks = []
        self.master = master
        master.title("To-Do List")
        master.geometry("400x300")

        self.task_entry = Entry(master)
        self.task_entry.pack()

        self.add_button = Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_list = Listbox(master)
        self.task_list.pack()

        self.mark_button = Button(master, text="Mark Completed", command=self.mark_completed)
        self.mark_button.pack()

        self.delete_button = Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(END, task)
            self.task_entry.delete(0, END)

    def mark_completed(self):
        selected = self.task_list.curselection()
        if selected:
            index = selected[0]
            completed_task = self.task_list.get(index)
            self.task_list.delete(index)
            self.tasks.remove(completed_task)

    def delete_task(self):
        selected = self.task_list.curselection()
        if selected:
            index = selected[0]
            deleted_task = self.task_list.get(index)
            self.task_list.delete(index)
            self.tasks.remove(deleted_task)

if __name__ == "__main__":
    set_appearance_mode("System")
    set_default_color_theme("blue")
    root = Tk()
    todo_list = TodoList(root)
    root.mainloop()
