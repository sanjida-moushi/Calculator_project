from tkinter import Tk, Button, Entry

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.configure(bg="lightblue")

        # Entry field for display
        self.display = Entry(root, font=("Arial", 20), bg="white", bd=5, relief="sunken", justify="right")
        self.display.place(x=10, y=10, width=280, height=50)

        # Button layout
        button_texts = [
            "(", ")", "%", "C",
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        # Create buttons dynamically
        for i, text in enumerate(button_texts):
            row, col = divmod(i, 4)
            Button(
                root, text=text, width=5, height=2, bg="pink", relief="flat",
                command=lambda t=text: self.on_button_click(t)
            ).place(x=col * 75, y=80 + row * 70)

    def on_button_click(self, value):
        # Handle button click
        if value == "C":
            self.display.delete(0, "end")  # Clear the display
        elif value == "=":
            try:
                # Evaluate the expression in the display
                result = eval(self.display.get())
                self.display.delete(0, "end")
                self.display.insert("end", str(result))
            except Exception as e:
                self.display.delete(0, "end")
                self.display.insert("end", "Error")
        else:
            # Add the button's value to the display
            self.display.insert("end", value)

if __name__ == "__main__":
    root = Tk()
    calc = Calculator(root)
    root.mainloop()
