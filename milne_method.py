eps = 1e-6
def rk_4_method(x0, y0, h, func):
    k1 = h*func(x0, y0)
    k2 = h*func(x0+h/2, y0+k1/2)
    k3 = h*func(x0+h/2, y0+k2/2)
    k4 = h*func(x0 + h, y0 + k3)
    return y0 + (k1 + 2*k2 + 2*k3 + k4)/6

def milne_method(x0, y0, h, f, xn):
    xvals = [x0]
    yvals = [y0]
    steps = int((xn -x0)/h)
    for i in range(3):
        yvals.append(rk_4_method(xvals[-1], yvals[-1], h, f))
        xvals.append(xvals[-1] + h)

    for i in range(steps - 3):
        pred = yvals[-4] + 4*h*(2*f(xvals[-1], yvals[-1]) - f(xvals[-2], yvals[-2]) + 2*f(xvals[-3], yvals[-3]))/3

        corrected = yvals[-2] + h*(f(xvals[-1] + h, pred) + 4*f(xvals[-1], yvals[-1]) + f(xvals[-2], yvals[-2]))/3
        yvals.append(corrected)
        xvals.append(round(xvals[-1] + h, 1))

    return xvals, yvals


if __name__ == "__main__":
    def f(x, y):
        return x*x + y*y

    x0 = 0
    y0 = 1
    h = 0.1
    xn = 1

    xvals, yvals = milne_method(x0, y0, h, f, xn)
    for i in range(len(xvals)):
        print(f"x = {xvals[i]}, y = {yvals[i]}")
