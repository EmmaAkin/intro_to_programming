def backup(fn1):
    file = open(fn1, "rb")
    text = file.read()
    file.close()

    newfile = open("backups/"+fn1+".bak", "wb")
    newfile.write(text)
    newfile.close()

backup("read.pdf")


def rename(fn, new_file):
    file = open(fn)
    text = file.read()


    newfile = open(new_file, "w")
    newfile.write(text)
    newfile.close()

    file = open (fn,"w")
    file.write().close()






