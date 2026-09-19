import tkinter as tk
reset_display = False

def click(event):
    global reset_display

    current = entry.get()
    button_text = event.widget.cget("text")
    operators = "+-*/%"

    if button_text == "C":
        entry.delete(0, tk.END)
        entry.insert(tk.END, "0")
        reset_display = False
        return

    if button_text == "=":
        try:
            expression = current.replace('%', '/100')
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
            reset_display = True
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error!")
            reset_display = True
        return

    # Handle continuing after a result
    if reset_display:
        if button_text in operators:
            # keep the previous result, just append the operator
            reset_display = False
        else:
            # starting a brand-new number clears the old result
            entry.delete(0, tk.END)
            current = ""
            reset_display = False

    if current == "0":
        current = ""

    # Avoid 2 consecutive operators
    if current and current[-1] in operators and button_text in operators:
        current = current[:-1]

    # Avoid starting an expression with certain operators
    if current == "" and button_text in "*/%":
        return

    entry.delete(0, tk.END)
    entry.insert(tk.END, current + button_text)

root = tk.Tk() #main window
root.title("Calculator")
root.geometry("300x400") #size of the window
root.resizable(False, False) #disable resizing
root.configure(bg="#F0F0F0") #background color

#Entry widget
entry = tk.Entry(root, bd=5, font=("Arial", 20), justify="right",width=17, bg ="#b6f2e9")
entry.pack(pady=6)

#Button Frame
btn_frame = tk.Frame(root, bg="#F0F0F0")
btn_frame.pack(padx=10, pady=10)

# Calculator buttons
buttons = [['C','(',')','/'],
           ['7','8','9','*'],
           ['4','5','6','-'],
           ['1','2','3','+'],
           ['.','0','%','=']]

for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        btn = tk.Button(btn_frame, text=buttons[i][j], width=3, height=1, font=("Arial", 16))
        btn.grid(row=i, column=j, padx=10, pady=10)
        btn.bind("<Button-1>", click) #bind the button to the click function



root.mainloop() #run the main loop
