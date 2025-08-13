# Simple Calculator 
import tkinter as tk
from tkinter import messagebox

# Function to perform the selected operation
def calculate(operation):
    try:
        number1 = float(entry_num1.get())
        number2 = float(entry_num2.get())

        if operation == '+':
            result = number1 + number2
        elif operation == '-':
            result = number1 - number2
        elif operation == '*':
            result = number1 * number2
        elif operation == '/':
            if number2 == 0:
                raise ZeroDivisionError
            result = number1 / number2

        result_label.config(text=f"Result: {number1} {operation} {number2} = {result}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("240x220")  
window.resizable(False, False)

# Input for the first number
tk.Label(window, text="First Number:", font=("Arial", 9)).pack(pady=(5, 0))
entry_num1 = tk.Entry(window, width=20, font=("Arial", 9))
entry_num1.pack(pady=3)

# Input for the second number
tk.Label(window, text="Second Number:", font=("Arial", 9)).pack(pady=(5, 0))
entry_num2 = tk.Entry(window, width=20, font=("Arial", 9))
entry_num2.pack(pady=3)

# operation buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Operation Buttons
tk.Button(button_frame, text="+", width=5, command=lambda: calculate('+')).grid(row=0, column=0, padx=3, pady=3)
tk.Button(button_frame, text="-", width=5, command=lambda: calculate('-')).grid(row=0, column=1, padx=3, pady=3)
tk.Button(button_frame, text="*", width=5, command=lambda: calculate('*')).grid(row=1, column=0, padx=3, pady=3)
tk.Button(button_frame, text="/", width=5, command=lambda: calculate('/')).grid(row=1, column=1, padx=3, pady=3)

# display the result
result_label = tk.Label(window, text="Result:", font=("Arial", 10))
result_label.pack(pady=5)

# Run 
window.mainloop()
