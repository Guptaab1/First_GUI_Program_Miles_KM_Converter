x = """Welcome to the first GUI program.
We will create a miles to KM converter.
"""
print(x)

import tkinter


def button_clicked():
    miles = float(miles_entry.get())
    km = miles * 1.609
    output_text.config(text=f"{km}")
    print("I got clicked.")


window = tkinter.Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# Miles label
miles_label = tkinter.Label(text="Miles", font=("Arial", 14, "bold"))
miles_label.grid(column=3, row=0)

# Equal label
equal_label = tkinter.Label(text="is equal to", font=("Arial", 14, "bold"))
equal_label.grid(column=0, row=1)

# KM label
km_label = tkinter.Label(text="Km", font=("Arial", 14, "bold"))
km_label.grid(column=3, row=1)

# Miles Entry
miles_entry = tkinter.Entry(width=20)
miles_entry.grid(column=2, row=0)
miles_entry.get()

# Output Entry
output_text = tkinter.Label(text="0", font=("Arial", 14, "bold"))
output_text.grid(column=2, row=1)

# Calculate Button
calculate_button = tkinter.Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=2, row=2)


tkinter.mainloop()
