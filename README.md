# 🧮 Advanced Calculator using Python & Tkinter

A sleek and functional GUI-based calculator built with Python's Tkinter library.  
This calculator supports **basic arithmetic operations**, **advanced functions**, and **constants** like π — all wrapped in a clean, responsive interface.

---

## 🚀 Features
- ✅ **Basic Operations:** Addition, Subtraction, Multiplication, Division  
- 🧠 **Advanced Functions:** Power (^), Square Root (√), Logarithm (log), Percentage (%)  
- 🔢 **Constants:** π (Pi)  
- 🖥️ **GUI:** Built with Tkinter  
- 🧼 **Clear Button:** Reset input  
- 🧮 **Real-time Expression Rendering**  
- 🧩 **Expression Parsing:** Supports parentheses  

---

## 📸 Interface Preview
*A screenshot or GIF of the calculator in action can be added here.*

---

## 🛠️ Installation

1. **Clone the repository**:
```bash
git clone https://github.com/your-username/advanced-calculator.git
cd advanced-calculator
Run the application (make sure Python 3 is installed):

bash
Copy code
python calculator.py
📦 Dependencies
Python 3.x

Tkinter (pre-installed with most Python distributions)

math module (standard library)

🧠 How It Works
User input is dynamically built as a string.

Special symbols like ^ and √ are parsed and converted to Python-compatible expressions.

The eval() function computes the result, with error handling for invalid inputs.

The GUI updates in real-time to reflect the current expression or result.

⚠️ Notes
This calculator uses Python’s eval() for expression evaluation. While safe in this context, avoid using eval() with untrusted input in production.

Logarithmic input must be closed with a parenthesis manually (e.g., log(100)).

📌 To-Do / Future Enhancements
Add support for trigonometric functions (sin, cos, tan)

Implement memory storage (M+, M-, MR)

Improve square root and log parsing for nested expressions

Add keyboard input support

🧑‍💻 Author
Shihab –
Fluent in Python, Pygame, and machine learning workflows. Passionate about building interactive applications and educational tools.

📄 License
This project is licensed under the MIT License. Feel free to use, modify, and distribute.
