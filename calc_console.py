def button_click(char):  # elöszőr kettő taggal rockie

    for i, x in enumerate(char):
        if x.isdigit() == False:
            l_index = i
            op = x
    n1 = [x for i, x in enumerate(char) if i < l_index]
    n2 = [x for i, x in enumerate(char) if i > l_index]

def basic4(n1,op,n2):
    if op == "+":
        return n1+n2
    if op == "-":
        return n1-n2
    if op == "x":
        return n1*n2
    if op == "/" and n2 != 0:
        return n1/n2
    if op == "/" and n2 == 0:
        return "cannot divide by 0"

print(basic4(3,"+",5))

n1 = (str([x for i, x in enumerate(data) if i < l_index])).rstrip('\']').lstrip('[\'')
n1 = "".join([x for i, x in enumerate(data) if i < l_index])
n2 = (str([x for i, x in enumerate(data) if i > l_index])).rstrip('\']').lstrip('[\'')

