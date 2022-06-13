def four_lines_area(k1, c1, k2, c2, k3, c3, k4, c4):
    """
    головна функція
    """
    #знайти точки перетину прямих
    point1 = lines_intersection(k1, c1, k2, c2)
    point2 = lines_intersection(k2, c2, k3, c3)
    point3 = lines_intersection(k3, c3, k4, c4)
    point4 = lines_intersection(k1, c1, k4, c4)
    if not point1 or not point2 or not point3 or not point4:
        return None

    #знайти сторони чотирикутника
    a = distance(point1[0], point1[1], point2[0], point2[1])
    b = distance(point2[0], point2[1], point3[0], point3[1])
    c = distance(point3[0], point3[1], point4[0], point4[1])
    d = distance(point1[0], point1[1], point4[0], point4[1])
    if not a or not b or not c or not d:
        return None

    #знайти діагоналі чотирикутника
    f1 = distance(point1[0], point1[1], point3[0], point3[1])
    f2 = distance(point2[0], point2[1], point4[0], point4[1])
    if not f1 or not f2:
        return None

    square = quadrangle_area(a, b, c, d, f1, f2)
    return square

def lines_intersection(k1, c1, k2, c2):
    """
    шукає точки перетину двох прямих
    """
    if k1 == k2:
        return None
    if k1 != k2:
        x = (c2-c1) / (k1-k2)
        y = k1*x + c1
    return (round(x, 2), round(y, 2))

def distance(x1, y1, x2, y2):
    """
    шукає відстань між двома точками
    """
    dis_ce = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return round(dis_ce, 2)

def quadrangle_area(a, b, c, d, f1, f2):
    """
    шукає площу опуклого чотирикутника
    """
    S = ((4*(f1**2)*(f2**2) - (b**2 + d**2 - a**2 - c**2)**2)/16)**0.5
    return round(S, 2)

four_lines_area(0, 20, 3, -0.3, 0.1, 10, -5, 3)

