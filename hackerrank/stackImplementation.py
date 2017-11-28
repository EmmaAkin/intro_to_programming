from stack import Stack


def par_checker(symbol_items):
    s = Stack()
    balance = True
    index = 0

    while index < len(symbol_items) and balance:
            symbol = symbol_items[index]
            if symbol in "({[":
                s.push(symbol)
            else:
                if s.is_empty():
                    balance = False
                else:
                    top = s.pop()
                    if not matches(top, symbol):
                        balance = False
            index +=1

    if balance and s.is_empty():
        return True
    else:
        return False


def matches(open, close):
    opens ="({["
    closes = ")}]"

    return opens.index(open) == closes.index(close)


print(par_checker(('((()))')))
print(par_checker("((())))"))