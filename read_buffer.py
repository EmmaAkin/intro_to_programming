import random, time
start_time = time.clock()

def backup(fn1):
    buffersize = 50000
    file = open(fn1, "r")
    newfile = open("backups/"+fn1+".bak", "w")
    buffertext = file.read(buffersize)

    while len(buffertext):
        newfile.write(buffertext)
        print(".", end ='')

    print("Done")

    file.close()

    newfile.close()

backup("read.pdf")

print("%s it to"%(time.clock-start_time))





