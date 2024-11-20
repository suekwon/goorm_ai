import tkinter as tk
from math import sin, cos, tan, log, sqrt, pi, e

# Initialize the main application window
root = tk.Tk()
root.title("계산기")
root.geometry("400x600")
root.resizable(False, False)

# Variables
current_input = tk.StringVar(value="0")

# Functions for calculator logic


def on_button_click(value):
    global current_input
    current_text = current_input.get()

    if value == "CE":
        current_input.set("0")
    elif value == "=":
        try:
            # Evaluate the expression safely
            expression = current_text.replace(
                "×", "*").replace("÷", "/").replace("π", str(pi)).replace("e", str(e))
            result = eval(expression)
            current_input.set(str(result))
        except Exception:
            current_input.set("Error")
    else:
        if current_text == "0":
            current_input.set(value)
        else:
            current_input.set(current_text + value)


# Create calculator UI
frame = tk.Frame(root, bg="white")
frame.pack(expand=True, fill="both", padx=10, pady=10)

# Display screen
display = tk.Label(frame, textvariable=current_input, font=(
    "Arial", 24), anchor="e", bg="lightgray", fg="black", height=2, relief="sunken")
display.pack(fill="x", pady=5)

# Buttons configuration
buttons = [
    ["Rad", ".", "Deg", "CE"],
    ["sin", "cos", "tan", "("],
    ["x!", "ln", "π", ")"],
    ["log", "e", "√", "×"],
    ["Ans", "EXP", "xʸ", "÷"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "x"]
]

# Button grid layout
for row_idx, row in enumerate(buttons):
    button_row = tk.Frame(frame)
    button_row.pack(fill="x")
    for col_idx, button in enumerate(row):
        def action(val=button): return on_button_click(val)
        tk.Button(
            button_row,
            text=button,
            font=("Arial", 16),
            width=5,
            height=2,
            command=action,
            bg="lightgray" if button not in ["CE", "="] else (
                "green" if button == "=" else "red"),
            fg="white" if button in ["CE", "="] else "black"
        ).pack(side="left", padx=5, pady=5, fill="x", expand=True)

# Run the main application loop
root.mainloop()
