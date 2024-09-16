import csv
import random
import tkinter as tk
from tkinter import filedialog, messagebox
import tkinter.font as tkfont


def browse_file():
  """Function that opens a dialog and selects a file"""
  filename = filedialog.askopenfilename(
    filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
  )
  if filename:
    file_entry.delete(0, tk.END)
    file_entry.insert(0, filename)


def process_data():
  """ Function that processes the input data."""
  filename = file_entry.get()
  n_students = int(param_entry.get())

  # Checks that the input data have been entered.
  if not filename or not n_students:
    messagebox.showwarning("Input Error", "Please select a file and enter a n_students.")
    return

  try:
    output = get_namelist(filename, n_students)
    # Font object
    font_obj = tkfont.Font(size=20, family="monospace")

    # adds a Message
    entry_names = tk.Message(root, text=output, font=font_obj)
    entry_names.grid(row=3, column=1, padx=10, pady=10, sticky="e")

  except Exception as e:
    messagebox.showerror("Error", f"An error occurred: {e}")


def get_namelist(filename, number):
  """Function that obtains the desired namelist """
  namelist = []
  with open(filename, newline='', encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      namelist.append(row['Nombre'] + ' ' + row['Apellido(s)'])

  chosen = random.sample(namelist, k=number)
  my_string = ""
  for student in chosen:
    my_string = my_string + student + "\n\n"

  print(my_string)
  return my_string


def exit_program():
  root.destroy()


# main window
root = tk.Tk()
# title of the window
root.title("Lotería de alumnos")

# Widget creation and positioning
tk.Label(root, text="Select File:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=10, pady=10)

browse_button = tk.Button(root, text="Browse...", command=browse_file)
browse_button.grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Number of students:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
param_entry = tk.Entry(root, width=50)
param_entry.grid(row=1, column=1, padx=10, pady=10)

process_button = tk.Button(root, text="Process", command=process_data)
process_button.grid(row=2, column=1, padx=10, pady=20)

exit_button = tk.Button(root, text="Close", command=exit_program)
exit_button.grid(row=2, column=2, padx=10, pady=20)

root.mainloop()
