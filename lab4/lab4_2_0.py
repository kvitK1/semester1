# """vefe
# """

# all_atrr = dir(str)
# all_methods = []
# for item in all_atrr:
#     if item[2:] != '__' and item[:2] != '__':
#         all_methods.append(item)

# print(len(all_methods))

# # strin_g = dir(str)
# # sr = list(strin_g)
# # strin_g = str(strin_g)
# # b = 0
# # strin_g.startswith('__')
# # for i in sr:
# #     if  strin_g.startswith('__') == False:
# #         b += 1
# # print(b)

# #lst = [func(i) for i in <sequential> if <condition>]
# #списковий вираз
# print(len([item for item in dir(str) if not (item.startswith("__") and
#                                               item.endswith('__'))]))
# a = [item.upper() for item in dir(str) if not (item.startswith("__") and
#                                               item.endswith('__'))]

# print(a)

# print(type(a[12].lower()))


# print('as2'.isalnum())
# srs = "ss ss rs ss"
# print(srs.rfind('ss'))


# def distance(x1, y1, x2, y2):
#     """
#     шукає відстань між двома точками
#     """
#     dis_ce = round(((x2-x1)**2 + (y2-y1)**2)**0.5, 2)
#     print(dis_ce)
# distance(1, 1, 6, 3)

# def lines_intersection(k1, c1, k2, c2):
#     """
#     шукає точки перетину двох прямих
#     """
#     if k1 == k2:
#         return None
#     x = round((c2-c1) / (k2-k1), 2)
#     y = round(k1*x + c1, 2)
#     print(x, y)
# lines_intersection(2, -2, 1, 0)   
def four_lines_area(k1, c1, k2,
            c2, k3, c3, k4, c4):
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
    print(square)

def lines_intersection(k1, c1, k2, c2):
    """
    шукає точки перетину двох прямих
    """
    if k1 == k2:
        return None
    x = round((c2-c1) / (k2-k1), 2)
    y = round(k1*x + c1, 2)
    print(x, y)
lines_intersection(2, -2, 1, 0)

def distance(x1, y1, x2, y2):
    """
    шукає відстань між двома точками
    """
    dis_ce = round(((x2-x1)**2 + (y2-y1)**2)**0.5, 2)
    return dis_ce

def quadrangle_area(a, b, c, d, f1, f2):
    """
    шукає площу опуклого чотирикутника
    """
    S = round(((4*(f1**2)*(f2**2) - (b**2 + d**2 - a**2 - c**2)**2)/16)**0.5, 2)
    return S