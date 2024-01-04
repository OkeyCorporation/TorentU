import tkinter as tk
import webbrowser

class DoooApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dota 3")
        self.root.configure(bg="black")

        self.label = tk.Label(root, text="Dota 3", font=("Arial", 24), fg="white", bg="black")
        self.label.pack(pady=50)

        # Плавное появление
        self.fade_in()

    def fade_in(self):
        alpha = 0.0
        self.root.attributes('-alpha', alpha)

        def fadeIn():
            nonlocal alpha
            if alpha < 1.0:
                alpha += 0.01
                self.root.attributes('-alpha', alpha)
                self.root.after(10, fadeIn)
            else:
                # После завершения появления, открываем ссылку и закрываем программу
                self.open_link()

        fadeIn()

    def open_link(self):
        webbrowser.open("https://youtu.be/dQw4w9WgXcQ?si=nArCXe7R_cVZ_StO")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300")  # Установите пользовательский размер окна
    app = DoooApp(root)
    root.mainloop()
