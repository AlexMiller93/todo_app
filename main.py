import os.path

from tkinter import *
from tkinter import messagebox

from models import Database
from const import *


class App:

    def __init__(self, master) -> None:
        self.master = master
        self.tasks = []
        self.screen()

    def update_count(self):
        return self.task_count.config(text=f"Tasks: {len(self.tasks)}")

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
            self.task_count_db.config(text=f"Total in db: {Database.count_items()}")
            return text

    def delete_task(self):
        task_id = self.entry.get()
        if self.list.curselection():
            task = self.list.get(ANCHOR)
            self.tasks.remove(task)
            Database.remove_item(task_id)
            self.task_count_db.config(text=f"Total in db: {Database.count_items()}")
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
            self.label.config(text="All tasks removed")
            Database.delete_all_items()
            self.task_count_db.config(text=f"Total in db: {Database.count_items()}")

    def exit(self):
        close_box = messagebox.askyesno("ToDo App", "Are you sure you want to exit?")
        if close_box:
            return self.master.destroy()

    def clean_text(self):
        self.entry.delete(0, END)
        
    def save(self):
        if len(self.tasks) != 0:
            save_msg = messagebox.askyesno("To Do App", "Save your tasks in file?")
            if save_msg:
                Database.save_data_in_file()
                self.label.config(text="Tasks saved in file")
                
                if os.path.exists(FOLDER):
                    Database.save_data_in_file()
                    self.label.config(text="Tasks saved in file")
                else:
                    os.mkdir(FOLDER)
                    Database.save_data_in_file()
                    self.label.config(text="Tasks saved in file")
        else:
            return self.label.config(text="No tasks")
        
    def sort_tasks_desc(self):
        if len(self.tasks) != 0:
            self.tasks.sort(reverse=True)
            self.list.delete(0, END)
            for task in self.tasks:
                self.list.insert(END, task)
        else:
            return self.label.config(text="No tasks")

    def sort_tasks(self):
        if len(self.tasks) != 0:
            self.tasks.sort()
            self.list.delete(0, END)
            for task in self.tasks:
                self.list.insert(END, task)
        else:
            return self.label.config(text="No tasks")
    
    def screen(self):
        ### labels
        self.main_label = Label(self.master, text="TO DO App", font=('Courier', 30), fg="black", pady=10) 
        self.label = Label(self.master, text="Write your tasks", font=15, fg="black")
        self.task_count = Label(self.master, text=f"Tasks: {len(self.tasks)}",bg="white", fg="black", font=15)
        self.task_count_db = Label(self.master, text=f"Total in db: {Database.count_items()}",bg="white", fg="black", font=15)
        
        self.main_label.grid(row=0, column=1, columnspan=2)
        self.label.grid(row=1, column=1, columnspan=2, sticky=W + E, pady=5, padx=10)
        self.task_count.grid(row=0, column=3, padx=5)
        self.task_count_db.grid(row=1, column=3, padx=5)

        
        # Listbox
        self.entry = Entry(self.master, width=30, font=15, bd=0, bg="gainsboro", fg="black")
        self.list = Listbox(self.master, width=30, height=16, bg="white", fg="black", font=("Sans-Bold", 12))

        self.entry.grid(row=2, column=1, columnspan=2, padx=15, pady=10)
        self.list.grid(row=3, column=1, rowspan=6, columnspan=2, padx=(5, 25), pady=(0, 15))

        ### buttons
        self.add_b = Button(self.master, text="Add task", bg="indianred1", fg="white", bd=0, width=12, activebackground="chartreuse1", activeforeground="black", font=8,
                            command=lambda: self.add_task(self.entry.get()))
        self.sort_b = Button(self.master, text="Sort tasks ->", bg="darkolivegreen1", fg="black", bd=0, width=12, activebackground="chartreuse1", activeforeground="black", font=8,
                            command=self.sort_tasks)
        self.sort_desc_b = Button(self.master, text="Sort tasks <-", bg="green", fg="white", bd=0, width=12, activebackground="chartreuse1", activeforeground="black", font=8,
                            command=self.sort_tasks_desc)
        self.delete_b = Button(self.master, text="Delete task", bg="black", fg="white", bd=0, width=12, activebackground="chartreuse1", activeforeground="black", font=8,
                                command=self.delete_task)
        self.delete_all_b = Button(self.master, text="Delete all tasks", bg="red", fg="white", bd=0, width=12, activebackground="chartreuse1", activeforeground="black", font=8,
                                command=self.delete_all_tasks)
        self.clean_b = Button(self.master, text="Clean", bg="blue", fg="white", bd=0, width=12, activebackground="chartreuse1", activeforeground="black", font=8,
                                command=self.clean_text)
        self.save_b = Button(self.master, text="Save in file", bg="red", fg="white", bd=0, width=12, activebackground="chartreuse1", activeforeground="black", font=8,
                                command=self.save)
        self.exit_b = Button(self.master, text="Exit", bg="maroon", fg="white", bd=0, width=12, activebackground="chartreuse1", activeforeground="black", font=8,
                                command=self.exit)


        # buttons grid
        self.add_b.grid(row=2, column=0, padx=5)
        self.sort_b.grid(row=3, column=0, padx=5)
        self.sort_desc_b.grid(row=4, column=0, padx=5)
        self.clean_b.grid(row=5, column=0, padx=5)
        # self.save_db_b.grid(row=6, column=0, padx=5)
        
        self.save_b.grid(row=2, column=3)
        self.delete_b.grid(row=3, column=3)
        self.delete_all_b.grid(row=4, column=3)
        self.exit_b.grid(row=5, column=3)


def main():
    root = Tk()
    root.title("To Do App")
    root.geometry("600x500")
    root.config(bg='cadetblue1')
    root.resizable(False, False)
    icon = PhotoImage(file = "icon/check-list.png")
    root.iconphoto(False, icon)

    App(root)

    root.mainloop()


if __name__ == '__main__':
    main()
