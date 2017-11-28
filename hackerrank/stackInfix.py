import this

from stack import Stack
#A+B*C  postfix ABC*+
def infix_to_postfix(infix_expr):
    # Dict that defines the preceeds and their weight
    prec = {}
    prec["*"]   = 3
    prec["/"]   = 3
    prec["+"]  = 2
    prec["-"]   = 2
    prec["("]   = 1

    op_stack = Stack()

    # List variable that would contain the expression and another that has the splited expression

    postfix_list = [] # contains the result of the conversion

    token_list = infix_expr.split()

    for token in token_list:
        print(token)
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token =="(":
            op_stack.push(token)
        elif token ==")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            # First before we push the operand to the stack we want to
            # Make sure that it is not a preceeden to the top most element
            # on the stack. So it is we first pop out the top most element
            # from the stack
            while (not op_stack.is_empty()) and \
            (prec[op_stack.peek()] >=prec[token]):
                postfix_list.append(op_stack.pop())
            # We push the token, which is the operand to the stack because
            # it is preceeded to the top most element on the stack
            op_stack.push(token)

# Now that we have finished processing the infix expression and stack the operands
# on the op_stack we want to pop (remove) all the operands we have on the
# stack and get them to the result which is postfix_list

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return "".join(postfix_list)


print(infix_to_postfix("A + B * D + C"))

print(infix_to_postfix("A + B * ( D + C )  * ( D - C )"))