# a =5
# b =10
# a,b  = b,a


# c = i > 5 ? 8: 10

# c = 10
# if i > 5:
#     c = 8


elements = [(2, 12, 'Mg'), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
new_elements = sorted(elements, key=lambda e: e[1])

print(new_elements)
