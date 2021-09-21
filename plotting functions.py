import numpy as np
import matplotlib.pyplot as plt

dpi = 100


def plotAA(AA, figname='plotAA', caption='', aminmax=(), xybox=(1, 1), sxy=(1, 1), cmap='gray', pause=0.):
    """
    xybox: () no axes; (1, 1) pixel index; (dx, dy) axes scale; (ax1, ax2, ay1, ay2) x, y ranges
    sxy = (sx, sy): stretch figure from default size
    """

    ny, nx = np.shape(AA)
    figxy = (nx * sxy[0] / dpi, ny * sxy[1] / dpi)

    if aminmax:
        AA = np.clip(AA, aminmax[0], aminmax[1])

    nobox = (len(xybox) == 0)
    if nobox:
        xybox = [0, 1, 0, 1]
    if len(xybox) == 2:
        dx, dy = xybox
        xybox = (0, nx * dx, 0, ny * dy)

    plt.figure(figname, figsize=figxy, dpi=dpi, tight_layout=True)
    plt.clf()
    plt.imshow(AA, cmap=cmap, aspect='auto', extent=xybox)
    plt.title(caption)

    fig = plt.gca()
    if nobox:
        fig.axes.get_xaxis().set_visible(False)
        fig.axes.get_yaxis().set_visible(False)

    if pause:
        plt.pause(pause)
    else:
        plt.show()


def graphB(B, figname='graphB', caption='', aminmax=(), xbox=(1,), sxy=(1, .3), line='#1f77b4', pause=0.):
    """
    xbox: () no x-axis; (1,) pixel index; (dx,) x-axis scale; (ax1, ax2) x range
    sxy = (sx, sy): stretch figx by sx and figy by sy * figx
    """

    B = np.transpose(B)
    nx = len(B)
    sx, sy = sxy
    figxy = (nx * sx / dpi, nx * sx * sy / dpi)

    xx = np.arange(nx)
    if len(xbox) == 1:
        xx = np.arange(nx) * xbox
    if len(xbox) == 2:
        ax1, ax2 = xbox
        xx = np.arange(nx) * (ax2 - ax1) / nx + ax1

    plt.figure(figname, figsize=figxy, tight_layout=True)
    plt.clf()
    plt.plot(xx, B, line)

    plt.title(caption)
    plt.autoscale(enable=True, axis='x', tight=True)
    if aminmax:
        plt.ylim(aminmax)
    plt.grid(True)

    fig = plt.gca()
    if len(xbox) == 0:
        fig.xaxis.set_visible(False)

    if pause:
        plt.pause(pause)
    else:
        plt.show()


def plotAAB(AA, figname='plotAAB', capA='', capB='', cmap='gray', line='#1f77b4', cursor=False,
            aminmax=(), xybox=(1, 1), roi=(), sxy=(1, 1), aby=(2, 1), pause=0.):
    """
    xybox: () no axes; (1, 1) pixel index; (dx, dy) axes scale; (ax1, ax2, ay1, ay2) x, y ranges
    sxy = (sx, sy): stretch figure from default size
    aby = (ay, by): relative y-size of AA and B
    """

    ''' plotAA '''
    ny, nx = np.shape(AA)
    sx, sy = sxy
    ay, by = aby
    figxy = (nx * sx / dpi, ny * sy * ((ay + by) / ay) / dpi)

    if aminmax:
        AA = np.clip(AA, aminmax[0], aminmax[1])

    nobox = (len(xybox) == 0)
    if nobox:
        xybox = [0, 1, 0, 1]
    if len(xybox) == 2:
        dx, dy = xybox
        xybox = (0, nx * dx, 0, ny * dy)

    plt.figure(figname, figsize=figxy, dpi=dpi, tight_layout=True)
    plt.clf()
    plt.subplot2grid((ay + by, 1), (0, 0), rowspan=ay)
    plt.imshow(AA, cmap=cmap, aspect='auto', extent=xybox)
    plt.title(capA)

    fig = plt.gca()
    if nobox:
        fig.axes.get_xaxis().set_visible(False)
        fig.axes.get_yaxis().set_visible(False)

    """ put cursor """
    cline = 'yellow'
    croi = 'cyan'
    alpha = 0.75

    ax1, ax2, ay1, ay2 = xybox
    if len(roi) == 0:
        roi = ((ax1 + ax2)/2, (ay1 + ay2)/2, (ax2 - ax1)/100, (ay2 - ay1)/100)
    rx0, ry0, rx, ry = roi

    rx1 = rx0 - rx/2
    rx2 = rx0 + rx/2
    ry1 = ry0 - ry/2
    ry2 = ry0 + ry/2

    if cursor:
        plt.axhline(y=ry0, color=cline, alpha=alpha)
        # plt.axvline(x=rx0, color=cline, alpha=alpha)
        plt.plot([rx1, rx2, rx2, rx1, rx1], [ry1, ry1, ry2, ry2, ry1], color=croi, alpha=alpha)

    """ graphB """
    iy = int(ny * (ry0 - ay1) / (ay2 - ay1))
    B = AA[iy, :]

    xx = np.arange(nx)
    if len(xybox) == 2:
        xx = np.arange(nx) * xybox[0]
    if len(xybox) == 4:
        ax1, ax2 = (xybox[0], xybox[1])
        xx = np.arange(nx) * (ax2 - ax1) / nx + ax1

    plt.subplot2grid((ay + by, 1), (ay , 0), rowspan=by)
    plt.plot(xx, B, line)
    plt.title(capB)
    plt.autoscale(enable=True, axis='x', tight=True)
    if aminmax:
        plt.ylim(aminmax)
    plt.grid(True)
    fig = plt.gca()
    if nobox:
        fig.xaxis.set_visible(False)

    if pause:
        plt.pause(pause)
    else:
        plt.show()


def graph_many():
    pass


def mayaviAA():
    pass


if __name__ == '__main__':
    aa = np.random.rand(1000, 1500)
    # plotAA(aa, figname='fig1', caption='AA', sxy=(.5, .5), cmap='jet', pause=.1)
    b = aa[0:2, :]
    # graphB(b, caption='B', xbox=(.5,), sxy=(.5, .5), pause=.1)
    plotAAB(aa, roi=(.25, 2, .1, .5), sxy=(.5, .5), xybox=(-1, 1, 0, 10), cursor=True, capA='AA', capB='B')

