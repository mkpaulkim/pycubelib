import numpy as np
import datetime

pi = np.pi
pi2 = pi * 2


def runstamp(script_path):
    s_path, _ = path_parts(script_path, 2)
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    stamp = f'[.../{s_path}] {time_stamp}'
    return stamp


def path_parts(full_path, nlast=2):

    base_path, fname_ext = os.path.split(full_path)
    fname, ext = os.path.splitext(fname_ext)

    rest_path = full_path
    parts = []
    for n in range(nlast):
        rest_path, part = os.path.split(rest_path)
        parts = [part] + parts
    short_path = f'{"/".join(parts)}'

    parts_dict = {'full_path': full_path, 'base_path': base_path, 'fname': fname, 'ext': ext, 'short_path': short_path}

    return short_path, parts_dict


def what_is(name, var, cmax=200):
    if type(var) == str:
        vlen = f' of len {len(var)}'
    elif type(var) == list:
        vlen = f' of len {len(var)}'
    elif type(var) == np.ndarray:
        vlen = f' of size {var.shape} of element type {type(var.reshape(np.product(var.shape))[0])}'
    else:
        vlen = ''

    output = f'> {name} is {type(var)}' + vlen + f': {name} = {var}'
    if cmax and (len(output) > cmax):
        output = output[:cmax] + ' ...'
    print(output)
    return output


if __name__ == '__main__':
    from tkinter import filedialog
    import os

    this_path = os.path.abspath(__file__)
    print(runstamp(this_path))
    f_path = filedialog.askopenfilename()
    s_path, dict_parts = path_parts(f_path)
    print(f'short_path = {s_path}')
    print(f'fname = {dict_parts["fname"]}')



