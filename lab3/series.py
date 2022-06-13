number = int(input())
string = ""
up = 1
while up < 2*number:
    down = up+1
    if down % 4 != 0:
        string += f'{up}' + '/' + f'{down}' + ' - '
    else:
        string += f'{up}' + '/' + f'{down}' + ' + '
    up += 2
string = string[:((len(string))-3)]   
print(string) 
