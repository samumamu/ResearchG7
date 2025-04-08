import tkinter as tk
import ctypes

class CustomWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1380x720")
        self.root.overrideredirect(True)

        self.fix_taskbar_window()
        self.create_title_bar()
        self.create_main_content()

    def fix_taskbar_window(self): 
        #GPT
        self.root.update_idletasks()
        hwnd = ctypes.windll.user32.GetParent(self.root.winfo_id())

        GWL_EXSTYLE = -20
        WS_EX_APPWINDOW = 0x00040000
        WS_EX_TOOLWINDOW = 0x00000080

        ex_style = ctypes.windll.user32.GetWindowLongPtrW(hwnd, GWL_EXSTYLE)
        ex_style = ex_style & ~WS_EX_TOOLWINDOW | WS_EX_APPWINDOW
        ctypes.windll.user32.SetWindowLongPtrW(hwnd, GWL_EXSTYLE, ex_style)

   
        self.root.withdraw()
        self.root.after(10, self.root.deiconify)

    def create_title_bar(self):
        self.title_bar = tk.Frame(self.root, bg="#2b2b2b", height=30)
        self.title_bar.pack(fill='x')

        self.title_label = tk.Label(self.title_bar, text="RS Group 7", fg="white", bg="#2b2b2b")
        self.title_label.pack(side='left', padx=10)

        close_button = tk.Button(self.title_bar, text='✕', command=self.root.destroy,
                                 bg="#2b2b2b", fg="white", bd=0, highlightthickness=0,
                                 activebackground='red', activeforeground='white')
        close_button.pack(side='right', padx=10)

        self.title_bar.bind('<B1-Motion>', self.move_window)
        self.title_bar.bind('<Button-1>', self.get_pos)

    def get_pos(self, event):
        self.xwin = event.x
        self.ywin = event.y

    def move_window(self, event):
        self.root.geometry(f'+{event.x_root - self.xwin}+{event.y_root - self.ywin}')

    def create_main_content(self):
        content = tk.Frame(self.root, bg='white')
        content.pack(expand=True, fill='both')
        label = tk.Label(content, text="Main Content", bg='white')
        label.pack(pady=100)

if __name__ == "__main__":
    app = CustomWindow()
    app.root.mainloop()

# can u see this chester