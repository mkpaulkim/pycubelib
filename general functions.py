import numpy as np
import datetime

pi = np.pi
pi2 = pi * 2


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




