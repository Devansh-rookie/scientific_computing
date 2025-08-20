
def euler(x0: float, y0: float, h: float, xf: float, func) -> tuple[float, list]:
    y = y0
    x = x0
    result = [(x, y)]
    for _ in range(int((xf - x0) / h)):
        y = y + h * func(x, y)
        x = x + h
        result.append((x, y))
    return y, result

def main():
    x0 = 0
    y0 = 1
    xf = 1
    h = 0.1
    # n = int((xf - x0) / h)
    def f(x:float, y:float) -> float:
        return x + y
    tup = euler(x0, y0, h, xf, f)
    print(tup[0])
    for (x, y) in tup[1]:
        print(f"x = {x:.6f}, y = {y:.6f}")


main()
