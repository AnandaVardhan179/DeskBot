import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
from src.main.python.chat_interface.chat_ui import ChatInterface  # Import the ChatInterface class

class AuthInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("DeskBot Authentication")
        self.root.geometry("800x600")

        self.background_frame = tk.Frame(root, bg="#2C3E50")
        self.background_frame.place(relwidth=1, relheight=1)

        self.title_label = tk.Label(self.background_frame, text="DeskBot", font=("Arial", 24), fg="#FFFFFF", bg="#2C3E50")
        self.title_label.place(relx=0.05, rely=0.05)

        self.image_path = 'C:/Users/Anand/PycharmProjects/Project - DeskBot/src/resourses/images/DeskBot (1)-modified.png'
        self.img = Image.open(self.image_path)
        self.img = self.img.resize((200, 200), Image.Resampling.LANCZOS)  # Resize image if needed
        self.photo = ImageTk.PhotoImage(self.img)
        self.user_icon = tk.Label(self.background_frame, image=self.photo, bg="#2C3E50")
        self.user_icon.place(relx=0.5, rely=0.05, anchor="n")

        def EntryBox(root, entry_text, relx, rely, show=""):
            # Create a rounded rectangle image for the background
            width, height = 400, 50  # Dimensions of the entry box
            radius = 20  # Corner radius
            img = Image.new("RGBA", (width, height), (255, 255, 255, 0))
            draw = ImageDraw.Draw(img)
            draw.rounded_rectangle((0, 0, width, height), radius, fill="white")

            # Convert to PhotoImage for Tkinter
            rounded_bg = ImageTk.PhotoImage(img)

            # Create a label to hold the background image
            bg_label = tk.Label(root, image=rounded_bg, bg="#2C3E50")
            bg_label.image = rounded_bg  # Keep a reference to the image to avoid garbage collection
            bg_label.place(relx=relx, rely=rely, anchor="center")

            # Create the Entry widget on top of the rounded background
            entry = tk.Entry(root, font=("Arial", 16), width=25, bd=0, highlightthickness=0, show=show)
            entry.insert(0, entry_text)
            entry.place(relx=relx, rely=rely, anchor="center")

            return entry

        self.username_entry = EntryBox(self.background_frame, "Username", 0.5, 0.45)
        self.password_entry = EntryBox(self.background_frame, "Password", 0.5, 0.55, show="*")

        self.login_button = tk.Button(
            self.background_frame,
            text="Login",
            font=("Arial", 16),
            bg="#32de97",  # Green background color
            fg="#FFFFFF",
            activebackground="#3c9d9b",  # Slightly darker green when pressed
            activeforeground="#ffffff",  # Text color when pressed
            width=15,
            bd=0,  # Remove border for a flat look
            highlightthickness=0,
            command=self.login
        )

        def fade_in(widget, start=0, end=1, steps=20, delay=50):
            step = (end - start) / steps
            widget.attributes('-alpha', start)

            def fade():
                nonlocal start
                start += step
                if start <= end:
                    widget.attributes('-alpha', start)
                    widget.after(delay, fade)

            fade()

        # Apply fade-in to the login button
        self.login_button = tk.Button(
            self.background_frame,
            text="Login",
            font=("Arial", 16),
            bg="#32de97",
            fg="#FFFFFF",
            activebackground="#3c9d9b",
            activeforeground="#ffffff",
            width=15,
            bd=0,
            highlightthickness=0,
            command=self.login
        )
        self.login_button.place(relx=0.5, rely=0.65, anchor="center")
        fade_in(self.login_button)

        self.login_button.place(relx=0.5, rely=0.65, anchor="center")
        self.social_frame = tk.Frame(self.background_frame, bg="#2C3E50")
        self.social_frame.place(relx=0.85, rely=0.85, anchor="center")

        self.google_button = tk.Button(self.social_frame, text="Google", font=("Arial", 12), bg="#FFFFFF", fg="#000000")
        self.google_button.pack(side="left", padx=10)

        self.twitter_button = tk.Button(self.social_frame, text="Twitter", font=("Arial", 12), bg="#FFFFFF", fg="#000000")
        self.twitter_button.pack(side="left", padx=10)

        root.bind('<Return>', lambda event: self.login())

    def create_rounded_rectangle(self, width, height, radius, color):
        img = Image.new("RGBA", (width, height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        draw.rounded_rectangle((0, 0, width, height), radius, fill=color)
        return ImageTk.PhotoImage(img)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "testuser" and password == "password":  # Simplified example
            print(f"Login successful for {username}")
            self.open_chat_interface()
        else:
            print("Invalid credentials")

    def open_chat_interface(self):
        # Destroy the authentication interface and open the chat interface
        for widget in self.root.winfo_children():
            widget.destroy()
        ChatInterface(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    auth_gui = AuthInterface(root)
    root.mainloop()
