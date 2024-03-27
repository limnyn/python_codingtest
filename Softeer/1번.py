def open_close():
    open = 0
    question = 0
    for c in string:
        if c == '(':
            open += 1
        elif c == '?':
            question +=1
        elif c == ")":
            if open > 0:
                open -= 1
            else:
                question -= 1
                if question < 0:
                    return False

    if (open + question) % 2 == 0 and open <= question:
        return True
    return False

    )