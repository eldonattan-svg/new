"""
Reading Schedule Planner
------------------------
Python + Tkinter assignment covering:
  1. A main window
  2. A separate Toplevel window for entering the book details
  3. Floor division (//) and modulo (%) to calculate complete reading
     days and remaining pages
  4. try/except to handle invalid input
"""

import tkinter as tk
from tkinter import ttk, messagebox


class ReadingPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Reading Schedule Planner")
        self.root.geometry("380x200")
        self.planner_window = None  # keeps track of the Toplevel window

        ttk.Label(root, text="Reading Schedule Planner",
                  font=("Helvetica", 16, "bold")).pack(pady=(25, 5))
        ttk.Label(root, text="Plan how many days a book will take to read."
                  ).pack(pady=5)

        ttk.Button(root, text="Open Planner",
                   command=self.open_planner).pack(pady=10)
        ttk.Button(root, text="Exit", command=root.destroy).pack()

    # ---------------------------------------------- Toplevel window
    def open_planner(self):
        # Don't open a second planner if one is already showing
        if self.planner_window is not None and self.planner_window.winfo_exists():
            self.planner_window.lift()
            return

        win = tk.Toplevel(self.root)
        win.title("Enter Book Details")
        win.geometry("360x320")
        self.planner_window = win

        ttk.Label(win, text="Total pages in the book:").pack(pady=(20, 2))
        self.pages_entry = ttk.Entry(win, justify="center")
        self.pages_entry.pack()

        ttk.Label(win, text="Pages you plan to read each day:").pack(pady=(15, 2))
        self.daily_entry = ttk.Entry(win, justify="center")
        self.daily_entry.pack()

        ttk.Button(win, text="Calculate", command=self.calculate).pack(pady=15)

        self.result_label = ttk.Label(win, text="", justify="center",
                                      font=("Helvetica", 11))
        self.result_label.pack(pady=5)

        ttk.Button(win, text="Close", command=win.destroy).pack(pady=10)
        self.pages_entry.focus_set()

    # ---------------------------------------------- calculation
    def calculate(self):
        try:
            total_pages = int(self.pages_entry.get())
            pages_per_day = int(self.daily_entry.get())

            if total_pages <= 0 or pages_per_day <= 0:
                raise ValueError("Numbers must be greater than zero.")

            complete_days = total_pages // pages_per_day   # floor division
            remaining_pages = total_pages % pages_per_day  # modulo

            text = (f"Complete reading days: {complete_days}\n"
                    f"Remaining pages: {remaining_pages}")
            if remaining_pages > 0:
                text += (f"\n(Plus 1 extra day to finish the last "
                         f"{remaining_pages} pages.)")
            self.result_label.config(text=text)

        except ValueError:
            messagebox.showerror(
                "Invalid input",
                "Please enter whole numbers greater than zero for both fields.",
                parent=self.planner_window)
            self.result_label.config(text="")
        except ZeroDivisionError:
            messagebox.showerror(
                "Invalid input",
                "Pages per day cannot be zero.",
                parent=self.planner_window)


if __name__ == "__main__":
    root = tk.Tk()
    ReadingPlanner(root)
    root.mainloop()