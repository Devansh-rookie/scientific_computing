eps = 1e-6
def rk_4_method(x0, y0, h, func):
    k1 = h*func(x0, y0)
    k2 = h*func(x0+h/2, y0+k1/2)
    k3 = h*func(x0+h/2, y0+k2/2)
    k4 = h*func(x0 + h, y0 + k3)
    return y0 + (k1 + 2*k2 + 2*k3 + k4)/6


def adam_bashforth_4(x0, y0, h, func, xn):
    x_list = [x0]
    y_list = [y0]
    steps = int((xn - x0) / h)
    coeff = [55.0/24, -59.0/24, 37.0/24, -9.0/24]
    for i in range(3):
        y_list.append(rk_4_method(x_list[-1], y_list[-1], h, func))
        x_list.append(x_list[-1] + h)

    while steps - 2 > 0:
        n = len(x_list) - 1
        fvals = []
        for i in range(4):
            fvals.append(func(x_list[n-i], y_list[n-i]))
        vals = 0.0
        for i in range(4):
            vals += coeff[i] * fvals[i]

        x_list.append(x_list[-1] + h)
        y_list.append(y_list[-1] + h*vals)
        steps-=1
    return x_list, y_list

if __name__ == "__main__":
    x0 = 1.0
    y0 = 1.0
    h = 0.0001
    xn = 1.4
    def f(x, y):
        return 1/x**2 - y/x
    x_list, y_list = adam_bashforth_4(x0, y0, h, f, xn)
    # print(x_list)
    # print(y_list)

    for i in range(len(x_list)):
        print(f"x = {x_list[i]}, y = {y_list[i]}")

    # Answers
    # x = 1.4000000000000004, y = 0.9546229678701645
    # x = 1.399999999999956, y = 0.9546230261580156
