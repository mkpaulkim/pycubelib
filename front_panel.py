import tkinter as tk

font0 = 'Consolas 10'


def tkwindow(title, window=(20, 20, 500, 300), color='gray'):
    tkw = tk.Tk()
    tkw.title(title)
    x0, y0, ax, ay = window
    tkw.geometry(f'{ax}x{ay}+{x0}+{y0}')
    tkw.config(bg=color)
    return tkw


class CmdButton:
    def __init__(self, frame, comm, text='push', xyw=(0, 0, 3), colors=('gray', 'yellow'), toggle=False):
        x, y, w = xyw
        off_color, on_color = colors
        self.button = tk.Button(frame, text=text, bg=off_color, width=w, font=font0)
        self.button.place(x=x, y=y)
        self.on_color = on_color
        self.off_color = off_color
        if toggle:
            # self.command(self.switch)
            self.button.config(command=comm)

    def command(self, command):
        self.button.config(command=command)

    def color(self, color):
        self.button['bg'] = color

    def on(self):
        self.button['bg'] = self.on_color

    def off(self):
        self.button['bg'] = self.off_color

    def is_on(self):
        return self.button['bg'] == self.on_color

    def switch(self):
        if self.is_on():
            self.off()
        else:
            self.on()


if __name__ == '__main__':
    tkw = tkwindow(title='aaa')
    btn1 = CmdButton(tkw, toggle=True)

    tk.mainloop()
