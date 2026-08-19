def flatten_recursive(nl):
    for i in nl:
        if type(i)== list:
            break
    else:
        return nl
    
    add=[]
    for i in nl:
        if isinstance(i,list):
            for j in i:
                add.append(j)
            continue
        add.append(i)
    return flatten_recursive(add)


def flatten_string_eval(nl):
    nl = str(nl)
    lt ="["
    for i in range(1,len(nl)-1):
        if nl[i] not in "[]":
            lt += nl[i]
    lt +="]"
    lt = eval(lt)
    return lt


def flatten_iterative(nl):
    while True:
        add=[]
        for i in nl:
            if isinstance(i,list):
                for j in i:
                    add.append(j)
                continue
            add.append(i)
        nl = add

        if not any(isinstance(i,list) for i in add):
            break
    return add

print(flatten_recursive([1, [2, [3, 4]],[[3, 4],9], 5, 5]))
