import tkinter as tk

font0 = 'Consolas 10'


def tkwindow(title, window=(20, 20, 500, 300), color='gray80'):
    tkw = tk.Tk()
    tkw.title(title)
    x0, y0, ax, ay = window
    tkw.geometry(f'{ax}x{ay}+{x0}+{y0}')
    tkw.config(bg=color)
    return tkw


tkw = tkwindow(title='aaa')


class CmdButton:
    def __init__(self, frame=tkw, xyw=(100, 50, 3), text='btn', colors=('gray70', 'yellow'), toggle=False):
        x, y, w = xyw
        off_color, on_color = colors
        self.button = tk.Button(frame, text=text, bg=off_color, width=w, font=font0)
        self.button.place(x=x, y=y)
        self.on_color = on_color
        self.off_color = off_color
        if toggle:
            self.command(self.switch)

    def command(self, command):
        self.button.config(command=command)

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

    def color(self, color):
        self.button['bg'] = color


class ParamEntry:
    def __init__(self, frame=tkw, xyw=(100, 100, 5), val=0, label='entry'):
        x, y, w = xyw
        self.entry = tk.Entry(frame, font=font0, justify=tk.RIGHT)
        self.entry['width'] = w
        self.entry.place(x=x, y=y)
        self.set_entry(val)
        self.lbl = tk.Label(frame, text=label, bg=frame['background'])
        self.lbl.place(x=x, y=y)
        frame.update_idletasks()
        lw = self.lbl.winfo_width()
        self.lbl.place(x=x-lw-2, y=y+3)

    def set_entry(self, val):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, val)
        self.entry.xview_moveto(1.)

    def get_val(self, typ=int):
        try:
            val = typ(self.entry.get())
        except ValueError:
            if typ == str:
                val = ''
            else:
                val = 0
        return val

    def get_list_val(self, typ=int):
        aa = self.entry.get()
        bb = aa.split()
        cc = [typ(b) for b in bb]
        return cc


class ProgressBar:
    def __init__(self, frame=tkw, xyw=(100, 150, 100), label='progress'):
        import tkinter.ttk as ttk
        x, y, w = xyw
        self.prog = ttk.Progressbar(frame)
        self.prog.place(x=x, y=y)
        self.lbl = tk.Label(frame, text=label, bg=frame['background'])
        self.lbl.place(x=x, y=y)
        frame.update_idletasks()
        lw = self.lbl.winfo_width()
        self.lbl.place(x=x-lw-2, y=y)

    def setval(self, val):
        self.prog['value'] = val
        self.prog.update_idletasks()

    def getval(self):
        val = self.prog['value']
        return val


if __name__ == '__main__':

    btn1 = CmdButton()
    ent1 = ParamEntry(xyw=(100, 100, 30))
    aaa = [11, 22, 33, 44, 55]
    ent1.set_entry(aaa)
    c = ent1.get_list_val()
    print(f'c = {c}')
    prog = ProgressBar()
    prog.setval(75)

    tk.mainloop()

