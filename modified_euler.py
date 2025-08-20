def modified_euler(x0: float, y0: float, h: float, xf: float, f) -> tuple[float, list[tuple[float, float]]]:
    x = x0
    y = y0
    tup = [(x, y)]
    n = int((xf - x0) / h)
    for _ in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        y = y + k2
        x = x + h
        tup.append((x, y))
    return (y, tup)

def main():
    x0 = 0
    y0 = 1
    xf = 1
    h = 0.1
    # n = int((xf - x0) / h)
    def f(x:float, y:float) -> float:
        return x + y
    tup = modified_euler(x0, y0, h, xf, f)
    print(tup[0])
    for (x, y) in tup[1]:
        print(f"x = {x:.6f}, y = {y:.6f}")


main()
