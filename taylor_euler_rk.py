# Solve y'' - y' + 3y = x
# Let y' = z  =>  z' = z - 3y + x
# Initial conditions: y(0)=1, z(0)=-2
# Using classical 4th order Runge–Kutta method

def f(x, y, z):
    # z' = z - 3y + x
    return z - 3*y + x

# Initial conditions
x0 = 0.0
y0 = 1.0
z0 = -2.0
h = 0.01     # step size
x_end = 4.0

# Number of steps
n = int((x_end - x0) / h)

# Initialize variables
def rk4Method(f, x0, y0, z0, h, x_end):
    x = x0
    y = y0
    z = z0

    # Lists for results
    x_vals = [x]
    y_vals = [y]
    z_vals = [z]

    # RK4 iteration
    for i in range(n):
        k1y = z
        k1z = f(x, y, z)

        k2y = z + 0.5*h*k1z
        k2z = f(x + 0.5*h, y + 0.5*h*k1y, z + 0.5*h*k1z)

        k3y = z + 0.5*h*k2z
        k3z = f(x + 0.5*h, y + 0.5*h*k2y, z + 0.5*h*k2z)

        k4y = z + h*k3z
        k4z = f(x + h, y + h*k3y, z + h*k3z)

        y = y + (h/6.0)*(k1y + 2*k2y + 2*k3y + k4y)
        z = z + (h/6.0)*(k1z + 2*k2z + 2*k3z + k4z)
        x = x + h

        x_vals.append(x)
        y_vals.append(y)
        z_vals.append(z)

    # Print sample results every 0.5 step
    step_show = int(0.5 / h)
    for i in range(0, len(x_vals), step_show):
        print(f"x = {x_vals[i]:.2f}, y = {y_vals[i]:.6f}, z = {z_vals[i]:.6f}")

def eulerMethod(f, x0, y0, z0, h, x_end):
    x = x0
    y = y0
    z = z0

    # Lists for results
    x_vals = [x]
    y_vals = [y]
    z_vals = [z]

    # Euler iteration
    for i in range(n):
        dy = h * z
        dz = h * f(x, y, z)

        # Apply the changes simultaneously
        y += dy
        z += dz
        x += h

        x_vals.append(x)
        y_vals.append(y)
        z_vals.append(z)


    # Print sample results every 0.5 step
    step_show = int(0.5 / h)
    for i in range(0, len(x_vals), step_show):
        print(f"x = {x_vals[i]:.2f}, y = {y_vals[i]:.6f}, z = {z_vals[i]:.6f}")

def taylorMethod(f, x0, y0, z0, h, x_end):
    x = x0
    y = y0
    z = z0

    # Lists for results
    x_vals = [x]
    y_vals = [y]
    z_vals = [z]

    # Taylor iteration
    for i in range(n):
        y_prime = z
        z_prime = f(x, y, z)
        y_double_prime = z_prime
        # The correct formula for z_double_prime: z' - 3y' + 1
        z_double_prime = z_prime - 3*y_prime + 1

        # Calculate total change for the step
        dy = h * y_prime + (h**2 / 2) * y_double_prime
        dz = h * z_prime + (h**2 / 2) * z_double_prime

        y += dy
        z += dz
        x += h

        x_vals.append(x)
        y_vals.append(y)
        z_vals.append(z)


    # Print sample results every 0.5 step
    step_show = int(0.5 / h)
    for i in range(0, len(x_vals), step_show):
        print(f"x = {x_vals[i]:.2f}, y = {y_vals[i]:.6f}, z = {z_vals[i]:.6f}")

print("RK4th Order")
rk4Method(f, x0, y0, z0, h, x_end)

print("Euler Method")
eulerMethod(f, x0, y0, z0, h, x_end)

print("Taylor Method")
taylorMethod(f, x0, y0, z0, h, x_end)
