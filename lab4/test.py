# def lines_intersection(k1, c1, k2, c2):
#     """
#     шукає точки перетину двох прямих
#     """
#     if k1 == k2:
#         return None
#     elif k1 != k2:
#         x = (c2-c1) / (k1-k2)
#         y = k1*x + c1
#     print((round(x, 2), round(y, 2)))

# lines_intersection(2, -2, 1, 0)

# # def lines_intersectionn(k1, c1, k2, c2):
# #     """
# #     counting lines intersection
# #     >>> lines_intersectionn(2, -2, 1, 0)
# #     (2.0, 2.0)
# #     """
# #     try:
# #         x = (c2-c1)/(k1-k2)
# #         y = round(k1 * x + c1 , 2)
# #         x = round(x,2)
# #         print((x, y))
# #     except ArithmeticError:
# #         return None

# # lines_intersectionn(2, -2, 1, 0)

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()


"""
modul to use sqrt
"""
from math import sqrt

def four_lines_area(k1, c1, k2, c2, k3, c3, k4, c4):
    """
    main function
    """
    #перші точки
    t1 = lines_intersection(k1, c1, k2, c2)
    #другі точки
    t2 = lines_intersection(k3, c3, k2, c2)
    #треті точки
    t3 = lines_intersection(k3, c3, k4, c4)
    #четверті точки
    t4 = lines_intersection(k1, c1, k4, c4)
    if (t1 or t2 or t3 or t4) is None:
        return None
    #перша сторона
    a = distance(t1[0], t1[1], t2[0], t2[1])
    #друга сторона
    b = distance(t3[0], t3[1], t2[0], t2[1])
    #третя сторона
    c = distance(t3[0], t3[1], t4[0], t4[1])
    #четверта сторона
    d = distance(t1[0], t1[1], t4[0], t4[1])
    #перша діагональ
    f1 = distance(t1[0], t1[1], t3[0], t3[1])
    #друга діагональ
    f2 = distance(t4[0], t4[1], t2[0], t2[1])
    if (a or b or c or d or f1 or f2) == 0:
        return None
    #площа
    print(quadrangle_area(a, b, c, d, f1, f2))

def lines_intersection(k1, c1, k2, c2):
    """
    counting lines intersection
    """
    try:
        x = (c2-c1)/(k1-k2)
        y = round(k1 * x + c1 , 2)
        x = round(x,2)
        return (x, y)
    except ArithmeticError:
        return None

def distance(x1, y1, x2, y2):
    """
    counting distance between lines intersections
    """
    side_len = round(sqrt((x1-x2)**2 + (y1-y2)**2) , 2)
    return side_len

def quadrangle_area(a, b, c, d, f1, f2):
    """
    counting area
    """
    try:
        area = sqrt((4 * f1**2 * f2**2 - (b**2 + d**2 - a**2 - c**2)**2)/16)
        return round(area,2)
    except ArithmeticError:
        return None

four_lines_area(0, 20, 3, -0.3, 0.1, 10, -5, 3)