import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Animated To-Do List")
        self.root.geometry("420x560")
        self.root.resizable(False, False)
        self.root.configure(bg="#0f172a")

        self.tasks = []

        self.title = tk.Label(
            root,
            text="To-Do List",
            font=("Arial", 26, "bold"),
            bg="#0f172a",
            fg="white"
        )
        self.title.pack(pady=25)

        self.entry_frame = tk.Frame(root, bg="#0f172a")
        self.entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(
            self.entry_frame,
            width=26,
            font=("Arial", 14),
            bg="#1e293b",
            fg="white",
            insertbackground="white",
            relief="flat"
        )
        self.task_entry.grid(row=0, column=0, ipady=10, padx=5)

        self.add_button = tk.Button(
            self.entry_frame,
            text="+",
            font=("Arial", 18, "bold"),
            bg="#38bdf8",
            fg="black",
            width=3,
            relief="flat",
            command=self.add_task
        )
        self.add_button.grid(row=0, column=1, padx=5)

        self.task_container = tk.Frame(root, bg="#0f172a")
        self.task_container.pack(pady=20, fill="both", expand=True)

        self.footer = tk.Label(
            root,
            text="Click task to mark as done",
            font=("Arial", 10),
            bg="#0f172a",
            fg="#94a3b8"
        )
        self.footer.pack(pady=10)

        self.task_entry.bind("<Return>", lambda event: self.add_task())

    def add_task(self):
        task_text = self.task_entry.get().strip()

        if task_text == "":
            messagebox.showwarning("Empty Task", "Please enter a task.")
            return

        task_frame = tk.Frame(
            self.task_container,
            bg="#1e293b",
            height=50
        )
        task_frame.pack(fill="x", padx=30, pady=6)

        task_label = tk.Label(
            task_frame,
            text=task_text,
            font=("Arial", 13),
            bg="#1e293b",
            fg="white",
            anchor="w"
        )
        task_label.pack(side="left", fill="x", expand=True, padx=15)

        delete_button = tk.Button(
            task_frame,
            text="✕",
            font=("Arial", 12, "bold"),
            bg="#ef4444",
            fg="white",
            relief="flat",
            command=lambda: self.delete_task(task_frame)
        )
        delete_button.pack(side="right", padx=10)

        task_label.bind("<Button-1>", lambda event: self.mark_done(task_label))

        self.tasks.append(task_frame)
        self.task_entry.delete(0, tk.END)

        self.animate_task(task_frame)

    def animate_task(self, widget, step=0):
        colors = [
            "#334155",
            "#2f3f55",
            "#2a394d",
            "#263447",
            "#223042",
            "#1e293b"
        ]

        if step < len(colors):
            widget.configure(bg=colors[step])
            for child in widget.winfo_children():
                if isinstance(child, tk.Label):
                    child.configure(bg=colors[step])
            self.root.after(60, lambda: self.animate_task(widget, step + 1))

    def mark_done(self, label):
        current_text = label.cget("text")

        if current_text.startswith("✓ "):
            label.config(
                text=current_text[2:],
                fg="white",
                font=("Arial", 13)
            )
        else:
            label.config(
                text="✓ " + current_text,
                fg="#22c55e",
                font=("Arial", 13, "overstrike")
            )

    def delete_task(self, task_frame):
        self.animate_delete(task_frame)

    def animate_delete(self, widget, step=0):
        colors = [
            "#7f1d1d",
            "#991b1b",
            "#b91c1c",
            "#dc2626",
            "#ef4444"
        ]

        if step < len(colors):
            widget.configure(bg=colors[step])
            for child in widget.winfo_children():
                child.configure(bg=colors[step])
            self.root.after(50, lambda: self.animate_delete(widget, step + 1))
        else:
            widget.destroy()


root = tk.Tk()
app = TodoApp(root)
root.mainloop()