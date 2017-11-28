def bar(n):
    return "*" *n

def graph(arr):

    words = {}
    for word in arr:
        words[word] = words.get(word,0)+1
    for word, count in words.items():
        v = bar(count)
        print (word +": "+ v)
        # words.split()

def replace_specialchar(textfile):
    chars = ["." ,  ",", "?", ")","(","<",":","\n",";"]
    for c in chars:
        textfile = text.replace(c,"")
    return textfile


def readfile_text(fn1):
    file = open(fn1, "r")
    text = file.read()

    # Strip the text with special characters
    text = replace_specialchar(text)

    arr_text = text.split()
    return arr_text








    file.close()



    for word, count in words.items():
            print (word +": "+bar(count))



graph(["a","b","c","f","c","f","g","s","d","f","g", "o", "n", "z", "e"])



