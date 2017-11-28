def read_file(filename):
    f = open(filename)
    text = f.read()
    f.close
    return text

def word_count(text_file):
    words = text.split('  ')
    d = {}
    for word in words:
        word = word.strip(' ./';<>":][}{=-_+)(*&^%$#@!`~\|").lower()
        d[word] = d.get(word,0)+1
    return d

def bar(character, n):
    return character *n

def graph(filename):
    #Get the content of a file
    text = read_file(filename)
    # Building a dictionary of unique words with a count for the number of times they occur
    word_count = word_count(text)

    # Plot the graph

    for key, value in word_count.items():
        print(key, " : " , bar('a', value) )


graph()