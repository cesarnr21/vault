#!/usr/bin/env python3
import numpy as np
import time
from matplotlib import cm, colors
import seaborn as sns

mod = 10
boldmod = 10
rgba255 = np.zeros(4)
CSI = '\033'
spins = '⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'
cmap = sns.husl_palette(as_cmap=True)
# https://stackoverflow.com/questions/3942878/how-to-decide-font-color-in-white-or-black-depending-on-background-color
# thresh = np.array([0.299, 0.587, 0.114, 0])

def wrap_color(a_string, rgba255=(255,0,0,0), is_bold=False):
    # bgstart = CSI+'[40m' if (rgba255 * thresh).sum() < 186 else CSI+'[47m'
    boldstart = CSI+'[1m' if is_bold else ''
    boldstop = CSI+'[0m' if is_bold else ''
    reset = CSI + '[0m'
    return f'{boldstart}{CSI}[38;2;{rgba255[0]:.0f};{rgba255[1]:.0f};{rgba255[2]:.0f}m{a_string}{boldstop}{reset}'

while True:
    try:
        now = time.time()
        remaining = 1.7e9-now
        rgba255[:] = cmap((remaining % mod)/mod)
        rgba255 *= 255
        is_bold = (remaining % boldmod) < 1
        spindx = int(remaining*10 % mod)

        # NOTE: the reason why the spins do not work anymore is because the time was reached
        # no time remainding
        spin = '✯' if remaining < 0 else spins[spindx]
        print('Celebration '+wrap_color('1700000000.000 '+spin, rgba255, is_bold))
        print('Currently   '+wrap_color(f'{now:>14.3f}', rgba255, is_bold))
        print('Remaining   '+wrap_color(f'{remaining:>14.3f}', rgba255, is_bold))

        # NOTE: is this what's used to keep the lines at 3?
        print(f"{CSI}[3A",end='') # move up 3 lines
        # time.sleep(.01)

    except KeyboardInterrupt:
        print(f'{CSI}[39;49m{CSI}[0m\n\n\n')
        break

