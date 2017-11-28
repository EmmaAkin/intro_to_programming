

from stack import Stack

def infix_to_postfix(infix_expr):
    op_stack = Stack
    token_list = infix_expr.split()
    postfix_result = []

    prec ={}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    for token in token_list:
        if  token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_result.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token ==")":
            top_token = op_stack.pop()
            while  top_token !="(":
                postfix_result.append(top_token)
                top_token = op_stack.pop()
        else:
            if  not (op_stack.is_empty()) and prec[op_stack.peek()] >= prec[token]:
                postfix_result.append(op_stack.pop())
            op_stack.push(token)
    while not op_stack.is_empty():
        postfix_result.append(op_stack.pop())

    return " ".join(postfix_result)


