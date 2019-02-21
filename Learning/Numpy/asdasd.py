

import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(h, w, maxit=50):
    y, x = np.ogrid[-2:0.8:w * 1j , -1.5:4.5:h * 1j, ]
    c = x + y * 1j
    asd = c
    divtime = maxit + np.zeros(asd.shape, dtype=int)

    for i in range(maxit):
        asd = asd ** 2 + c
        diverge = asd * np.conj(asd) > 4 ** 5  # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i  # note when
        asd[diverge] = 2  # avoid diverging too much

    return divtime


plt.imshow(mandelbrot(600, 600))
plt.show()