import numpy as np
import general_functions as gf


class Data2D(np.ndarray):
    def __init__(self, aaa):
        super().__init__(aaa)


def renormalize(aa, alimit, blimit, btype=None):

    atype = type(aa)
    aa = aa.astype(float)
    if alimit:
        aa = np.clip(aa, alimit[0], alimit[1])
    else:
        alimit = (np.min(aa), np.max(aa))
    amin, amax = alimit
    bmin, bmax = blimit
    bb = bmin + (bmax - bmin) * (aa - amin) / (amax - amin)
    if btype:
        bb = bb.astype(btype)
    else:
        bb = bb.astype(atype)

    return bb


def get_roi(aa, roi):
    rx0, ry0, rx, ry = roi
    return aa


if __name__ == '__main__':

    aa = Data2D(range(10))
    print(f'aa = {aa}')
    gf.what_is('aa', aa)



