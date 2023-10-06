import tkinter as tk
import csv
import datetime
import os

class AskWhatYouAreDoing:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Worklog")

        self.label = tk.Label(self.root, text="Share what are you doing?")
        self.label.pack(padx=10, pady=10)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(padx=10, pady=10)

        self.entry.focus_set()

        # Bind the Ctrl+A keyboard shortcut to the select_all() function
        self.entry.bind("<Control-Key-a>", self.select_all)

        self.entry.bind("<Return>", self.save_input)

        self.center_window_at_top()

        self.root.mainloop()

    def select_all(self, event):
        """Selects all text in the text input."""
        self.entry.select_range(0, "end")

    def save_input(self, event):
        user_input = self.entry.get()
        current_time = datetime.datetime.now()

        # Get the date, month in word, and year
        date = current_time.day
        month = datetime.datetime.strftime(current_time, "%b")
        year = current_time.year

        # Get the hour, minutes, and seconds
        hour = current_time.hour
        minutes = current_time.minute
        seconds = current_time.second

        # Format the date and time
        date_string = f"{date}/{month}/{year}"
        time_string = f"{hour}:{minutes}:{seconds}"

        # Save the data to the CSV file
        worklog_dir = os.path.join(os.path.expanduser("~"), ".worklog")
        if not os.path.exists(worklog_dir):
            os.makedirs(worklog_dir)

        with open(os.path.join(worklog_dir, "worklog.csv"), "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([date_string, time_string, user_input])

        self.root.destroy()

    def center_window_at_top(self):
        # Update the window so that the height is calculated correctly
        self.root.update()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()

        # Calculate the x and y coordinates for the center of the window
        x_coordinate = int((screen_width - window_width) / 2)
        y_coordinate = int(window_height)

        # Update the window's position
        self.root.geometry(f"+{x_coordinate}+{y_coordinate}")

if __name__ == "__main__":
    AskWhatYouAreDoing()
