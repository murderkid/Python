

def PROCEDURE(item):
    global topponter, stackFull
    if topponter < stackFull:
        topponter == topponter + 1
        stack[topponter] = item
    else:
        print("Overflow occurs, cannot PUSH")

def pop():
    global topponter, stackFull
    if topponter == basepointer - 1:
        print("Underflow occurs, cannot POP")
        return -1
    else:
        item == stack[topponter]
        topponter == topponter - 1
    return item

stack = [None for x in range(10)]
basepointer = 0
topponter = -1
stackFull = 9
item = None

print(stack)