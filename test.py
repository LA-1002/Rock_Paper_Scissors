rck = [
'##########',
'##########',
'##########',
'##########',
'##########',
]
pap = [
'##########',
'|        |',
'|        |',
'|        |',
'##########',
]
sci = [
'\     /',
' \   / ', 
'   X   ', 
'  / \  ',
'[]   []',
]
vs = [
'      \       / ========        ',
'       \     /  |               ', 
'        \   /   |======|        ',
'         \ /           |        ',
'          v     =======|        ',
]
lines = [];
for i in range(5):
    line = str(rck[i] + vs[i] + pap[i] + '\n')
    lines.append(line)

for line in lines:
    print(line)



    



