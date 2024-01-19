import tkinter as tk
import pyttsx3

class DesktopAssistant:
    def __init__(self, master):
        self.master = master
        self.master.title("Desktop Assistant")

        # Set background color
        self.master.configure(bg="lightblue")

        self.label = tk.Label(master, text="Desktop Assistant", font=("Helvetica", 16), bg="lightblue")
        self.label.pack(pady=10)

        self.textbox = tk.Entry(master, width=40, bg="white")
        self.textbox.pack(pady=10)

        self.listen_button = tk.Button(master, text="Listen", command=self.listen, bg="green", fg="white")
        self.listen_button.pack(pady=10)

        self.text_output = tk.Text(master, height=5, width=50, bg="white")
        self.text_output.pack(pady=10)

        self.speak_button = tk.Button(master, text="Speak", command=self.speak, bg="orange", fg="white")
        self.speak_button.pack(pady=10)

        self.quit_button = tk.Button(master, text="Quit", command=master.destroy, bg="red", fg="white")
        self.quit_button.pack(pady=10)

        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)

    def listen(self):
        query = self.textbox.get()
        self.text_output.insert(tk.END, f"User: {query}\n")
        self.textbox.delete(0, tk.END)

    def speak(self):
        query = self.text_output.get("1.0", tk.END).strip()
        if query:
            self.engine.say(query)
            self.engine.runAndWait()
            self.text_output.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = DesktopAssistant(root)
    root.mainloop()
