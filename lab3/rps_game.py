win = ['SP', 'PR', 'RS']
lose = ['PS', 'RP', 'SR']
draw = ['SS', 'PP', 'RR']
combinations = []
i = input()
while i != '':
    combinations.append(i)
    i = input()
for i in combinations:
    if i in win:
        print('True')
    if i in lose:
        print('False')
    if i in draw:
        print('False | False')      
