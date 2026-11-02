sp = []
def push(x):
    global sp
    sp.append(x)
    return

def pop():
    global sp
    temp = sp[-1]
    sp.pop()
    return temp

def back():
    global sp
    return sp[-1]

def clear():
    global sp
    sp.clear()
    return

def size():
    global sp
    return len(sp)

