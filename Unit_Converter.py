import tkinter as tk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature():
    if temperature_var.get() == "Celsius to Fahrenheit":
        celsius = float(input_entry.get())
        result = celsius_to_fahrenheit(celsius)
    else:
        fahrenheit = float(input_entry.get())
        result = fahrenheit_to_celsius(fahrenheit)
    result_label.config(text=f"Result: {result:.2f} {temperature_var.get()}")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Create a label
title_label = tk.Label(window, text="Temperature Converter", font=("Helvetica", 16))
title_label.pack(pady=10)

# Create an entry field
input_label = tk.Label(window, text="Enter Temperature:")
input_label.pack()
input_entry = tk.Entry(window)
input_entry.pack()

# Create a dropdown menu for temperature options
temperature_var = tk.StringVar()
temperature_var.set("Celsius to Fahrenheit")
options = ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
temperature_menu = tk.OptionMenu(window, temperature_var, *options)
temperature_menu.pack()

# Create a button to convert temperature
convert_button = tk.Button(window, text="Convert", command=convert_temperature)
convert_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(window, text="", font=("Helvetica", 14))
result_label.pack()

# Start the application
window.mainloop()
