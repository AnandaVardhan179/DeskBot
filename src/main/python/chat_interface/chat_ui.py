import tkinter as tk
from chat_bot import get_response


class ChatInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("DeskBot Chat Interface")

        self.chat_log = tk.Text(root, bd=1, bg="white", width=50, height=8, font=("Arial", 12), wrap=tk.WORD)
        self.chat_log.config(state=tk.DISABLED)

        self.scrollbar = tk.Scrollbar(root, command=self.chat_log.yview)
        self.chat_log['yscrollcommand'] = self.scrollbar.set

        self.entry_box = tk.Text(root, bd=0, bg="white", width=29, height=5, font=("Arial", 12))

        self.send_button = tk.Button(root, text="Send", width=12, height=5, bd=0, bg="#32de97",
                                     activebackground="#3c9d9b", fg='#ffffff', command=self.send_message)

        self.chat_log.grid(row=0, column=0, columnspan=2)
        self.scrollbar.grid(row=0, column=2, sticky='ns')
        self.entry_box.grid(row=1, column=0)
        self.send_button.grid(row=1, column=1)

    def send_message(self):
        user_message = self.entry_box.get("1.0", tk.END).strip()
        if user_message:
            self.chat_log.config(state=tk.NORMAL)
            self.chat_log.insert(tk.END, "You: " + user_message + '\n\n')
            self.chat_log.config(foreground="#442265", font=("Verdana", 12))

            response = get_response(user_message)
            self.chat_log.insert(tk.END, "Bot: " + response + '\n\n')

            self.chat_log.config(state=tk.DISABLED)
            self.chat_log.yview(tk.END)

            self.entry_box.delete("1.0", tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatInterface(root)
    root.mainloop()
