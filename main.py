from tkinter import *
from tkinter import messagebox

from models import Database


class App:

    def __init__(self, master) -> None:
        self.master = master
        self.tasks = []
        self.screen()

    def update_count(self):
        return self.task_count.config(text=len(self.tasks))

    def update_list(self):
        self.list.delete(0, END)
        for i in self.tasks:
            self.list.insert(END, i)

    def add_task(self, text):
        if text == '':
            self.label.config(text="Please enter the field")
        else:
            self.tasks.append(text)
            self.update_count()
            Database.add_new_item(text)
            self.entry.delete(0, END)
            self.label.config(text="")
            self.update_list()
            # Database.print_all_items()

    def delete_task(self):
        task_id = self.entry.get()
        if self.list.curselection():
            task = self.list.get(ANCHOR)
            Database.remove_item(task_id)
            if task in self.tasks:
                self.tasks.remove(task)

            self.update_count()
            self.label.config(text="")
            return self.list.delete(ANCHOR)

        else:
            return self.label.config(text="Select a Task")

    def delete_all_tasks(self):
        delete_msg = messagebox.askyesno("ToDo App", "Are you sure to delete all tasks?")
        if delete_msg:
            self.tasks.clear()
            self.update_count()
            self.list.delete(0, END)
            self.label.config(text="")
            Database.delete_all_items()

    def exit(self):
        close_box = messagebox.askyesno("ToDo App", "Are you sure you want to exit?")
        if close_box:
            return self.master.destroy()

    def screen(self):
        ### labels
        self.label = Label(self.master, text="", bg="black", fg="white")
        self.task_count = Label(self.master, text=len(self.tasks), fg="white", bg="black")

        self.label.grid(row=0, column=1, columnspan=2, sticky=W + E)
        self.task_count.grid(row=0, column=3, padx=5)

        ### buttons
        self.add_b = Button(self.master, text="Add task", bg="red", fg="white", bd=0, width=17,
                            command=lambda: self.add_task(self.entry.get()))
        self.delete_b = Button(self.master, text="Delete Task", bg="#676767", fg="white", bd=0,
                               width=17, command=self.delete_task)

        self.delete_all_b = Button(self.master, text="Delete all tasks", bg="#676767", fg="white", bd=0,
                                   width=17, command=self.delete_all_tasks)

        self.exit_b = Button(self.master, text="Exit App", bg="#676767", fg="white", bd=0,
                             width=17, command=self.exit)

        self.add_b.grid(row=1, column=0)
        self.delete_b.grid(row=2, column=0)
        self.delete_all_b.grid(row=3, column=0)
        self.exit_b.grid(row=4, column=0)

        # Listbox
        self.entry = Entry(self.master, width=30, font=15, bd=0, bg="#404040", fg="white")
        self.list = Listbox(self.master, width=35, height=16, bg="#404040", fg="white", font=("Sans-Bold", 12))

        self.entry.grid(row=1, column=1, columnspan=2, padx=(0, 15), pady=(0, 10))
        self.list.grid(row=2, column=1, rowspan=7, columnspan=2, padx=(5, 25), pady=(0, 15))


def main():
    root = Tk()
    root.title("To Do App")
    # root.resizable()
    root.geometry("800x400")
    root.config(bg='black')

    App(root)
    # command = App(root)

    root.mainloop()


if __name__ == '__main__':
    main()
