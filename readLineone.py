def words(fn):
    file = open(fn)

    filename = fn.split(".")[0]
    newfile = open(filename+"-words.cgn", "w")

    print(text)
    for line in text:
        text =file.readline()
        word = line.split()

        if len(word)==0: continue


    newfile.close

print(words("file.txt"))