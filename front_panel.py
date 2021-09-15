import tkinter as tk


class TkWindow:
    def __init__(self, title='TkWindow', window=(20, 20, 500, 300), color='gray'):
        self.tkw = tk.Tk()
        self.tkw.title(title)
        x0, y0, ax, ay = window
        self.tkw.geometry(f'{ax}x{ay}+{x0}+{y0}')
        self.tkw.config(bg=color)


class PushButton:
    def __init__(self, tkw, text, xyw, colors=('yellow', 'cyan')):
        color_off, color_on =colors
        self.button = tk.Button(tkw, text=text, bg=color_off, font=font1)


if __name__ == '__main__':
    tkw = TkWindow(color='orange')
    tk.mainloop()

