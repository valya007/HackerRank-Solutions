import string
al = string.ascii_lowercase

n = 5
line = 4*n-3
row = 2*n-1

s = "-"

def create_text(midpoint,lenside):    
    text = ""
    i = midpoint + lenside
    while i != midpoint:
        text += al[i] + s
        i = i - 1
    i = midpoint
    while i < midpoint + lenside:
        text += al[i] + s
        i = i + 1
    text += al[midpoint + lenside]
    return text  

for i in range(row):
    midpoint = abs(n - (i+1))
    if i < n:
        lenside = i
    else:
        lenside = row - i - 1

    text = create_text(midpoint,lenside)
    print (text.center(line,s))

