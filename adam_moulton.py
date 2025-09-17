eps = 1e-6
def rk_4_method(x0, y0, h, func):
    k1 = h*func(x0, y0)
    k2 = h*func(x0+h/2, y0+k1/2)
    k3 = h*func(x0+h/2, y0+k2/2)
    k4 = h*func(x0 + h, y0 + k3)
    return y0 + (k1 + 2*k2 + 2*k3 + k4)/6


def adam_moulton(f, x0, y0, h, xn):
    n = int((xn - x0) / h)
    x = [x0]
    y = [y0]

    for i in range(3):
        y.append(rk_4_method(x[i], y[i], h, f))
        x.append(round(x[i] + h, 6))

    for i in range(3, n):
        pred = y[-1] + h*(55*f(x[-1], y[-1]) - 59*f(x[-2], y[-2]) + 37*f(x[-3], y[-3]) - 9*f(x[-4], y[-4]))/24
        corrected = y[-1] + h*(9*f(x[-1] + h, pred) + 19*f(x[-1], y[-1]) - 5*f(x[-2], y[-2]) + f(x[-3], y[-3]))/24
        y.append(corrected)
        x.append(round(x[i] + h, 6))

    return x, y


if __name__ == "__main__":
    x0 = 0
    y0 = 1
    h = 0.01
    xn = 0.4
    def f(x, y):
        return x*y + y*y
    x_list, y_list = adam_moulton(f, x0, y0, h, xn)
    # print(x_list)
    # print(y_list)

    for i in range(len(x_list)):
        print(f"x = {x_list[i]}, y = {y_list[i]}")
