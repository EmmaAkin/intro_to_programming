def read_file(filename):
    f = open(filename)
    text = f.read()
    f.close
    return text

def word_count(text_file):
    words = text.split('  ')
    d = {}
    for word in words:
        word = word.strip('').lower()
        d[word] = d.get(word,0)+1
    return d

def bar(character, n):
    return character *n

def  graph(filename):
    #Get the content of a file
    text = read_file(filename)
    # Building a dictionary of unique words with a count for the number of times they occur
    word_count = word_count(text)

    # Plot the graph
    for key, value in word_count.items():
        print(key, " : " , bar('a', value) )


def graph_inverted(dictionary):
    # Get the max vlaue about the values in the dictionary
    plotPeak = max(dictionary.values())

    # Get the matrix to have the ploted area

    matrix_plot = {}

    for i in dictionary.keys():
        matrix_plot[i] = ("*" *dictionary[i]).rjust(plotPeak," ")
    #get the key of the matrix we formed so It become the label of the plot
    print(matrix_plot)

    dictionary_keys = dictionary.keys()

    for i in range(plotPeak):
        # Loop through the rows of the new matrix to fix the plot points
        for j in matrix_plot:
            print(matrix_plot[j][i], end="\t")
        print("")

    for i in dictionary_keys: print(i+"", end="\t")


dict_data_points = {'a':1,'b':2,'c':3}
graph_inverted(dict_data_points)


