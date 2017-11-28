def to_upper(fn1, fn2):
    file = open(fn1)
    text = file.read()
    file.close()

    newfile = open(fn2, "wb")
    newfile.write(text.upper())
    newfile.close()
to_upper("fib2.py", "newfile.txt")