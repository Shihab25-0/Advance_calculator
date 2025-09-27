
import tkinter as tk
import math

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.config(state='normal')
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
    text_result.config(state='disabled')

def evaluate_calculation():
    global calculation
    try:
        # Handle power and square root 
        calculation = calculation.replace('^', '**')
        if '√' in calculation:
            # Extract number after √ and calculate its square root
            index = calculation.index('√') + 1
            number = ""
            while index < len(calculation) and (calculation[index].isdigit() or calculation[index] == '.'):
                number += calculation[index]
                index += 1
            if number:
                result = math.sqrt(float(number))
                calculation = calculation.replace(f"√{number}", str(result))
        calculation = str(eval(calculation))
        text_result.config(state='normal')
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
        text_result.config(state='disabled')
    except Exception as e:
        clear_field()
        text_result.config(state='normal')
        text_result.insert(1.0, "Error")
        text_result.config(state='disabled')

def clear_field():
    global calculation
    calculation = ""
    text_result.config(state='normal')
    text_result.delete(1.0, "end")
    text_result.config(state='disabled')

#Window
app = tk.Tk()
app.title("Advanced Calculator")
app.geometry("400x600") 
app.resizable(False, False)

#Screen
text_result = tk.Text(app, height=2, width=22, font=("Arial", 24), state='disabled', bg="light yellow")
text_result.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
text_result.config(state='normal')

# Button Specification
button_specs = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 1), ('.', 4, 0), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('^', 5, 3),
    ('√', 6, 0), ('%', 6, 1), ('π', 6, 2), ('log', 6, 3)  
]

#Button
for (text, row, col) in button_specs:
    if text == '=':
        tk.Button(app, text=text, command=evaluate_calculation, width=5, height=2, font=("Arial", 18), bg="light green").grid(row=row, column=col, padx=5, pady=5)
    elif text == 'C':
        tk.Button(app, text=text, command=clear_field, width=5, height=2, font=("Arial", 18), bg="light coral").grid(row=row, column=col, padx=5, pady=5)
    elif text == 'π':
        tk.Button(app, text=text, command=lambda: add_to_calculation(math.pi), width=5, height=2, font=("Arial", 18)).grid(row=row, column=col, padx=5, pady=5)
    elif text == 'log':
        tk.Button(app, text=text, command=lambda: add_to_calculation('math.log('), width=5, height=2, font=("Arial", 18)).grid(row=row, column=col, padx=5, pady=5)
    elif text == '%':
        tk.Button(app, text=text, command=lambda: add_to_calculation('%'), width=5, height=2, font=("Arial", 18)).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(app, text=text, command=lambda t=text: add_to_calculation(t), width=5, height=2, font=("Arial", 18)).grid(row=row, column=col, padx=5, pady=5)

app.mainloop()
