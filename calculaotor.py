import tkinter as tk
from library.syntaxTree_N_RPN_eval import add_spaces,calculate_expression,calculate_expression_rpn,convert_to_rpn

operators = set(['+', '-', '*', '/', '**'])
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3}

def evaluate_expression():
    expression = entry.get()
    if mode.get() == "Syntax Tree":
        try:
            spaced_expression = add_spaces(expression, operators)
            result = calculate_expression(spaced_expression)
            result_str.set(f"Processed Expression: {spaced_expression}\nResult: {result}")
        except ValueError as e:
            result_str.set("Error: " + str(e))
    elif mode.get() == "RPN":
        try:
            spaced_expression = add_spaces(expression, operators)
            result = calculate_expression_rpn(spaced_expression)
            result_str.set(f"Processed Expression (RPN): {convert_to_rpn(spaced_expression)}\nResult: {result}")
        except ValueError as e:
            result_str.set("Error: " + str(e))


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Calculator")
    window.geometry("500x300")
    font_style = ("Helvetica", 12)
    entry = tk.Entry(window, font=font_style, width=30)
    entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


    mode = tk.StringVar()
    mode.set("Syntax Tree")
    syntax_tree_radio = tk.Radiobutton(window, text="Syntax Tree", variable=mode, value="Syntax Tree", font=font_style)
    syntax_tree_radio.grid(row=1, column=0, padx=10, pady=5)
    rpn_radio = tk.Radiobutton(window, text="RPN", variable=mode, value="RPN", font=font_style)
    rpn_radio.grid(row=1, column=1, padx=5, pady=5)
    evaluate_button = tk.Button(window, text="Evaluate", command=evaluate_expression, font=font_style)
    evaluate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    result_str = tk.StringVar()
    result_label = tk.Label(window, textvariable=result_str, font=font_style)
    result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x_offset = (window.winfo_screenwidth() - width) // 2
    y_offset = (window.winfo_screenheight() - height) // 2
    window.geometry(f"+{x_offset}+{y_offset}")

    window.mainloop()