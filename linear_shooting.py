# y" = y + x
# y(0) = 0
# y(1) = 1
def f(x, y, z):
    # y'' = y + x
    return y + x

def rk4(f, x0, y0, z0, h, x_end):
    x = x0
    y = y0
    z = z0
    n = int((x_end - x0) / h)

    x_vals = [x]
    y_vals = [y]
    z_vals = [z]

    for i in range(n):
        k1y = z
        k1z = f(x, y, z)

        k2y = z + 0.5 * h * k1z
        k2z = f(x + 0.5 * h, y + 0.5 * h * k1y, z + 0.5 * h * k1z)

        k3y = z + 0.5 * h * k2z
        k3z = f(x + 0.5 * h, y + 0.5 * h * k2y, z + 0.5 * h * k2z)

        k4y = z + h * k3z
        k4z = f(x + h, y + h * k3y, z + h * k3z)

        y += (h / 6.0) * (k1y + 2*k2y + 2*k3y + k4y)
        z += (h / 6.0) * (k1z + 2*k2z + 2*k3z + k4z)
        x += h

        x_vals.append(x)
        y_vals.append(y)
        z_vals.append(z)

    return x_vals, y_vals, z_vals


def linearShooting(f, a, b, ya, yb, h):
    # Solve first IVP
    x1, y1, z1 = rk4(f, a, ya, 0.0, h, b)

    # Solve second IVP
    x2, y2, z2 = rk4(f, a, 0.0, 1.0, h, b)

    # Compute constant c
    c = (yb - y1[-1]) / y2[-1]

    # Construct final solution
    y_final = [y1[i] + c * y2[i] for i in range(len(y1))]

    # Print sample values
    step_show = int(0.1 / h)
    print(f"c = {c:.6f}")
    for i in range(0, len(x1), step_show):
        print(f"x = {x1[i]:.2f}, y = {y_final[i]:.6f}")

    return x1, y_final


# Parameters
a = 0.0
b = 1.0
ya = 0.0
yb = 1.0
h = 0.01

# Run
print("Linear Shooting Method:")
x_vals, y_vals = linearShooting(f, a, b, ya, yb, h)
